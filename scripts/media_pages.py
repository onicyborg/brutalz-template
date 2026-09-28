"""Phase 7 galleries, sliders, and timeline using local artwork."""

from html import escape

MEDIA_PAGES = ('light-gallery', 'gallery1', 'carousel', 'owl-carousel', 'timeline')

ARTWORK = [
    ('studio', 'Studio North', 'Website', 'Ruang digital untuk ide yang berani.'),
    ('forma', 'Forma Objects', 'Branding', 'Bentuk sederhana, kesan yang menetap.'),
    ('pocket', 'Pocket Club', 'Aplikasi', 'Keuangan terasa lebih dekat.'),
    ('bloom', 'Bloom Market', 'Branding', 'Pasar tanaman dengan semangat baru.'),
    ('mono', 'Mono Journal', 'Website', 'Cerita yang nyaman untuk dibaca.'),
    ('move', 'Move Together', 'Aplikasi', 'Kemajuan kecil yang dirayakan bersama.'),
]


def image(name, alt, loading='lazy'):
    return (f'<img src="assets/img/workspace/{name}.svg" alt="{escape(alt, quote=True)}" '
            f'width="720" height="480" loading="{loading}">')


def card(title, description, body, extra=''):
    return ('<section class="card media-panel ' + extra + '"><div class="card-body">'
            + '<div class="panel-heading"><div><h2>' + escape(title) + '</h2><p>'
            + escape(description) + '</p></div></div>' + body + '</div></section>')


def light_gallery(heading):
    tiles = ''.join(
        f'<a class="light-gallery-item media-tile glightbox" href="assets/img/workspace/{name}.svg" '
        f'data-gallery="workspace" data-title="{escape(title, quote=True)}" '
        f'data-description="{escape(description, quote=True)}" aria-label="Perbesar karya {escape(title, quote=True)}">'
        + image(name, 'Ilustrasi karya ' + title, 'eager' if index == 0 else 'lazy')
        + f'<span class="media-tile-caption"><strong>{escape(title)}</strong><small>{escape(category)} ↗</small></span></a>'
        for index, (name, title, category, description) in enumerate(ARTWORK)
    )
    return (heading('Karya yang layak dilihat dekat.', 'Klik ilustrasi untuk membuka lightbox dan telusuri dengan tombol panah atau sentuhan.')
            + '<p class="alert alert-info small">Galeri ini memakai GLightbox lokal dan ilustrasi SVG asli template. Tidak ada gambar atau skrip yang diambil dari CDN.</p>'
            + '<div id="lightGallery" class="media-gallery-grid">' + tiles + '</div>')


def gallery_one(heading):
    tiles = ''.join(
        f'<figure class="masonry-item media-tile"><div class="masonry-art">'
        + image(name, 'Ilustrasi karya ' + title, 'eager' if index == 0 else 'lazy')
        + f'</div><figcaption><span class="badge bg-{("yellow", "purple", "green")[index % 3]}">{escape(category)}</span>'
        + f'<h2>{escape(title)}</h2><p>{escape(description)}</p></figcaption></figure>'
        for index, (name, title, category, description) in enumerate(ARTWORK)
    )
    return (heading('Kumpulan ide di satu kanvas.', 'Galeri masonry responsif dengan kolom CSS dan tanpa pustaka JavaScript.')
            + '<div class="masonry-gallery">' + tiles + '</div>')


def carousel_item(name, title, category, description, active=False):
    return ('<div class="carousel-item' + (' active' if active else '') + '">'
            + image(name, 'Ilustrasi karya ' + title, 'eager')
            + '<div class="media-slide-caption"><span class="badge bg-yellow">'
            + escape(category) + '</span><h3>' + escape(title) + '</h3><p>'
            + escape(description) + '</p></div></div>')


