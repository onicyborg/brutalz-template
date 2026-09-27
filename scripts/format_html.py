#!/usr/bin/env python3
"""
Rapikan file HTML: pecah tag, tambahkan indentasi, tanpa mengubah isi.

Menggunakan lxml untuk parsing struktur (entities di-decode).
Untuk raw text elements (<pre>, <script>, <style>, <textarea>), konten
diambil VERBATIM dari source string — supaya entity references seperti
&lt; &gt; &quot; di dalam <pre><code> tetap tampil sebagai teks di browser.

Aturan:
- Block elements: tag pembuka di baris baru (indent), tag penutup di baris baru.
- Inline elements: tetap di baris yang sama.
- Void elements (br, img, dll): inline.
- Raw text elements: tulis konten source apa adanya (no decode).
- Whitespace antara tag block: dibuang.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from lxml import html, etree

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

INLINE_CONTENT_TAGS = {
    "title", "h1", "h2", "h3", "h4", "h5", "h6", "p",
    "li", "dt", "dd", "figcaption", "summary",
}

RAW_TEXT_PARENTS = {"pre", "script", "style", "textarea"}

INDENT = "  "


def _attrs_of(el: html.HtmlElement) -> str:
    parts: list[str] = []
    for name, value in el.attrib.items():
        if value is None:
            parts.append(f" {name}")
        else:
            parts.append(f' {name}="{value}"')
    return "".join(parts)


def _is_void(tag: str) -> bool:
    return tag in VOID_TAGS


def _is_inline_content(tag: str) -> bool:
    return tag in INLINE_CONTENT_TAGS


def _has_only_text(el: html.HtmlElement) -> bool:
    if len(el) == 0:
        return True
    return all(child.tag is etree.Comment for child in el)


def _is_empty_element(el: html.HtmlElement) -> bool:
    if len(el) > 0:
        return False
    if el.text and el.text.strip():
        return False
    return True


def _is_only_text_inline(el: html.HtmlElement) -> bool:
    for child in el:
        if isinstance(child.tag, str):
            return False
    return True


# -------- raw text extraction --------
# Untuk raw text elements (<pre>, <script>, dll), kita perlu ambil konten
# VERBATIM dari source. Pendekatan: cari di source string dari posisi
# tag pembuka sampai tag penutup yang matching.

_TAG_RE = re.compile(r"<\s*([a-zA-Z][a-zA-Z0-9]*)\b([^>]*)>(.*?)</\s*\1\s*>", re.DOTALL)


def _find_raw_content(source: str, tag: str, start_pos: int) -> tuple[str, int] | None:
    """Cari konten raw text element di source.

    Returns (konten_di_antara_tag_pembuka_dan_penutup, posisi_setelah_tag_penutup)
    atau None kalau tidak ketemu.
    """
    # Cari tag pembuka dengan attrs apapun dari posisi start_pos
    open_re = re.compile(rf"<\s*{re.escape(tag)}\b[^>]*>", re.IGNORECASE)
    m = open_re.search(source, start_pos)
    if not m:
        return None
    open_end = m.end()

    # Cari tag penutup
    close_re = re.compile(rf"</\s*{re.escape(tag)}\s*>", re.IGNORECASE)
    m2 = close_re.search(source, open_end)
    if not m2:
        return None
    close_start = m2.start()
    return source[open_end:close_start], m2.end()


def _render_inline(el: html.HtmlElement, depth: int, source_pos: int = 0, source: str = "") -> tuple[str, int]:
    """Return (rendered_string, new_source_pos)."""
    tag = el.tag
    attrs = _attrs_of(el)

    if _is_void(tag):
        return f"<{tag}{attrs}>", source_pos

    if _is_empty_element(el):
        return f"<{tag}{attrs}></{tag}>", source_pos

    if _is_inline_content(tag):
        out = f"<{tag}{attrs}>"
        out += _render_inline_text_content(el, depth)
        out += f"</{tag}>"
        return out, source_pos

    if _has_only_text(el):
        out = f"<{tag}{attrs}>"
        out += _render_inline_text_content(el, depth)
        out += f"</{tag}>"
        return out, source_pos

    # Multiline
    indent = INDENT * depth
    child_indent = INDENT * (depth + 1)
    out = f"<{tag}{attrs}>\n"
    if el.text and el.text.strip():
        out += child_indent + " ".join(el.text.split()) + "\n"

    cur_pos = source_pos
    for child in el:
        if child.tag is etree.Comment:
            out += child_indent + f"<!--{child.text}-->\n"
            continue

        # Jika child adalah raw text element: ambil konten dari source
        if child.tag in RAW_TEXT_PARENTS:
            out += child_indent + _render_raw(child, depth + 1, cur_pos, source)
            cur_pos = _advance_pos(source, cur_pos, child)
            if child.tail and child.tail.strip():
                out += child_indent + " ".join(child.tail.split()) + "\n"
            continue

        if _is_void(child.tag) or _is_empty_element(child) or _has_only_text(child):
            rendered, cur_pos = _render_inline(child, depth + 1, cur_pos, source)
            out += child_indent + rendered + "\n"
        else:
            rendered, cur_pos = _render_block(child, depth + 1, cur_pos, source)
            out += rendered

        if child.tail and child.tail.strip():
            out += child_indent + " ".join(child.tail.split()) + "\n"

    out += indent + f"</{tag}>"
    return out, cur_pos


def _advance_pos(source: str, start_pos: int, el: html.HtmlElement) -> int:
    """Advance position past this element's tags in source."""
    # Cari tag pembuka + closing di source
    open_re = re.compile(rf"<\s*{re.escape(el.tag)}\b[^>]*>", re.IGNORECASE)
    m = open_re.search(source, start_pos)
    if not m:
        return start_pos
    open_end = m.end()
    # Cek apakah self-closing di source
    if source[m.end()-2:m.end()] == "/>":
        return m.end()
    # Cari tag penutup
    close_re = re.compile(rf"</\s*{re.escape(el.tag)}\s*>", re.IGNORECASE)
    m2 = close_re.search(source, open_end)
    if not m2:
        return open_end
    return m2.end()


