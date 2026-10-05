"""Phase 2 component showcases built with the shared BRUTAL. page shell."""

ADVANCED_PAGES = (
    'avatar', 'card', 'modal', 'sweet-alert', 'toastr',
    'empty-state', 'multiple-upload', 'tabs',
)


def panel(title, subtitle, content, extra_class=''):
    return f'''
    <section class="card {extra_class}">
      <div class="card-body">
        <div class="panel-heading"><div><h2>{title}</h2><p>{subtitle}</p></div></div>
        {content}
      </div>
    </section>'''


def avatar_page(heading, icon):
    sizes = ''.join(
        f'<div class="avatar-example"><span class="avatar avatar-{size} bg-{color}" aria-label="Avatar {label}">{initials}</span><strong>{label}</strong><small>{pixels} px</small></div>'
        for size, color, label, initials, pixels in [
            ('xs', 'yellow', 'Extra small', 'AD', 24),
            ('sm', 'green', 'Small', 'NS', 28),
            ('md', 'purple', 'Medium', 'RK', 36),
            ('lg', 'orange', 'Large', 'DP', 52),
            ('xl', 'blue', 'Extra large', 'BR', 72),
        ]
    )
    statuses = ''.join(
        f'<div class="avatar-example"><span class="avatar-status-wrap"><span class="avatar avatar-lg bg-{color}">{initials}</span><span class="avatar-status-dot status-{status}" aria-label="{label}"></span></span><strong>{label}</strong><small>{description}</small></div>'
        for color, initials, status, label, description in [
            ('purple', 'NS', 'online', 'Online', 'Siap berkolaborasi'),
            ('yellow', 'RK', 'away', 'Away', 'Sedang istirahat'),
            ('orange', 'DP', 'offline', 'Offline', 'Belum aktif'),
        ]
    )
    groups = '''
    <div class="d-flex flex-wrap align-items-center gap-4">
      <div class="avatar-stack avatar-stack-demo" aria-label="Tim desain: Alex, Nina, Rio, dan 5 anggota lain">
        <span class="avatar bg-purple">AD</span><span class="avatar bg-green">NS</span>
        <span class="avatar bg-orange">RK</span><span class="avatar bg-yellow">+5</span>
      </div>
      <p class="mb-0">Avatar saling bertumpuk untuk menunjukkan anggota tim tanpa memenuhi ruang.</p>
    </div>'''
    placeholders = '''
    <div class="d-flex flex-wrap gap-3 align-items-center">
      <span class="avatar avatar-lg bg-purple" aria-label="Alex Darma">AD</span>
      <span class="avatar avatar-lg bg-green" aria-label="Nina Sari">NS</span>
      <span class="avatar avatar-lg bg-yellow" aria-label="Pengguna tanpa nama">?</span>
      <p class="small text-muted mb-0">Inisial tetap terbaca saat foto profil belum tersedia.</p>
    </div>'''
    return (
        heading('Wajah di balik ide.', 'Avatar sederhana untuk orang, status, dan tim.')
        + '<div class="row g-4"><div class="col-12">'
        + panel('Lima ukuran', 'Skala dari navigasi kecil hingga kartu profil.', f'<div class="avatar-gallery">{sizes}</div>')
        + '</div><div class="col-lg-6">'
        + panel('Status anggota', 'Titik status memiliki label yang dapat dibaca pembaca layar.', f'<div class="avatar-gallery">{statuses}</div>')
        + '</div><div class="col-lg-6 d-grid gap-4">'
        + panel('Avatar group', 'Cocok untuk kolaborator proyek.', groups)
        + panel('Placeholder inisial', 'Tanpa foto atau permintaan jaringan.', placeholders)
        + '</div></div>'
    )


