"""Phase 4 table showcases. HTML is formatted by the shared generator."""

from html import escape

TABLE_PAGES = ('basic-table', 'advance-table', 'datatables', 'export-table', 'editable-table')

RECORDS = [
    ('PRJ-101', 'Studio website', 'Website', 'Berjalan', '4800000', '2026-10-12'),
    ('PRJ-102', 'Acme identity', 'Branding', 'Review', '3600000', '2026-10-18'),
    ('PRJ-103', 'Finance mobile', 'Mobile app', 'Berjalan', '7800000', '2026-10-22'),
    ('PRJ-104', 'Summer campaign', 'Marketing', 'Selesai', '2400000', '2026-09-30'),
    ('PRJ-105', 'Coffee landing', 'Website', 'Rencana', '1850000', '2026-11-03'),
    ('PRJ-106', 'Creative portfolio', 'Website', 'Rencana', '2200000', '2026-11-08'),
    ('PRJ-107', 'Social kit', 'Marketing', 'Selesai', '1600000', '2026-09-28'),
    ('PRJ-108', 'Motion system', 'Branding', 'Review', '4200000', '2026-10-25'),
    ('PRJ-109', 'Event microsite', 'Website', 'Berjalan', '2950000', '2026-11-12'),
    ('PRJ-110', 'Product dashboard', 'Mobile app', 'Rencana', '5300000', '2026-12-01'),
    ('PRJ-111', 'Launch newsletter', 'Marketing', 'Review', '1250000', '2026-10-06'),
    ('PRJ-112', 'Studio refresh', 'Branding', 'Selesai', '3450000', '2026-09-25'),
]


def static_rows():
    colors = {'Berjalan': 'purple', 'Review': 'orange', 'Selesai': 'green', 'Rencana': 'blue'}
    return ''.join(
        f'<tr><td class="text-nowrap fw-bold">{escape(code)}</td>'
        f'<td>{escape(name)}</td><td>{escape(category)}</td>'
        f'<td><span class="badge bg-{colors[status]}">{escape(status)}</span></td>'
        f'<td data-order="{budget}" class="text-nowrap">Rp{int(budget):,}</td>'
        f'<td data-order="{due}" class="text-nowrap">{escape(due)}</td></tr>'
        for code, name, category, status, budget, due in RECORDS
    )


def editable_rows():
    return ''.join(
        f'<tr data-record="{escape(code)}"><td class="fw-bold">{escape(code)}</td>'
        f'<td><button type="button" class="editable-cell" data-field="name" aria-label="Edit nama {escape(name)}">{escape(name)}</button></td>'
        f'<td><button type="button" class="editable-cell" data-field="category" aria-label="Edit kategori {escape(name)}">{escape(category)}</button></td>'
        f'<td><button type="button" class="editable-cell" data-field="budget" data-value="{budget}" aria-label="Edit anggaran {escape(name)}">Rp{int(budget):,}</button></td>'
        f'<td class="text-nowrap">{escape(due)}</td></tr>'
        for code, name, category, _status, budget, due in RECORDS[:6]
    )