def _render_raw(el: html.HtmlElement, depth: int, source_pos: int, source: str) -> str:
    """Render raw text element dengan konten VERBATIM dari source.

    Untuk <script src="..."> atau <link> external, render sebagai inline
    satu baris (tidak perlu raw content).
    """
    tag = el.tag
    attrs = _attrs_of(el)
    indent = INDENT * depth

    # External script (memiliki src) atau stylesheet eksternal: render inline
    if el.get("src") or el.get("href"):
        return indent + f"<{tag}{attrs}></{tag}>\n"

    # Cari konten raw dari source
    result = _find_raw_content(source, tag, source_pos)
    if result:
        raw_content, end_pos = result
    else:
        raw_content = ""

    out = f"{indent}<{tag}{attrs}>\n"
    if raw_content:
        lines = raw_content.split("\n")
        for i, line in enumerate(lines):
            if i < len(lines) - 1:
                if line.strip() == "":
                    out += "\n"
                else:
                    out += indent + INDENT + line + "\n"
            else:
                if line:
                    out += indent + INDENT + line + "\n"
    out += f"{indent}</{tag}>\n"
    return out


def _render_inline_text_content(el: html.HtmlElement, depth: int) -> str:
    parts: list[str] = []
    if el.text:
        parts.append(el.text)
    for child in el:
        if child.tag is etree.Comment:
            parts.append(f"<!--{child.text}-->")
        else:
            rendered, _ = _render_inline(child, depth)
            parts.append(rendered)
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)


def _render_block(el: html.HtmlElement, depth: int, source_pos: int = 0, source: str = "") -> tuple[str, int]:
    tag = el.tag
    attrs = _attrs_of(el)
    indent = INDENT * depth

    if _is_inline_content(tag) and _is_only_text_inline(el):
        rendered, source_pos = _render_inline(el, depth, source_pos, source)
        return indent + rendered + "\n", source_pos

    out = f"{indent}<{tag}{attrs}>\n"
    child_depth = depth + 1
    child_indent = INDENT * child_depth

    if el.text:
        if el.text.strip() or _is_inline_content(tag):
            out += child_indent + " ".join(el.text.split()) + "\n"

    cur_pos = source_pos
    for child in el:
        if child.tag is etree.Comment:
            out += child_indent + f"<!--{child.text}-->\n"
            continue

        if child.tag in RAW_TEXT_PARENTS:
            out += _render_raw(child, child_depth, cur_pos, source)
            cur_pos = _advance_pos(source, cur_pos, child)
            if child.tail:
                if child.tail.strip():
                    out += child_indent + " ".join(child.tail.split()) + "\n"
            continue

        ctag = child.tag
        if _is_void(ctag):
            rendered, cur_pos = _render_inline(child, child_depth, cur_pos, source)
            out += child_indent + rendered + "\n"
        elif _is_inline_content(ctag) and _is_only_text_inline(child):
            rendered, cur_pos = _render_inline(child, child_depth, cur_pos, source)
            out += child_indent + rendered + "\n"
        elif _is_only_text_inline(child):
            rendered, cur_pos = _render_inline(child, child_depth, cur_pos, source)
            out += child_indent + rendered + "\n"
        else:
            rendered, cur_pos = _render_block(child, child_depth, cur_pos, source)
            out += rendered

        if child.tail:
            if child.tail.strip():
                out += child_indent + " ".join(child.tail.split()) + "\n"

    out += f"{indent}</{tag}>\n"
    return out, cur_pos


