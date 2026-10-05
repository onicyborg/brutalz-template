"""Phase 6 icon library showcases. Only selected SVG assets are bundled."""

from html import escape
from pathlib import Path
import json
from animated_icon_pages import animated_icons

ICON_PAGES = (
    'icon-font-awesome', 'icon-material', 'icon-ionicons',
    'icon-feather', 'icon-weather-icon', 'icon-animated',
)

ROOT = Path(__file__).resolve().parent.parent


def icon_card(label, preview, snippet, copy_key=None):
    safe_label = escape(label)
    copy_attribute = (f' data-copy-key="{escape(copy_key, quote=True)}"' if copy_key else
                      f' data-copy="{escape(snippet, quote=True)}"')
    return (
        '<div class="col-6 col-md-4 col-xl-3 icon-item" data-icon-name="'
        + escape(label.lower(), quote=True) + '"><article class="icon-card h-100">'
        + '<div class="icon-preview" aria-hidden="true">' + preview + '</div>'
        + '<div class="icon-card-meta"><h3>' + safe_label + '</h3>'
        + '<button type="button" class="btn btn-sm icon-copy"' + copy_attribute + ' aria-label="Salin kode '
        + safe_label + '">Salin kode</button></div>'
        + '<code>' + escape(snippet) + '</code></article></div>'
    )


def section(title, description, cards):
    return (
        '<section class="icon-section mb-5"><div class="d-flex flex-wrap align-items-end justify-content-between gap-2 mb-3">'
        + '<div><h2 class="fs-4 mb-1">' + escape(title) + '</h2><p class="text-muted mb-0">'
        + escape(description) + '</p></div><span class="badge bg-yellow">'
        + str(len(cards)) + ' ikon</span></div><div class="row g-3">'
        + ''.join(cards) + '</div></section>'
    )


def scaffold(heading, title, subtitle, library, intro, body):
    return (
        heading(title, subtitle)
        + '<section class="card icon-guide mb-4"><div class="card-body">'
        + '<span class="badge bg-purple mb-3">' + escape(library) + '</span>'
        + '<p class="mb-0">' + intro + '</p></div></section>'
        + '<div class="row g-3 align-items-end mb-4"><div class="col-md-7">'
        + '<label class="form-label fw-bold" for="iconSearch">Cari ikon di halaman ini</label>'
        + '<input id="iconSearch" class="form-control" type="search" autocomplete="off" placeholder="Contoh: home, cloud, calendar…">'
        + '</div><div class="col-md-5"><p class="small text-muted mb-0" id="iconCount" role="status"></p></div></div>'
        + '<p id="iconEmpty" class="alert alert-warning d-none">Tidak ada ikon yang cocok. Coba kata lain.</p>'
        + body + '<p id="iconCopyStatus" class="visually-hidden" role="status" aria-live="polite"></p>'
    )


def svg_asset(collection, name):
    return (ROOT / 'assets/bundles' / collection / 'svg' / (name + '.svg')).read_text(encoding='utf-8').strip()


FEATHER_PAIRS = [
    ('Dashboard', 'grid'), ('Grafik', 'bar-chart-2'), ('Folder', 'folder'),
    ('Kalender', 'calendar'), ('Lapisan', 'layers'), ('Dokumen', 'file-text'),
    ('Pengguna', 'user'), ('Tim', 'users'), ('Kunci', 'lock'),
    ('Cari', 'search'), ('Notifikasi', 'bell'), ('Tambah', 'plus'),
    ('Panah', 'arrow-right'), ('Tren', 'trending-up'), ('Centang', 'check'),
    ('Menu', 'menu'), ('Keluar', 'log-out'), ('Kilat', 'zap'),
    ('Kode', 'code'), ('Email', 'mail'), ('Favorit', 'heart'),
    ('Lihat', 'eye'), ('Pengaturan', 'settings'), ('Unduh', 'download'),
]


def write_feather_data(root):
    entries = {name: svg_asset('feather', name) for _, name in FEATHER_PAIRS}
    output = '// Generated from official local Feather SVGs by scripts/icon_pages.py.\n'
    output += 'window.BRUTAL_FEATHER_SVG = {\n'
    output += ',\n'.join(f'  {json.dumps(name)}: {json.dumps(svg)}' for name, svg in entries.items())
    output += '\n};\n'
    (root / 'assets/js/feather-data.js').write_text(output, encoding='utf-8')