def card_page(heading, icon):
    accents = ''.join(
        f'<article class="card advanced-color-card bg-{color}"><div class="card-body"><span class="eyebrow">{label}</span><h3 class="mt-3">{title}</h3><p class="mb-0">{description}</p></div></article>'
        for color, label, title, description in [
            ('purple', 'PURPLE', 'Eksplorasi', 'Ruang untuk mencoba arah baru.'),
            ('green', 'GREEN', 'Kolaborasi', 'Ide tumbuh bersama tim.'),
            ('yellow', 'YELLOW', 'Momentum', 'Langkah kecil tetap berarti.'),
            ('orange', 'ORANGE', 'Peluncuran', 'Siap diperlihatkan ke dunia.'),
        ]
    )
    icon_card = f'''<div class="d-flex align-items-start gap-3">
      <span class="project-icon bg-purple">{icon('bolt')}</span>
      <div><h3>Ide minggu ini</h3><p class="mb-0">Gunakan satu kartu untuk menghubungkan ikon, judul, dan tindakan yang jelas.</p></div>
    </div><a class="btn btn-sm mt-4" href="projects.html">Lihat proyek ↗</a>'''
    stats = '''<div class="row g-3">
      <div class="col-sm-6"><div class="card stat-card bg-purple h-100"><div class="card-body"><span class="stat-label">Proyek aktif</span><div class="stat-value">24</div><span class="small">↗ 4 dari bulan lalu</span></div></div></div>
      <div class="col-sm-6"><div class="card stat-card bg-green h-100"><div class="card-body"><span class="stat-label">Kolaborator</span><div class="stat-value">12</div><span class="small">Tim kreatif demo</span></div></div></div>
    </div>'''
    overlay = '''<article class="card advanced-image-card">
      <img src="assets/img/workspace/studio.svg" alt="Ilustrasi geometris identitas Studio North" width="720" height="480">
      <div class="advanced-image-overlay"><span class="badge bg-yellow">FEATURED WORK</span><h3>Studio North</h3><p>Identitas digital yang berani tampil.</p><a href="portfolio.html" class="btn btn-sm btn-dark">Lihat portfolio ↗</a></div>
    </article>'''
    return (
        heading('Kartu untuk setiap cerita.', 'Variasi card Bootstrap dengan garis tegas dan bayangan solid.')
        + '<div class="row g-4"><div class="col-lg-6">'
        + '''<article class="card h-100"><div class="card-header"><h2 class="mb-0">Kartu dengan header</h2></div><div class="card-body"><p>Struktur sederhana untuk konten yang butuh konteks.</p><p class="mb-0 text-muted">Gunakan header dan footer hanya ketika membantu pembaca menemukan informasi.</p></div><div class="card-footer d-flex justify-content-between align-items-center"><span class="small">Diperbarui hari ini</span><a href="docs.html" class="fw-bold">Pelajari ↗</a></div></article>'''
        + '</div><div class="col-lg-6">'
        + panel('Kartu dengan ikon', 'Ikon SVG lokal selaras dengan konten.', icon_card, 'h-100')
        + '</div><div class="col-12">'
        + panel('Warna aksen', 'Empat token tema yang sudah tersedia.', f'<div class="advanced-color-grid">{accents}</div>')
        + '</div><div class="col-lg-7">'
        + panel('Stat card', 'Statistik dapat memakai kelas .stat-card yang sama seperti dashboard.', stats, 'h-100')
        + '</div><div class="col-lg-5">'
        + panel('Kartu bergambar', 'Ilustrasi SVG lokal dengan overlay yang tetap terbaca.', overlay, 'h-100')
        + '</div></div>'
    )