def carousel_controls(id_):
    return (f'<button class="carousel-control-prev" type="button" data-bs-target="#{id_}" data-bs-slide="prev" aria-label="Slide sebelumnya">'
            '<span aria-hidden="true">←</span></button>'
            f'<button class="carousel-control-next" type="button" data-bs-target="#{id_}" data-bs-slide="next" aria-label="Slide berikutnya">'
            '<span aria-hidden="true">→</span></button>')


def bootstrap_carousel(heading):
    hero = ('<div id="mediaHeroCarousel" class="carousel slide media-carousel" data-bs-ride="false">'
            + '<div class="carousel-indicators">'
            + ''.join(f'<button type="button" data-bs-target="#mediaHeroCarousel" data-bs-slide-to="{index}" '
                      + ('class="active" aria-current="true" ' if index == 0 else '')
                      + f'aria-label="Slide {index + 1}"></button>' for index in range(3))
            + '</div><div class="carousel-inner">'
            + ''.join(carousel_item(*ARTWORK[index], index == 0) for index in range(3))
            + '</div>' + carousel_controls('mediaHeroCarousel') + '</div>')
    groups = [ARTWORK[:3], ARTWORK[3:]]
    multi = ('<div id="mediaMultiCarousel" class="carousel slide media-carousel-multi" data-bs-ride="false"><div class="carousel-inner">'
             + ''.join('<div class="carousel-item' + (' active' if index == 0 else '') + '"><div class="row g-3">'
                       + ''.join('<div class="col-12 col-sm-4"><article class="media-mini-card">'
                                 + image(name, 'Ilustrasi karya ' + title, 'eager')
                                 + '<h3>' + escape(title) + '</h3><p>' + escape(category) + '</p></article></div>'
                                 for name, title, category, _ in group)
                       + '</div></div>' for index, group in enumerate(groups))
             + '</div>' + carousel_controls('mediaMultiCarousel') + '</div>')
    caption = ('<div id="mediaCaptionCarousel" class="carousel slide media-caption-carousel" data-bs-ride="false"><div class="carousel-inner">'
               + ''.join(carousel_item(*ARTWORK[index], index == 3) for index in range(3, 6))
               + '</div>' + carousel_controls('mediaCaptionCarousel') + '</div>')
    return (heading('Slide demi slide, tetap berani.', 'Tiga variasi carousel bawaan Bootstrap 5: hero, kumpulan kartu, dan cerita dengan caption.')
            + '<div class="d-grid gap-4">'
            + card('Hero dengan indikator', 'Satu karya per slide, dengan kontrol dan indikator posisi.', hero)
            + card('Beberapa kartu sekaligus', 'Dua kelompok karya dalam susunan responsif.', multi)
            + card('Caption yang menonjol', 'Cerita singkat di atas ilustrasi karya.', caption)
            + '</div>')


def owl_item(name, title, category, description):
    return ('<article class="media-owl-item">' + image(name, 'Ilustrasi karya ' + title, 'eager')
            + '<div><span class="badge bg-yellow">' + escape(category) + '</span><h3>'
            + escape(title) + '</h3><p>' + escape(description) + '</p></div></article>')