def build_icon_pages(heading):
    solid = [
        ('House', 'house'), ('Magnifying glass', 'magnifying-glass'),
        ('User', 'user'), ('Gear', 'gear'), ('Bell', 'bell'),
        ('Envelope', 'envelope'), ('Calendar', 'calendar'),
        ('Chart line', 'chart-line'), ('Folder', 'folder'),
        ('Download', 'download'), ('Heart', 'heart'), ('Star', 'star'),
    ]
    regular = [
        ('User', 'user'), ('Bell', 'bell'), ('Calendar', 'calendar'),
        ('Envelope', 'envelope'), ('Heart', 'heart'), ('Star', 'star'),
    ]
    brands = [
        ('GitHub', 'github'), ('Instagram', 'instagram'), ('YouTube', 'youtube'),
        ('LinkedIn', 'linkedin'), ('Figma', 'figma'), ('Dribbble', 'dribbble'),
    ]
    def fa_cards(items, family):
        return [icon_card(label, f'<i class="fa-{family} fa-{name}"></i>',
                          f'<i class="fa-{family} fa-{name}"></i>') for label, name in items]

    fa_body = (
        section('Solid', 'Ikon penuh untuk aksi dan navigasi.', fa_cards(solid, 'solid'))
        + section('Regular', 'Versi garis untuk UI yang lebih ringan.', fa_cards(regular, 'regular'))
        + section('Brands', 'Logo brand resmi dari koleksi gratis.', fa_cards(brands, 'brands'))
    )
    fa = scaffold(heading, 'Satu simbol, banyak ide.', 'Font Awesome Free: solid, regular, dan brand dalam grid yang siap disalin.',
                  'FONT AWESOME FREE', 'CSS dan webfont diambil dari paket Font Awesome Free lokal. Salin snippet HTML pada kartu; stylesheet hanya diperlukan pada halaman yang memakai ikon.', fa_body)

    material_names = [
        'home', 'search', 'person', 'settings', 'notifications', 'mail',
        'event', 'favorite', 'star', 'shopping_cart', 'chat', 'cloud',
        'wb_sunny', 'brightness_2', 'photo_camera', 'description',
        'file_download', 'share', 'verified_user', 'palette',
        'dashboard', 'menu', 'edit', 'delete',
    ]
    material_cards = [icon_card(name.replace('_', ' ').title(),
                                f'<span class="material-icons">{name}</span>',
                                f'<span class="material-icons">{name}</span>') for name in material_names]
    material = scaffold(heading, 'Material, terasa familiar.', 'Icon font Material dengan ligature yang mudah ditempel ke markup.',
                        'MATERIAL ICONS', 'Font Material Icons di-host lokal. Nama ikon ditulis sebagai teks ligature di dalam elemen <code>.material-icons</code>.',
                        section('Pilihan populer', 'Ikon untuk navigasi, konten, status, dan aksi.', material_cards))

    ion_names = [
        'home', 'search', 'person', 'settings', 'notifications', 'mail',
        'calendar', 'heart', 'star', 'cart', 'chatbubble', 'cloud',
        'sunny', 'moon', 'camera', 'document', 'download', 'share-social',
        'shield-checkmark', 'color-palette', 'logo-github', 'logo-instagram',
        'logo-youtube', 'logo-linkedin',
    ]
    ion_cards = [icon_card(name.replace('-', ' ').title(),
                           f'<img src="assets/bundles/ionicons/svg/{name}.svg" alt="">',
                           f'<img src="assets/bundles/ionicons/svg/{name}.svg" alt="">') for name in ion_names]
    ion = scaffold(heading, 'Ionicons untuk semua sudut.', 'Ikon Ionic modern sebagai SVG lokal, tanpa permintaan jaringan tambahan.',
                   'IONICONS', 'File SVG resmi disimpan lokal. Snippet memakai <code>&lt;img&gt;</code>; untuk ikon dekoratif, atribut <code>alt</code> boleh kosong.',
                   section('Interface dan brand', 'Ikon bentuk penuh yang bekerja tanpa runtime JavaScript.', ion_cards))

    feather_cards = [icon_card(label,
                               f'<img src="assets/bundles/feather/svg/{name}.svg" alt="">',
                               f'<svg class="feather feather-{name}">…</svg>', name)
                     for label, name in FEATHER_PAIRS]
    feather = scaffold(heading, 'Tipis, jelas, serbaguna.', 'Feather SVG dengan gaya garis yang dekat dengan ikon sidebar BRUTAL.',
                       'FEATHER ICONS', 'Klik “Salin kode” untuk menyalin markup SVG lengkap. Ikon sidebar template dibuat terpisah; koleksi ini memakai aset Feather resmi.',
                       section('Ikon antarmuka', 'Pratinjau SVG lokal, dengan markup inline siap disalin.', feather_cards))

    weather_groups = [
        ('Siang', ['day-sunny', 'day-cloudy', 'day-rain', 'day-showers', 'day-snow', 'day-thunderstorm']),
        ('Malam', ['night-clear', 'night-alt-cloudy', 'night-alt-rain', 'night-alt-snow', 'night-alt-thunderstorm', 'night-fog']),
        ('Kondisi', ['cloud', 'cloudy', 'rain', 'showers', 'snow', 'fog', 'strong-wind', 'humidity', 'thermometer', 'umbrella', 'sunrise', 'sunset']),
    ]
    weather_body = ''.join(section(title, 'Kelas CSS dapat dipakai bersama warna dan ukuran tema.',
                                   [icon_card(name.replace('-', ' ').title(), f'<i class="wi wi-{name}"></i>',
                                              f'<i class="wi wi-{name}"></i>') for name in names])
                           for title, names in weather_groups)
    weather = scaffold(heading, 'Prakiraan dengan karakter.', 'Weather Icons: koleksi cuaca berbasis font lokal.',
                       'WEATHER ICONS', 'Gunakan kelas <code>wi</code> dan <code>wi-*</code> bersama. Font dan CSS tersedia di bundle lokal.', weather_body)

    return dict(zip(ICON_PAGES, (fa, material, ion, feather, weather, animated_icons(heading, scaffold))))