def modal_page(heading, icon):
    size_buttons = ''.join(
        f'<button type="button" class="btn" data-bs-toggle="modal" data-bs-target="#{key}">{label}</button>'
        for key, label in [
            ('modalSmall', 'Small'), ('modalDefault', 'Default'),
            ('modalLarge', 'Large'), ('modalExtraLarge', 'Extra large'),
            ('modalFull', 'Fullscreen'),
        ]
    )
    dialogs = ''.join(
        f'''<div class="modal fade" id="{key}" tabindex="-1" aria-labelledby="{key}Title" aria-hidden="true">
          <div class="modal-dialog {size}"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="{key}Title">{label}</h2><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><div class="modal-body"><p>Contoh modal ukuran {label.lower()} dengan fokus dan tombol Escape bawaan Bootstrap 5.</p></div><div class="modal-footer"><button type="button" class="btn btn-primary" data-bs-dismiss="modal">Selesai</button></div></div></div>
        </div>'''
        for key, label, size in [
            ('modalSmall', 'Small', 'modal-sm'),
            ('modalDefault', 'Default', ''),
            ('modalLarge', 'Large', 'modal-lg'),
            ('modalExtraLarge', 'Extra large', 'modal-xl'),
            ('modalFull', 'Fullscreen', 'modal-fullscreen'),
        ]
    )
    dialogs += '''
    <div class="modal fade" id="modalScrollable" tabindex="-1" aria-labelledby="modalScrollableTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-scrollable"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="modalScrollableTitle">Catatan panjang</h2><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><div class="modal-body">'''
    dialogs += ''.join(f'<p><strong>Bagian {number}.</strong> Ide yang baik perlu ruang untuk dijelaskan, diuji, lalu diperbaiki bersama tim.</p>' for number in range(1, 15))
    dialogs += '''</div><div class="modal-footer"><button type="button" class="btn" data-bs-dismiss="modal">Tutup</button></div></div></div></div>
    <div class="modal fade" id="modalCentered" tabindex="-1" aria-labelledby="modalCenteredTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="modalCenteredTitle">Di tengah layar</h2><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><div class="modal-body">Cocok untuk keputusan yang butuh perhatian singkat.</div><div class="modal-footer"><button type="button" class="btn btn-primary" data-bs-dismiss="modal">Mengerti</button></div></div></div></div>
    <div class="modal fade" id="modalForm" tabindex="-1" aria-labelledby="modalFormTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="modalFormTitle">Tambahkan ide</h2><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><form id="advancedModalForm"><div class="modal-body"><label for="modalIdea" class="form-label">Judul ide</label><input id="modalIdea" class="form-control" required maxlength="80" placeholder="Contoh: Eksplorasi warna baru"><p class="small text-muted mt-3 mb-0">Demo ini tidak menyimpan data ke server.</p></div><div class="modal-footer"><button type="button" class="btn" data-bs-dismiss="modal">Batal</button><button type="submit" class="btn btn-primary">Simpan demo</button></div></form></div></div></div>
    <div class="modal fade" id="modalDelete" tabindex="-1" aria-labelledby="modalDeleteTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="modalDeleteTitle">Hapus item contoh?</h2><button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><div class="modal-body">Item contoh akan hilang dari kartu ini sampai halaman dimuat ulang.</div><div class="modal-footer"><button type="button" class="btn" data-bs-dismiss="modal">Batal</button><button type="button" class="btn btn-danger" id="confirmModalDelete">Ya, hapus</button></div></div></div></div>'''
    return (
        heading('Ruang untuk keputusan.', 'Modal Bootstrap untuk informasi, formulir, dan konfirmasi.')
        + '<div class="row g-4"><div class="col-12">'
        + panel('Ukuran modal', 'Small, default, large, extra large, dan fullscreen.', f'<div class="d-flex flex-wrap gap-3">{size_buttons}</div>')
        + '</div><div class="col-lg-6">'
        + panel('Penempatan & scroll', 'Konten panjang tetap mudah dibaca.', '''<div class="d-flex flex-wrap gap-3"><button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalScrollable">Scrollable</button><button class="btn" data-bs-toggle="modal" data-bs-target="#modalCentered">Centered</button></div>''')
        + '</div><div class="col-lg-6">'
        + panel('Form di dalam modal', 'Validasi input sebelum modal ditutup.', '''<button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalForm">Buka form</button><p id="modalFormResult" class="small mt-3 mb-0" role="status">Belum ada ide disimpan.</p>''')
        + '</div><div class="col-12">'
        + panel('Konfirmasi penghapusan', 'Tindakan hanya mengubah item demo di halaman ini.', '''<div class="d-flex flex-wrap align-items-center gap-3"><strong id="deleteDemoItem">Konsep website studio</strong><button class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#modalDelete">Hapus item</button><span id="deleteModalResult" role="status"></span></div>''')
        + '</div></div>' + dialogs
    )