def build_table_pages(heading, projects_table, new_project_button):
    overview_items = [
        ('basic-table', 'Tabel dasar', 'Daftar proyek workspace: cari, filter, urutkan, pagination, dan CSV.', 'bg-yellow'),
        ('advance-table', 'Advanced table', 'Variasi striped, hover, bordered, dan sorting langsung.', 'bg-purple'),
        ('datatables', 'DataTables', 'Pencarian, urut multi-kolom, pagination, serta jumlah data.', 'bg-green'),
        ('export-table', 'Export table', 'Unduh XLSX, CSV, PDF, atau buka tampilan cetak.', 'bg-orange'),
        ('editable-table', 'Editable table', 'Klik sel, ubah nilainya, lalu simpan di browser.', 'bg-blue'),
    ]
    overview = heading('Data yang mudah dibaca.', 'Pilih pola tabel sesuai kebutuhan: sederhana, interaktif, ekspor, atau edit langsung.')
    overview += '<div class="row g-4">' + ''.join(
        f'<div class="col-md-6 col-xl-4"><a class="card table-index-card h-100 text-decoration-none text-dark" href="{slug}.html"><div class="card-body"><span class="badge {color} mb-3">{title}</span><h2 class="fs-4">{title} →</h2><p class="text-muted mb-0">{description}</p></div></a></div>'
        for slug, title, description, color in overview_items
    ) + '</div>'

    advanced = heading('Tabel dengan karakter.', 'Tiga variasi Bootstrap dan sorting lokal yang responsif.')
    advanced += '''<div class="row g-4"><div class="col-12"><section class="card"><div class="card-body"><div class="d-flex flex-wrap justify-content-between align-items-center gap-2"><div><h2 class="mb-1">Proyek menurut anggaran</h2><p class="small text-muted mb-0">Klik judul kolom untuk urutkan secara naik atau turun.</p></div><span class="badge bg-yellow">SORTING LOKAL</span></div></div><div class="table-responsive"><table class="table table-hover table-striped table-bordered table-showcase" id="advancedTable"><caption class="visually-hidden">Proyek contoh yang dapat diurutkan</caption><thead><tr><th scope="col"><button type="button" data-sort="text">Kode</button></th><th scope="col"><button type="button" data-sort="text">Proyek</button></th><th scope="col"><button type="button" data-sort="text">Kategori</button></th><th scope="col"><button type="button" data-sort="text">Status</button></th><th scope="col"><button type="button" data-sort="number">Anggaran</button></th><th scope="col"><button type="button" data-sort="date">Tenggat</button></th></tr></thead><tbody>''' + static_rows() + '''</tbody></table></div><div class="card-footer small" id="advancedSortStatus" role="status">Urutan awal sesuai kode proyek.</div></section></div><div class="col-lg-6"><section class="card h-100"><div class="card-body"><h2>Striped & hover</h2><p class="small text-muted">Baris berselang-seling dan sorot saat penunjuk berada di atasnya.</p><div class="table-responsive"><table class="table table-striped table-hover"><thead><tr><th scope="col">Tim</th><th scope="col">Tugas</th><th scope="col">Status</th></tr></thead><tbody><tr><td>Desain</td><td>Wireframe</td><td><span class="badge bg-purple">Berjalan</span></td></tr><tr><td>Produk</td><td>Riset</td><td><span class="badge bg-green">Selesai</span></td></tr><tr><td>Konten</td><td>Copywriting</td><td><span class="badge bg-orange">Review</span></td></tr></tbody></table></div></div></section></div><div class="col-lg-6"><section class="card h-100"><div class="card-body"><h2>Bordered</h2><p class="small text-muted">Garis tegas pada setiap sel untuk membedakan angka dengan cepat.</p><div class="table-responsive"><table class="table table-bordered"><thead><tr><th scope="col">Kanal</th><th scope="col">Kunjungan</th><th scope="col">Konversi</th></tr></thead><tbody><tr><td>Organik</td><td>1.280</td><td>5,2%</td></tr><tr><td>Sosial</td><td>920</td><td>4,1%</td></tr><tr><td>Referral</td><td>410</td><td>3,8%</td></tr></tbody></table></div></div></section></div></div>'''

    datatables = heading('Temukan data dalam sekejap.', 'DataTables mengatur pencarian, pagination, dan urutan multi-kolom di browser.')
    datatables += '''<section class="card"><div class="card-body"><h2>Direktori proyek</h2><p class="small text-muted">Ketik di kotak pencarian. Tahan Shift saat mengeklik judul kolom lain untuk urut multi-kolom.</p><div class="table-responsive"><table id="dataTableDemo" class="table table-striped table-hover table-showcase"><caption class="visually-hidden">Direktori proyek contoh</caption><thead><tr><th scope="col">Kode</th><th scope="col">Proyek</th><th scope="col">Kategori</th><th scope="col">Status</th><th scope="col">Anggaran</th><th scope="col">Tenggat</th></tr></thead><tbody>''' + static_rows() + '''</tbody></table></div></div></section>'''

    export = heading('Bawa datanya ke mana saja.', 'Ekspor dataset contoh langsung dari browser dengan DataTables Buttons.')
    export += '''<section class="card"><div class="card-body"><h2>Laporan proyek contoh</h2><p class="small text-muted">Filter atau urutkan tabel terlebih dahulu; tombol ekspor mengikuti baris yang terlihat pada hasil pencarian. Data hanya contoh.</p><div class="table-responsive"><table id="exportTableDemo" class="table table-striped table-hover table-showcase"><caption class="visually-hidden">Laporan proyek yang dapat diekspor</caption><thead><tr><th scope="col">Kode</th><th scope="col">Proyek</th><th scope="col">Kategori</th><th scope="col">Status</th><th scope="col">Anggaran</th><th scope="col">Tenggat</th></tr></thead><tbody>''' + static_rows() + '''</tbody></table></div><p id="exportStatus" class="small mt-3 mb-0" role="status"></p></div></section>'''

    editable = heading('Ubah data tanpa pindah halaman.', 'Klik nama, kategori, atau anggaran untuk membuka editor sel.')
    editable += '''<div class="row g-4"><div class="col-xl-9"><section class="card"><div class="card-body"><div class="d-flex justify-content-between flex-wrap gap-2"><div><h2>Anggaran proyek</h2><p class="small text-muted mb-3">Perubahan demo tersimpan di browser ini. Tekan Enter untuk simpan atau Escape untuk batal.</p></div><button class="btn btn-sm align-self-start" id="editableReset" type="button">Pulihkan contoh</button></div><div class="table-responsive"><table id="editableTable" class="table table-hover table-showcase"><caption class="visually-hidden">Data proyek dengan sel yang dapat diedit</caption><thead><tr><th scope="col">Kode</th><th scope="col">Proyek</th><th scope="col">Kategori</th><th scope="col">Anggaran</th><th scope="col">Tenggat</th></tr></thead><tbody>''' + editable_rows() + '''</tbody></table></div><p id="editableStatus" class="small mt-3 mb-0" role="status"></p></div></section></div><div class="col-xl-3"><div class="alert alert-info small">Editor hanya mengubah dataset demo di halaman ini. Proyek workspace asli tetap terpisah.</div></div></div>'''

    return {
        'tables': overview,
        'basic-table': heading('Data rapi. Keputusan tepat.', 'Cari, filter, dan ekspor proyek dari workspace demo.', new_project_button()) + projects_table(True),
        'advance-table': advanced,
        'datatables': datatables,
        'export-table': export,
        'editable-table': editable,
    }