def format_html(content: str) -> str:
    parser = html.HTMLParser(remove_blank_text=False, remove_comments=False)
    root = html.fromstring(content, parser=parser)

    out_parts: list[str] = []

    doctype_match = re.search(r"<!doctype[^>]*>", content, re.IGNORECASE)
    if doctype_match:
        out_parts.append(doctype_match.group(0) + "\n")

    # Cari posisi doctype di source
    source_pos = doctype_match.end() if doctype_match else 0

    if root.tag == "html":
        html_attrs = _attrs_of(root)
        out_parts.append(f"<html{html_attrs}>\n")
        for child in root:
            if child.tag is etree.Comment:
                out_parts.append(f"<!--{child.text}-->\n")
                source_pos = _advance_pos(content, source_pos, child)
                continue

            if child.tag in RAW_TEXT_PARENTS:
                out_parts.append(_render_raw(child, 0, source_pos, content))
                source_pos = _advance_pos(content, source_pos, child)
                continue

            if _is_void(child.tag):
                rendered, source_pos = _render_inline(child, 0, source_pos, content)
                out_parts.append(rendered + "\n")
            elif _is_inline_content(child.tag) and _is_only_text_inline(child):
                rendered, source_pos = _render_inline(child, 0, source_pos, content)
                out_parts.append(rendered + "\n")
            elif _is_only_text_inline(child):
                rendered, source_pos = _render_inline(child, 0, source_pos, content)
                out_parts.append(rendered + "\n")
            else:
                rendered, source_pos = _render_block(child, 0, source_pos, content)
                out_parts.append(rendered)
        out_parts.append("</html>\n")
    else:
        if _is_only_text_inline(root):
            rendered, _ = _render_inline(root, 0)
            out_parts.append(rendered + "\n")
        else:
            rendered, _ = _render_block(root, 0)
            out_parts.append(rendered)

    out = "".join(out_parts)
    out = out.rstrip() + "\n"
    out = re.sub(r"\n{4,}", "\n\n\n", out)
    return out


def verify_semantic(original: str, formatted: str) -> tuple[bool, str]:
    """Verifikasi struktur sama persis.

    Pendekatan pragmatis:
    - Untuk non-raw text elements: whitespace dianggap ekuivalen (collapsed).
    - Untuk raw text elements (<pre>, <script>, <style>, <textarea>):
      teks HARUS identik (preserve entity references).
    - Struktur tag + attrs harus identik.
    """

    def collect(html_str: str):
        """Parse dan return list of (kind, tag, attrs, text_or_None)."""
        events: list[tuple] = []

        try:
            parser = html.HTMLParser(remove_blank_text=False, remove_comments=False)
            root = html.fromstring(html_str, parser=parser)
        except Exception as e:
            return None, f"parse error: {e}"

        def walk(el):
            tag = el.tag
            if isinstance(tag, str):
                attrs = tuple(sorted((k, v) for k, v in el.attrib.items()))
                is_raw = tag in RAW_TEXT_PARENTS
                text = el.text or ""
                # Untuk raw elements, simpan teks TANPA whitespace di awal/akhir
                # (karena formatter menambahkan indentasi)
                if is_raw:
                    text = text.strip()
                else:
                    text = " ".join(text.split())
                events.append(("start", tag, attrs, text if is_raw else (text if text.strip() else None)))
                for child in el:
                    walk(child)
                    tail = child.tail or ""
                    # Untuk tail setelah raw element atau biasa: normalize
                    if child.tag in RAW_TEXT_PARENTS:
                        # tail setelah raw: literal preserve tapi normalize whitespace
                        tail = " ".join(tail.split())
                    else:
                        tail = " ".join(tail.split())
                    events.append(("tail", child.tag if isinstance(child.tag, str) else "comment",
                                   None, tail if tail.strip() else None))
                events.append(("end", tag, None, None))
            else:
                events.append(("comment", str(tag), None, el.text))

        walk(root)
        return events, None

    a, err = collect(original)
    if err:
        return False, f"original: {err}"
    b, err = collect(formatted)
    if err:
        return False, f"formatted: {err}"

    if a == b:
        return True, ""
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            return False, f"diff at event #{i}: orig={a[i]!r} vs new={b[i]!r}"
    return False, f"length differs: {len(a)} vs {len(b)}"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: format_html.py <file_or_dir> [...]", file=sys.stderr)
        return 1

    targets: list[Path] = []
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_dir():
            targets.extend(sorted(p.glob("*.html")))
        else:
            targets.append(p)

    if not targets:
        print("No HTML files found.", file=sys.stderr)
        return 1

    failed: list[tuple[Path, str]] = []
    for path in targets:
        original = path.read_text(encoding="utf-8")
        try:
            formatted = format_html(original)
        except Exception as e:
            print(f"  ERROR     {path.name}: {e}")
            failed.append((path, str(e)))
            continue
        ok, msg = verify_semantic(original, formatted)
        if not ok:
            print(f"  REVERTED  {path.name}: {msg[:200]}")
            failed.append((path, msg))
            continue
        if formatted == original:
            print(f"  no-change  {path.name}")
        else:
            path.write_text(formatted, encoding="utf-8")
            print(f"  formatted  {path.name}")

    if failed:
        print(f"\n{len(failed)} file(s) FAILED (left unchanged).", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