def sweet_alert_page(heading, icon):
    examples = [
        ('success', 'Berhasil', 'Operasi selesai dengan jelas.', 'green'),
        ('error', 'Error', 'Tunjukkan apa yang gagal.', 'orange'),
        ('warning', 'Peringatan', 'Minta perhatian sebelum lanjut.', 'yellow'),
        ('info', 'Informasi', 'Berikan konteks tambahan.', 'blue'),
        ('confirm', 'Konfirmasi', 'Pilihan ya atau batal.', 'purple'),
        ('custom', 'Konten kustom', 'Pesan dengan daftar sederhana.', 'green'),
        ('toast', 'Toast ringan', 'Umpan balik tanpa menghalangi.', 'yellow'),
    ]
    cards = ''.join(
        f'''<div class="col-md-6 col-xl-4"><section class="card h-100"><div class="card-body d-flex flex-column"><span class="badge bg-{color} align-self-start">{key.upper()}</span><h2 class="mt-3">{title}</h2><p class="text-muted">{description}</p><button type="button" class="btn btn-primary mt-auto" data-swal-demo="{key}">Lihat demo ↗</button></div></section></div>'''
        for key, title, description, color in examples
    )
    return heading('Pesan yang terasa jelas.', 'Dialog SweetAlert2 lokal untuk tujuh skenario umum.') + f'<div class="row g-4">{cards}</div><p id="sweetAlertResult" class="small text-muted mt-4" role="status">Pilih contoh untuk mencoba interaksinya.</p>'


def toastr_page(heading, icon):
    cards = ''.join(
        f'''<div class="col-sm-6 col-xl-3"><section class="card h-100"><div class="card-body"><span class="badge bg-{color}">{kind.upper()}</span><h2 class="mt-3">{title}</h2><p>{description}</p><button type="button" class="btn btn-primary" data-toastr-demo="{kind}">Tampilkan</button></div></section></div>'''
        for kind, color, title, description in [
            ('success', 'green', 'Success', 'Kabar baik yang tidak menghalangi kerja.'),
            ('info', 'blue', 'Info', 'Informasi singkat untuk konteks.'),
            ('warning', 'yellow', 'Warning', 'Perlu perhatian sebelum lanjut.'),
            ('error', 'orange', 'Error', 'Jelaskan kegagalan dengan jelas.'),
        ]
    )
    positions = ''.join(f'<option value="{value}">{label}</option>' for value, label in [
        ('toast-top-right', 'Kanan atas'), ('toast-top-left', 'Kiri atas'),
        ('toast-bottom-right', 'Kanan bawah'), ('toast-bottom-left', 'Kiri bawah'),
        ('toast-top-center', 'Tengah atas'), ('toast-bottom-center', 'Tengah bawah'),
    ])
    return (
        heading('Notifikasi tanpa ribet.', 'Empat jenis Toastr dengan posisi yang bisa diubah.')
        + f'<div class="row g-4">{cards}</div>'
        + panel('Pengaturan toast', 'Pilih posisi, lalu jalankan contoh di atas.', f'<div class="d-flex flex-wrap align-items-end gap-3"><div><label for="toastrPosition" class="form-label">Posisi</label><select id="toastrPosition" class="form-select">{positions}</select></div><button type="button" class="btn" id="toastrClear">Bersihkan semua toast</button></div>', 'mt-4')
    )


