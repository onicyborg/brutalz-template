"""Data-driven reference appendix for the in-browser documentation."""

from html import escape
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent.parent
PACKAGES = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))['devDependencies']


def all_pages(items, prefix=()):
    for item in items:
        if 'children' in item:
            yield from all_pages(item['children'], (*prefix, item['label']))
        else:
            yield item, prefix


def docs_appendix(nav):
    groups = []
    total = 0
    for section in nav:
        entries = list(all_pages(section['items']))
        total += len(entries)
        links = ''.join(
            '<li class="col-sm-6 col-xl-4 mb-2"><a href="' + escape(item['page'], quote=True) + '.html">'
            + escape(' › '.join((*parents, item['label']))) + '</a></li>'
            for item, parents in entries
        )
        groups.append('<section class="mb-4"><h3 class="fs-5">' + escape(section['group']) + '</h3>'
                      + '<ul class="row list-unstyled small mb-0">' + links + '</ul></section>')

    bundles = [
        ('SweetAlert2', 'sweetalert2', 'sweet-alert'),
        ('Toastr', 'toastr', 'toastr'),
        ('jQuery', 'jquery', 'toastr, Select2, Steps, DataTables, Sparkline, Morris, Owl'),
        ('Dropzone', 'dropzone', 'multiple-upload'),
        ('Select2', 'select2', 'Semua form-select, termasuk modal proyek'),
        ('Flatpickr', 'flatpickr', 'Tanggal/waktu di form dan modal'),
        ('Quill', 'quill', 'forms-editor, create-post'),
        ('jQuery Steps', 'jquery-steps', 'form-wizard'),
        ('DataTables Bootstrap 5', 'datatables.net-bs5', 'datatables, export-table'),
        ('DataTables Buttons', 'datatables.net-buttons-bs5', 'export-table'),
        ('JSZip', 'jszip', 'export-table'),
        ('pdfMake', 'pdfmake', 'export-table'),
        ('Chart.js', 'chart.js', 'chart-chartjs'),
        ('ApexCharts', 'apexcharts', 'chart-apexchart'),
        ('amCharts 4', '@amcharts/amcharts4', 'chart-amchart'),
        ('Apache ECharts', 'echarts', 'chart-echart'),
        ('jQuery Sparkline', 'jquery-sparkline', 'chart-sparkline'),
        ('Morris.js', 'morris.js', 'chart-morris'),
        ('Raphael', 'raphael', 'chart-morris'),
        ('Font Awesome Free', '@fortawesome/fontawesome-free', 'icon-font-awesome'),
        ('Material Icons', '@fontsource/material-icons', 'icon-material'),
        ('Ionicons', 'ionicons', 'icon-ionicons'),
        ('Feather Icons', 'feather-icons', 'icon-feather'),
        ('Weather Icons', 'weather-icons', 'icon-weather-icon'),
        ('GLightbox', 'glightbox', 'light-gallery'),
        ('Owl Carousel', 'owl.carousel', 'owl-carousel'),
        ('jsVectorMap', 'jsvectormap', 'vector-map'),
    ]
    aliases = {'morris.js': '0.5.1 (commit 14530d0)', 'weather-icons': '2.0.12'}
    rows = ''.join(
        '<tr><th scope="row">' + escape(name) + '</th><td><code>'
        + escape(aliases.get(package, PACKAGES[package])) + '</code></td><td>'
        + escape(usage) + '</td></tr>'
        for name, package, usage in bundles
    )
    return (
        '<section id="page-directory" class="card mt-4"><div class="card-body">'
        f'<h2>Direktori seluruh {total} halaman</h2><p class="small text-muted">Daftar ini dihasilkan dari konfigurasi sidebar yang sama dengan navigasi dan pencarian.</p>'
        + ''.join(groups) + '</div></section>'
        '<section id="library-directory" class="card mt-4"><div class="card-body"><h2>Library dan versi</h2>'
        '<p class="small">Bootstrap 5.3.8 adalah fondasi CSS/JavaScript. Bundle berikut disimpan lokal dan hanya dimuat pada halaman yang memerlukannya. '
        'Google Maps JavaScript API dimuat dari Google setelah key dimasukkan di browser; peta vektor tidak membutuhkan key. '
        'Rincian lisensi dan sumber ada di <code>assets/bundles/README.md</code>.</p>'
        '<div class="table-responsive"><table class="table"><thead><tr><th scope="col">Library</th><th scope="col">Versi</th><th scope="col">Contoh pemakaian</th></tr></thead><tbody>'
        + rows + '</tbody></table></div></div></section>'
        '<section id="enhanced-controls" class="card mt-4"><div class="card-body"><h2>Kontrol form dan tema komponen</h2>'
        '<p>Dropdown <code>.form-select</code> memakai Select2 lokal; kalender tanggal/waktu memakai Flatpickr dengan bahasa Indonesia. '
        'Keduanya mempertahankan field asli, nama, nilai, label, validasi, dan reset. Modal proyek tersedia di setiap halaman sehingga bundle kontrol dimuat bersama shell.</p>'
        '<ul class="small"><li>Style bersama berada di <code>assets/css/controls.css</code>, inisialisasi di <code>assets/js/controls.js</code>. '
        'Popup Select2 mengikuti lebar trigger; jangan menerapkan <code>width:100% !important</code> pada semua <code>.select2-container</code>.</li>'
        '<li>Select mendukung pencarian, multiple, optgroup, disabled, ukuran Bootstrap, serta field dinamis. '
        'Setelah mengubah nilai select lewat kode, kirim event <code>change</code> agar tampilan dan handler ikut diperbarui. '
        'Gunakan <code>change.select2</code> bila hanya menyinkronkan tampilan tanpa menjalankan logika form.</li>'
        '<li>Date memakai nilai <code>YYYY-MM-DD</code>, time <code>HH:MM</code>, datetime-local <code>YYYY-MM-DDTHH:MM</code>. '
        'Input dapat diketik langsung; rentang min/max dan validasi tanggal tetap diperiksa. '
        'Panah bawah membuka picker, panah menavigasi tanggal, Enter memilih, Escape menutup. Tombol Hari ini/Sekarang dan Bersihkan tersedia.</li>'
        '<li>Atribut <code>data-native</code> mempertahankan kontrol browser. Input readonly/disabled tidak membuka kalender. '
        'Jenis month/week belum dipakai pada halaman template dan tetap native bila ditambahkan; panel native mengikuti OS/browser sehingga tidak dapat diberi tema penuh.</li>'
        '<li>Tanpa JavaScript/plugin, markup select dan input tanggal asli tetap tersedia. '
        'Popup di modal dipasang di dalam modal agar fokus keyboard tetap terjaga.</li>'
        '<li>Tinggi progress memakai <code>--bs-progress-height</code>; warna memakai <code>background-color</code> agar pola garis tidak terhapus. '
        'Transisi menggunakan <code>--neo-transition</code> dan mengikuti <code>prefers-reduced-motion</code>.</li></ul>'
        '<p class="small mb-0">Referensi: <a href="https://select2.org/troubleshooting/common-problems">Select2 dalam modal</a> dan '
        '<a href="https://flatpickr.js.org/options/">opsi Flatpickr</a>.</p></div></section>'
        '<section id="contributing" class="card mt-4"><div class="card-body"><h2>Menambah halaman dengan rapi</h2>'
        '<ol class="small"><li>Gunakan nama file <code>lowercase-kebab-case.html</code> dan nilai <code>data-page</code> yang sama tanpa ekstensi.</li>'
        '<li>Tambahkan halaman ke <code>assets/js/sidebar-config.js</code>. Gunakan <code>id</code> unik untuk setiap dropdown; sidebar dan pencarian membaca konfigurasi ini.</li>'
        '<li>Tulis konten permanen di modul <code>scripts/*_pages.py</code> atau <code>scripts/build.py</code>. Generator akan menimpa HTML hasil build.</li>'
        '<li>Tempatkan style di <code>assets/css/</code>, interaksi di <code>assets/js/</code>, dan vendor berlisensi di <code>assets/bundles/</code>. Muat bundle hanya pada halaman terkait.</li>'
        '<li>Jalankan <code>npm run build</code> lalu <code>npm test</code>. Periksa desktop, mobile, keyboard, dan tautan sebelum commit.</li></ol>'
        '<p class="small mb-0">Template statis dapat dibuka langsung lewat <code>index.html</code> atau server <code>npm run dev</code>. '
        'Aset SVG asli tersimpan di <code>assets/img/</code>; sumber dan lisensi vendor dirinci di README proyek serta folder bundle.</p>'
        '</div></section>'
    )