def owl_carousel(heading):
    basic = '<div id="owlBasic" class="owl-carousel owl-theme">' + ''.join(owl_item(*art) for art in ARTWORK) + '</div>'
    autoplay = '<div id="owlAutoplay" class="owl-carousel owl-theme">' + ''.join(owl_item(*art) for art in ARTWORK) + '</div>'
    thumbs = '<div id="owlThumbs" class="owl-carousel owl-theme">' + ''.join(owl_item(*art) for art in ARTWORK) + '</div>'
    thumb_buttons = ''.join(
        f'<button type="button" class="media-thumb {"active" if index == 0 else ""}" data-owl-thumb="{index}" '
        f'aria-label="Tampilkan {escape(title, quote=True)}" aria-pressed="{"true" if index == 0 else "false"}">'
        + image(name, '','eager') + '</button>'
        for index, (name, title, _, _) in enumerate(ARTWORK)
    )
    return (heading('Geser, jelajahi, ulangi.', 'Owl Carousel lokal untuk kartu karya yang nyaman digeser pada desktop maupun mobile.')
            + '<div class="d-grid gap-4">'
            + card('Carousel dasar', 'Geser dengan pointer atau sentuhan; jumlah kartu menyesuaikan lebar layar.', basic)
            + card('Autoplay dengan kendali', 'Slide berganti otomatis; jeda tersedia saat dibutuhkan.',
                   '<div class="d-flex justify-content-end mb-3"><button id="owlAutoplayToggle" class="btn btn-sm" type="button" aria-pressed="false">Jeda autoplay</button></div>' + autoplay)
            + card('Navigasi thumbnail', 'Pilih ilustrasi kecil untuk pindah ke slide terkait.',
                   thumbs + '<div class="media-thumb-nav" role="group" aria-label="Pilih slide karya">' + thumb_buttons + '</div>')
            + '</div>')


def timeline(heading):
    events = [
        ('28 Sep 2026', 'Konsep disetujui', 'Arah visual baru dipilih untuk Studio North.', 'bg-purple'),
        ('25 Sep 2026', 'Eksplorasi warna', 'Palet pastel dan border tegas diuji bersama tim.', 'bg-yellow'),
        ('22 Sep 2026', 'Prototype pertama', 'Alur halaman awal siap dipakai untuk diskusi.', 'bg-green'),
        ('18 Sep 2026', 'Kickoff proyek', 'Tujuan, ruang lingkup, dan ritme kerja disepakati.', 'bg-orange'),
    ]
    vertical = '<ol class="media-timeline media-timeline-single">' + ''.join(
        f'<li><span class="media-timeline-date">{date}</span><span class="media-timeline-marker {color}" aria-hidden="true"></span>'
        f'<div class="media-timeline-content"><h3>{title}</h3><p>{description}</p></div></li>'
        for date, title, description, color in events
    ) + '</ol>'
    zigzag = '<ol class="media-timeline media-timeline-zigzag">' + ''.join(
        f'<li><span class="media-timeline-date">{date}</span><span class="media-timeline-marker {color}" aria-hidden="true"></span>'
        f'<div class="media-timeline-content"><h3>{title}</h3><p>{description}</p></div></li>'
        for date, title, description, color in events
    ) + '</ol>'
    attachments = '<ol class="media-timeline media-timeline-single">' + ''.join(
        f'<li><span class="media-timeline-date">{date}</span><span class="media-timeline-marker bg-yellow" aria-hidden="true"></span>'
        '<div class="media-timeline-content"><h3>' + escape(title) + '</h3><p>' + escape(description) + '</p>'
        + image(name, 'Lampiran ' + title) + '</div></li>'
        for date, title, description, name in [
            ('28 Sep 2026', 'Moodboard studio', 'Pilihan warna dan komposisi awal.', 'studio'),
            ('24 Sep 2026', 'Eksplorasi identitas', 'Bentuk yang paling sesuai dengan cerita brand.', 'forma'),
        ]
    ) + '</ol>'
    return (heading('Proses punya cerita.', 'Tiga pola timeline untuk memperlihatkan perjalanan proyek dengan jelas.')
            + '<div class="d-grid gap-4">'
            + card('Alur vertikal', 'Aktivitas terbaru di atas, mudah dipindai.', vertical)
            + card('Kiri dan kanan', 'Ritme zigzag pada layar besar, satu kolom pada layar kecil.', zigzag)
            + card('Dengan lampiran gambar', 'Tampilkan aset yang memberi konteks pada sebuah milestone.', attachments)
            + '</div>')


def build_media_pages(heading):
    return {
        'light-gallery': light_gallery(heading),
        'gallery1': gallery_one(heading),
        'carousel': bootstrap_carousel(heading),
        'owl-carousel': owl_carousel(heading),
        'timeline': timeline(heading),
    }