def empty_state_page(heading, icon):
    illustration = '''<svg class="empty-illustration" viewBox="0 0 260 170" aria-hidden="true"><rect x="40" y="42" width="155" height="104" rx="10" fill="#232420"/><rect x="30" y="32" width="155" height="104" rx="10" fill="#fffefb" stroke="#232420" stroke-width="4"/><path d="M30 65h155" stroke="#232420" stroke-width="4"/><circle cx="51" cy="49" r="4" fill="#c4a8f5"/><circle cx="65" cy="49" r="4" fill="#f9de6e"/><path d="m76 111 23-23 18 18 25-32" fill="none" stroke="#7952b3" stroke-width="5" stroke-linecap="round"/><path d="m183 20 5 15 15 5-15 5-5 15-5-15-15-5 15-5z" fill="#f9de6e" stroke="#232420" stroke-width="3"/></svg>'''
    return (
        heading('Kosong, tetap penuh arah.', 'Contoh empty state yang membantu pengguna mengambil langkah berikutnya.')
        + '<div class="row g-4"><div class="col-lg-7">'
        + panel('Mulai dari satu ide', 'Ilustrasi SVG lokal dan tindakan yang jelas.', f'<div class="advanced-empty text-center">{illustration}<h3>Belum ada proyek untuk ditampilkan.</h3><p class="text-muted">Setiap hal besar dimulai dari satu percobaan kecil.</p><a href="projects.html" class="btn btn-primary">Jelajahi proyek ↗</a></div>')
        + '</div><div class="col-lg-5">'
        + panel('Daftar kosong dalam card', 'Status daftar berubah saat contoh ditambahkan.', '''<div id="emptyDemo"><div class="advanced-empty compact"><span class="empty-symbol" aria-hidden="true">✳</span><h3>Daftar ide masih kosong.</h3><p class="text-muted">Tambahkan contoh untuk melihat keadaan berisi.</p></div></div><div class="d-flex flex-wrap gap-3 mt-4"><button type="button" class="btn btn-primary" id="emptyAdd">Tambahkan ide contoh</button><button type="button" class="btn" id="emptyReset" hidden>Kosongkan lagi</button></div>''', 'h-100')
        + '</div></div>'
    )


def multiple_upload_page(heading, icon):
    return (
        heading('File siap ditinjau.', 'Area Dropzone untuk melihat file dan progres pembacaan lokal.')
        + '<div class="row g-4"><div class="col-lg-8">'
        + panel('Tarik, lepas, atau pilih file', 'Maksimal 5 file gambar atau PDF, masing-masing 5 MB.', '''<div id="uploadDropzone" class="dropzone advanced-dropzone" aria-label="Area pilih file"><div class="dz-message"><span class="upload-symbol" aria-hidden="true">↥</span><strong>Letakkan file di sini</strong><span>atau klik untuk memilih dari perangkat</span></div></div><div class="d-flex align-items-center justify-content-between flex-wrap gap-3 mt-4"><p id="uploadSummary" class="small mb-0" role="status">Belum ada file dipilih.</p><button id="uploadClear" type="button" class="btn btn-sm" disabled>Hapus semua</button></div>''')
        + '</div><div class="col-lg-4">'
        + panel('Demo lokal', 'File hanya dibaca dalam browser.', '''<ul class="small ps-3 mb-4"><li>Gambar mendapat pratinjau thumbnail.</li><li>Setiap file punya indikator progres pembacaan.</li><li>File dapat dihapus satu per satu atau sekaligus.</li></ul><div class="alert alert-info mb-0 small">Tidak ada upload ke server. Tidak ada file yang disimpan setelah halaman ditutup.</div>''', 'h-100')
        + '</div></div>'
    )


