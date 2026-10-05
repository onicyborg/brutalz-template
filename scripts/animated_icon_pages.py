"""Animated icon gallery, backed by the local Lordicon player and demo assets."""

from html import escape
import json

ANIMATED_ICONS = (
    ('coins', 'Coins', 'loop(1800)', 'loop-spin'),
    ('download', 'Download', 'click', 'hover-pinch'),
    ('lock', 'Lock', 'hover', 'hover-locked'),
    ('lock-alt', 'Unlock', 'click', 'hover-unlocked'),
    ('puzzle', 'Puzzle', 'hover', 'hover-detach'),
    ('trash', 'Trash', 'loop(1800)', 'hover-trash-empty'),
)


def write_animated_data(root):
    data = {
        name: json.loads((root / 'assets/bundles/lordicon/icons' / f'{name}.json').read_text())
        for name, *_ in ANIMATED_ICONS
    }
    # Inline data also supports opening the generated HTML directly via file://.
    (root / 'assets/js/animated-icon-data.js').write_text(
        '// Generated from the local Lordicon JSON assets. Do not edit manually.\n'
        + 'window.BRUTAL_ANIMATED_ICONS = ' + json.dumps(data, separators=(',', ':')) + ';\n',
        encoding='utf-8',
    )


def animated_icons(heading, scaffold):
    cards = []
    for name, label, trigger, state in ANIMATED_ICONS:
        snippet = (
            f'<button type="button" class="animated-icon-target" aria-label="{label}">\n'
            f'  <lord-icon src="assets/bundles/lordicon/icons/{name}.json"\n'
            f'    trigger="{trigger}" target=".animated-icon-target" state="{state}"\n'
            '    colors="primary:#232420,secondary:#a78bfa" style="width:80px;height:80px"\n'
            '    aria-hidden="true"></lord-icon>\n</button>'
        )
        mode = 'Otomatis' if trigger.startswith('loop') else trigger.title()
        cards.append(
            f'<div class="col-sm-6 col-xl-4 icon-item" data-icon-name="{label.lower()}">'
            '<article class="icon-card h-100 animated-icon-card">'
            f'<button type="button" class="icon-preview animated-icon-target" aria-label="Putar animasi {label}">'
            f'<lord-icon data-icon="{name}" data-default-trigger="{trigger}" state="{state}" '
            'colors="primary:#232420,secondary:#a78bfa" target=".animated-icon-target" aria-hidden="true"></lord-icon>'
            '</button><div class="icon-card-meta">'
            f'<h3>{label}</h3><span class="badge bg-yellow animated-mode">{mode}</span></div>'
            '<p class="small text-muted mb-0 animated-hint">Hover, fokuskan, atau tekan ikon untuk mencoba.</p>'
            f'<pre class="animated-code mb-0"><code>{escape(snippet)}</code></pre>'
            f'<button type="button" class="btn btn-sm icon-copy align-self-start" data-copy="{escape(snippet, quote=True)}" '
            f'aria-label="Salin kode {label}">Salin kode</button></article></div>'
        )
    controls = '''
    <section class="card mb-4" aria-label="Pengaturan animasi">
      <div class="card-body">
        <div class="row g-3 align-items-end">
          <div class="col-md-5">
            <label class="form-label fw-bold" for="animatedTrigger">Pemicu animasi</label>
            <select id="animatedTrigger" class="form-select">
              <option value="default">Variasi demo</option>
              <option value="hover">Hover / fokus</option>
              <option value="click">Klik / sentuh</option>
              <option value="loop(1800)">Otomatis berulang</option>
            </select>
          </div>
          <div class="col-md-3">
            <label class="form-label fw-bold" for="animatedSpeed">Kecepatan</label>
            <select id="animatedSpeed" class="form-select">
              <option value="0.5">0,5×</option><option value="1" selected>1× Normal</option><option value="1.5">1,5×</option><option value="2">2×</option>
            </select>
          </div>
          <div class="col-md-4"><button type="button" class="btn btn-dark w-100" id="animatedPause" aria-pressed="false">Jeda semua animasi</button></div>
        </div>
        <p class="small text-muted mt-3 mb-0" id="animatedStatus" role="status">Pilih pemicu, lalu coba ikon di bawah. Tombol ikon juga mendukung Enter dan Space.</p>
      </div>
    </section>'''
    usage = '''
    <section class="card mt-4"><div class="card-body">
      <h2 class="fs-4">Pakai di halamanmu</h2>
      <p>Muat player satu kali, lalu tempel kode dari kartu. Path aset mengikuti root template. Jalankan melalui server lokal (<code>npm run dev</code>) agar file JSON pada snippet dapat dimuat.</p>
      <pre class="animated-code"><code>&lt;script src="assets/bundles/lordicon/lordicon.js"&gt;&lt;/script&gt;</code></pre>
      <p>Untuk memicu animasi dari aksi aplikasi, panggil <code>play()</code>. Contoh di bawah memakai event klik tombol.</p>
      <div class="d-flex flex-wrap align-items-center gap-3 mb-3">
        <lord-icon id="animatedEventIcon" data-icon="download" state="hover-pinch" colors="primary:#232420,secondary:#a78bfa" aria-hidden="true"></lord-icon>
        <button type="button" class="btn btn-dark" id="animatedEventButton">Simulasikan unduhan</button>
        <span class="small text-muted" id="animatedEventStatus" role="status">Siap dicoba.</span>
      </div>
      <pre class="animated-code mb-3"><code>const icon = document.querySelector('lord-icon');
// Panggil saat aksi aplikasi selesai.
icon.play({ from: 'start' });</code></pre>
      <p class="small text-muted mb-0">Player dan aset contoh disimpan lokal. Preferensi reduced motion dihormati secara otomatis.
      Ikon oleh <a href="https://lordicon.com/">Lordicon</a> · <a href="https://lordicon.com/docs/web">Dokumentasi</a>.</p>
    </div></section>'''
    return scaffold(
        heading, 'Ikon dengan cerita kecil.',
        'Animasi pada detail ikon: coba hover, klik, atau putar otomatis.',
        'LORDICON · ANIMATED ICONS',
        'Enam ikon interaktif dengan garis tegas dan warna khas BRUTAL. Pilih pemicu dan kecepatan, lalu salin kode sesuai pengaturanmu.',
        controls + '<section class="icon-section"><div class="row g-4">' + ''.join(cards) + '</div></section>' + usage,
    )