def tab_group(group, labels, classes='nav-tabs', vertical=False, nav_last=False, show_icons=False, icon=None):
    buttons = ''.join(
        f'''<li class="nav-item" role="presentation"><button class="nav-link{' active' if index == 0 else ''}" id="{group}-tab-{index}" data-bs-toggle="tab" data-bs-target="#{group}-pane-{index}" type="button" role="tab" aria-controls="{group}-pane-{index}" aria-selected="{'true' if index == 0 else 'false'}">{icon('bolt') if show_icons and index == 0 else icon('users') if show_icons and index == 1 else ''}{label}</button></li>'''
        for index, label in enumerate(labels)
    )
    nav = f'<ul class="nav {classes}{" flex-column" if vertical else ""}" role="tablist" aria-label="Tab {group}" aria-orientation="{"vertical" if vertical else "horizontal"}">{buttons}</ul>'
    panes = ''.join(
        f'<div class="tab-pane fade{" show active" if index == 0 else ""}" id="{group}-pane-{index}" role="tabpanel" aria-labelledby="{group}-tab-{index}" tabindex="0"><h3>{label}</h3><p class="mb-0">Panel {label.lower()} dapat dibuka dengan klik atau tombol panah saat fokus berada pada tab.</p></div>'
        for index, label in enumerate(labels)
    )
    position = "right" if vertical and nav_last else "left" if vertical else "bottom" if nav_last else "top"
    content = f'<div class="tab-content advanced-tab-content tab-content--{position}">{panes}</div>'
    if vertical:
        return f'<div class="advanced-vertical-tabs{" reverse" if nav_last else ""}">{content + nav if nav_last else nav + content}</div>'
    return content + nav if nav_last else nav + content


def tabs_page(heading, icon):
    examples = [
        ('Basic atas', 'Pola default untuk konten berlapis.', tab_group('tabsTop', ['Ringkasan', 'Aktivitas', 'Catatan'])),
        ('Tab bawah', 'Navigasi berada setelah panel.', tab_group('tabsBottom', ['Info', 'Detail'], nav_last=True)),
        ('Tab kiri', 'Navigasi vertikal di kiri panel.', tab_group('tabsLeft', ['Proyek', 'Tim', 'File'], vertical=True)),
        ('Tab kanan', 'Navigasi vertikal di kanan panel.', tab_group('tabsRight', ['Desain', 'Riset'], vertical=True, nav_last=True)),
        ('Tab dengan ikon', 'SVG lokal membantu pengenalan cepat.', tab_group('tabsIcon', ['Inspirasi', 'Kolaborasi'], show_icons=True, icon=icon)),
        ('Pills', 'Alternatif ringkas tanpa garis tab.', tab_group('tabsPills', ['Hari ini', 'Minggu ini'], classes='nav-pills')),
        ('Justified', 'Tautan membagi ruang secara merata.', tab_group('tabsJustified', ['Semua', 'Berjalan', 'Selesai'], classes='nav-tabs nav-justified')),
    ]
    cards = ''.join(f'<div class="col-lg-6"><section class="card h-100"><div class="card-body"><div class="panel-heading"><div><h2>{title}</h2><p>{subtitle}</p></div></div>{content}</div></section></div>' for title, subtitle, content in examples)
    return heading('Konten yang punya tempat.', 'Variasi Bootstrap nav-tabs dan nav-pills dalam satu halaman.') + f'<div class="row g-4">{cards}</div>'


def build_advanced_pages(heading, icon):
    return {
        'avatar': avatar_page(heading, icon),
        'card': card_page(heading, icon),
        'modal': modal_page(heading, icon),
        'sweet-alert': sweet_alert_page(heading, icon),
        'toastr': toastr_page(heading, icon),
        'empty-state': empty_state_page(heading, icon),
        'multiple-upload': multiple_upload_page(heading, icon),
        'tabs': tabs_page(heading, icon),
    }
