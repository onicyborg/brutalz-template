"""Complete usage guide. This is the source of docs.html; edit here, then build."""

from html import escape
from docs_page import docs_appendix


def code(value):
    return '<pre class="docs-code"><code>' + escape(value.strip('\n')) + '</code></pre>'


def section(key, title, body):
    return f'<section id="{key}" class="card docs-section"><div class="card-body"><h2>{title}</h2>{body}</div></section>'


def documentation(heading, nav):
    sections = []

    def add(key, title, body):
        sections.append((key, title, section(key, title, body)))

    add('overview', '1. Mengenal BRUTAL.', '''
    <p>BRUTAL. adalah template admin HTML statis berbahasa Indonesia dengan Bootstrap 5.3.8 dan tema Neubrutalism: garis hitam, warna pastel, serta bayangan solid. Semua halaman hasil build dan bundle browser tersedia di repository. Preview tidak membutuhkan instalasi npm atau kompilasi Sass.</p>
    <p>Template mencakup workspace, komponen UI, form, tabel, grafik, enam koleksi ikon, media, peta, autentikasi demo, dan halaman utilitas. Gunakan direktori halaman di bagian bawah untuk menemukan contoh yang dibutuhkan.</p>
    <div class="alert alert-info mb-0">Interaksi akun, chat, email, unggahan, kontak, dan publikasi adalah demo frontend. Template tidak menyediakan backend, database, sesi login, atau pengiriman pesan nyata. Google Maps adalah integrasi eksternal opsional.</div>''')

    add('setup', '2. Clone dan jalankan di lokal', '''
    <p>Siapkan Git dan Python 3.10 atau lebih baru. Node.js 22+ dengan npm diperlukan jika memakai perintah npm, memperbarui paket vendor, atau menjalankan suite Playwright; keduanya tidak diperlukan untuk preview lewat Python langsung.</p>
    <h3>Preview paling sederhana</h3>'''
        + code('''git clone https://github.com/onicyborg/brutalz-template.git
cd brutalz-template
python3 -m http.server 4173 --bind 127.0.0.1''') + '''
    <p>Buka <a href="http://127.0.0.1:4173/">http://127.0.0.1:4173/</a> untuk dashboard atau <a href="http://127.0.0.1:4173/docs.html">/docs.html</a> untuk panduan ini. Hentikan server dengan Ctrl+C. Pada Windows, gunakan <code>py -m http.server 4173 --bind 127.0.0.1</code> bila perintah <code>python3</code> tidak tersedia.</p>
    <h3>Perintah npm</h3>'''
        + code('''npm run dev
# Menjalankan server Python yang sama; npm ci tidak diperlukan untuk preview.''') + '''
    <p><code>npm run dev</code> menggunakan perintah <code>python3</code>. Jika nama executable Python di sistemmu berbeda, pakai perintah Python langsung di atas.</p>
    <p class="mb-0">Membuka <code>index.html</code> lewat <code>file://</code> cukup untuk sebagian besar demo, tetapi HTTP lokal dianjurkan agar origin penyimpanan konsisten, clipboard bekerja, dan snippet yang memuat JSON dapat digunakan. <code>localhost</code> dan <code>127.0.0.1</code> memiliki penyimpanan browser yang berbeda.</p>''')

    add('build', '3. Setup pengembangan dan build HTML', '''
    <p>HTML dibuat oleh generator Python dengan lxml. Buat virtual environment supaya dependensi build terpisah dari Python sistem. Jalankan perintah dari root repository.</p>
    <h3>Linux / macOS</h3>'''
        + code('''python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-build.txt
python scripts/build.py''') + '''
    <h3>Windows PowerShell</h3>'''
        + code(r'''py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-build.txt
.\.venv\Scripts\python.exe scripts/build.py''') + '''
    <p>Alternatif di environment yang menyediakan <code>python3</code>: <code>npm run build</code>. Tidak ada watcher otomatis: jalankan build setiap kali generator berubah, lalu refresh browser. Perubahan CSS/JS cukup diikuti refresh.</p>
    <h3>Dependensi development JavaScript</h3>'''
        + code('''npm ci
# Menginstal versi persis dari package-lock.json.
# Hanya diperlukan untuk pengujian browser atau pekerjaan vendor.''') + '''
    <p>Build menghasilkan 93 halaman dengan indentasi dan pemeriksaan bahwa format tidak mengubah makna HTML. Generator juga memperbarui aset demo seperti ikon sidebar, Feather, data animasi, flag, dan ilustrasi workspace.</p>
    <div class="alert alert-warning mb-0">Edit konten permanen di <code>scripts/</code>. Perubahan langsung pada HTML yang dikelola generator akan tertimpa saat build berikutnya. Build tidak menyalin ulang bundle dari <code>node_modules</code> dan tidak mengompilasi Bootstrap.</div>''')

    add('structure', '4. Struktur dan sumber perubahan', code('''*.html                        Halaman siap dibuka / deploy
assets/css/theme.css          Token tema, shell, override Bootstrap
assets/css/controls.css       Select2 dan Flatpickr bersama
assets/css/docs.css           Tampilan dokumentasi ini
assets/css/*.css              Style khusus modul
assets/js/sidebar-config.js   Konfigurasi sidebar dan pencarian
assets/js/sidebar.js          Renderer sidebar dan drawer
assets/js/app.js              Workspace, proyek, kalender, profil
assets/js/controls.js         Peningkatan select dan input tanggal
assets/js/kanban.js           Drag/drop pointer, sentuh, keyboard
assets/js/*.js                Interaksi modul lainnya
assets/bundles/               Distribusi vendor dan lisensi
assets/img/                   Ilustrasi, flags, favicon SVG
assets/files/                 Contoh lampiran lokal
bootstrap-5.3.8/              CSS/JS Bootstrap, source map, lisensi
scripts/build.py              Shell, pemetaan halaman, pipeline build
scripts/*_pages.py            Konten masing-masing kelompok halaman
scripts/documentation_page.py Sumber panduan ini
scripts/docs_page.py          Direktori halaman dan daftar library
scripts/format_html.py        Formatter HTML dan pemeriksaan semantik
tests/                       Suite pengujian development
requirements-build.txt        Dependensi build Python
package.json / package-lock.json Dependensi dan perintah npm''') + '''
    <p class="mb-0"><code>PHASE-PLAN.md</code> dan <code>SIDEBAR-CHECKLIST.md</code> menyimpan riwayat cakupan/pengembangan. Keduanya tidak diperlukan di hosting. Folder <code>node_modules</code>, <code>.venv</code>, cache, screenshot referensi, dan laporan tes tidak masuk Git.</p>''')

    add('theme', '5. Mengubah tema dan identitas', '''
    <p>Token ada di bagian awal <code>assets/css/theme.css</code>. Ubah lapisan tema ini; file vendor Bootstrap tetap asli. Warna utility <code>bg-purple</code>, <code>bg-yellow</code>, <code>bg-green</code>, <code>bg-orange</code>, dan <code>bg-blue</code> tersedia untuk kartu, badge, serta panel.</p>'''
        + code(''':root {
  --neo-ink: #232420;
  --neo-paper: #f5f4ef;
  --neo-surface: #fffefb;
  --neo-purple: #c4a8f5;
  --neo-yellow: #f9de6e;
  --neo-border: 2px solid var(--neo-ink);
  --neo-shadow: 4px 4px 0 var(--neo-ink);
}''') + '''
    <p>Untuk tombol Bootstrap, perhatikan variabel komponen <code>--bs-btn-*</code> di aturan <code>.btn</code> dan variannya. Mengubah <code>--bs-primary</code> saja tidak otomatis mengganti semua warna tombol yang sudah ditentukan oleh CSS.</p>
    <p>Identitas BRUTAL., topbar, footer, judul dokumen, dan modal bersama dibuat oleh <code>scripts/build.py</code>. Ikon identitas berada di <code>assets/img/favicon.svg</code>. Struktur sidebar dibangun di <code>assets/js/sidebar.js</code>; cari teks brand di kedua sumber saat menggantinya.</p>
    <p class="mb-0">Gunakan grid Bootstrap <code>.row</code>, <code>.col-md-*</code>, dan utility spacing. Jaga focus ring, label, kontras, serta dukungan <code>prefers-reduced-motion</code>. Progress berwarna harus memakai <code>background-color</code> agar pola striped tetap tampil.</p>''')

    add('navigation', '6. Sidebar, pencarian, dan halaman baru', '''
    <p><code>assets/js/sidebar-config.js</code> adalah sumber navigasi dan pencarian halaman. Nilai <code>page</code> sama dengan nama file tanpa ekstensi. Dropdown memakai <code>id</code> unik dan array <code>children</code>; menu bertingkat memakai bentuk yang sama.</p>'''
        + code('''{"id":"reportsMenu","label":"Laporan","icon":"chart","children":[
  {"page":"sales-report","label":"Laporan penjualan"}
]}''') + '''
    <p>Simpan array konfigurasi sebagai JSON valid karena generator juga membacanya: gunakan kutip ganda dan hindari trailing comma. Nama ikon dropdown harus tersedia di kamus <code>ICONS</code> pada <code>scripts/build.py</code>.</p>
    <ol><li>Tambahkan entri <code>sales-report</code> pada grup navigasi yang sesuai.</li>
    <li>Buat fungsi konten di modul Python atau tambahkan pemetaan di <code>main()</code> pada <code>scripts/build.py</code>, misalnya contoh di bawah.</li>
    <li>Tambahkan style/JavaScript khusus bila diperlukan dan muat bersyarat berdasarkan key halaman di fungsi <code>page()</code>.</li>
    <li>Jalankan build. Generator mengisi title, <code>data-page</code>, shell, dan direktori dokumentasi.</li></ol>'''
        + code('''# Tambahkan ke dictionary pages di main() sebelum loop write_page.
'sales-report': heading('Laporan penjualan', 'Ringkasan periode ini.')
    + card('Pendapatan', '<p>Isi laporan di sini.</p>'),''') + '''
    <p class="mb-0">Untuk prototipe manual, salin <code>blank.html</code> dengan nama baru lalu ubah title, <code>body[data-page]</code>, dan kontennya. Daftarkan di sidebar agar dapat dicari. Generator tidak memperbarui salinan manual tersebut; pindahkan kontennya ke generator bila ingin shell tetap konsisten.</p>''')

    add('components', '7. Urutan aset dan penggunaan komponen', '''
    <p>Halaman generated menjadi referensi urutan aset lengkap. Secara umum: CSS vendor → CSS kontrol bersama → tema → CSS modul. JavaScript Bootstrap dan shell dimuat lebih dulu, lalu vendor lokal, inisialisasi modul, dan kontrol bersama. Jangan memuat jQuery atau Bootstrap dua kali.</p>'''
        + code('''<link rel="stylesheet" href="bootstrap-5.3.8/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="assets/css/theme.css">

<button type="button" class="btn btn-primary">Simpan perubahan</button>
<div class="card mt-4">
  <div class="card-body">
    <span class="badge bg-green">Aktif</span>
    <h2 class="mt-3">Judul panel</h2>
    <p class="mb-0">Konten panel.</p>
  </div>
</div>

<script src="bootstrap-5.3.8/dist/js/bootstrap.bundle.min.js"></script>''') + '''
    <p>Contoh minimal di atas hanya menunjukkan Bootstrap dan tema. Untuk shell, modal, tooltip, popover, atau kontrol form lengkap, mulai dari halaman generated dan pertahankan dependency yang digunakannya.</p>
    <p class="mb-0">Salin markup komponen dari halaman demonya. Ganti ID agar unik, lalu sesuaikan <code>for</code>, <code>aria-controls</code>, <code>aria-labelledby</code>, dan <code>data-bs-target</code> yang merujuknya. Gunakan tombol untuk aksi dan tautan untuk navigasi.</p>''')

    add('forms-guide', '8. Form, editor, dan validasi', '''
    <p>Semua <code>.form-select</code> ditingkatkan menjadi Select2 oleh <code>assets/js/controls.js</code>; input date/time/datetime-local memakai Flatpickr. Markup native, atribut <code>name</code>, label, required, min/max, serta reset tetap menjadi sumber nilai.</p>'''
        + code('''<label for="projectStatus" class="form-label">Status</label>
<select id="projectStatus" name="status" class="form-select" required>
  <option value="Rencana">Rencana</option>
  <option value="Berjalan">Berjalan</option>
</select>
<label for="dueDate" class="form-label mt-3">Tenggat</label>
<input id="dueDate" name="due" type="date" class="form-control" required>''') + code('''const field = document.querySelector('#projectStatus');
field.value = 'Berjalan';
field.dispatchEvent(new Event('change', { bubbles: true }));''') + '''
    <p>Tambahkan <code>data-native</code> untuk mempertahankan kontrol browser. Untuk mengganti tanggal setelah picker terpasang, gunakan <code>field._flatpickr.setDate('2026-10-05', true)</code>. Detail kontrol dan keyboard tersedia pada bagian Kontrol form di bawah.</p>
    <p>Validasi demo memakai constraint HTML dan kelas Bootstrap. Saat menghubungkan backend, gunakan <code>form.checkValidity()</code>, tangani respons error per field, dan validasi ulang di server. Quill tersedia pada Editor dan Create Post; ambil Delta atau HTML sesuai kebutuhan API, dan sanitasi konten yang akan dirender. Wizard memvalidasi langkah sebelum pindah.</p>
    <p class="mb-0">Dropzone hanya menampilkan antrean/pratinjau lokal. Mengaktifkan upload memerlukan endpoint server dan handler keberhasilan/kegagalan. Jangan menganggap file preview sudah tersimpan permanen.</p>''')

    add('workspace-guide', '9. Proyek canvas dan workspace', '''
    <p><a href="projects.html">Projects</a> memiliki kolom Rencana, Berjalan, Review, dan Selesai. Tambah proyek lewat modal, ubah status melalui dropdown, atau seret kartu ke kolom tujuan. Posisi di dalam kolom juga dapat diurutkan atas/bawah.</p>
    <ul><li>Mouse: seret area kartu. Kontrol dropdown tetap dapat diklik secara normal.</li><li>Sentuh: geser canvas untuk scroll; tekan-tahan kartu untuk mulai drag.</li><li>Keyboard: fokuskan kartu, Enter/Space untuk mengambil, panah kiri/kanan mengganti kolom, atas/bawah mengatur urutan, Enter/Space untuk meletakkan, Escape untuk membatalkan.</li></ul>
    <p>Status dan <code>boardOrder</code> disimpan bersama proyek. <code>assets/js/kanban.js</code> menangani interaksi drag dan event <code>kanban:move</code>; <code>assets/js/app.js</code> mengubah data lalu merender ulang. Jika mengganti renderer, tutup Select2 sebelum membuang field agar listener scroll dibersihkan.</p>
    <p class="mb-0">Kalender menyimpan agenda lokal. Chat dan mailbox menyimulasikan percakapan, draft, balas, serta kirim di browser. Blog dan portfolio memakai data contoh/filter; Create Post dan Posts menyediakan draft/publikasi lokal. Statistik dashboard dan chart adalah ilustrasi, bukan agregasi otomatis proyek.</p>''')

    add('tables-charts', '10. Tabel, ekspor, dan grafik', '''
    <p><a href="basic-table.html">Tabel Dasar</a> terhubung ke proyek workspace dan menyediakan pencarian, filter, pengurutan, pagination, serta CSV. <a href="datatables.html">DataTables</a> memakai data demo sendiri dengan default 10 baris agar cocok dengan pilihan jumlah entri.</p>'''
        + code('''// assets/js/tables.js — konfigurasi DataTables
new DataTable('#dataTableDemo', {
  pageLength: 10,
  order: [[0, 'asc']],
  layout: {
    topStart: 'pageLength', topEnd: 'search',
    bottomStart: 'info', bottomEnd: 'paging'
  }
});''') + '''
    <p>Jangan inisialisasi tabel yang sama dua kali. Ketika memuat data API, gunakan API instance DataTables untuk mengubah baris. Export Table memuat Buttons, JSZip, dan pdfMake untuk Excel, CSV, PDF, serta cetak; Editable Table menyimpan edit pada key terpisah.</p>
    <p>Chart.js, ApexCharts, amCharts 4, ECharts, Sparkline, dan Morris diinisialisasi dalam <code>assets/js/charts.js</code>. Masing-masing halaman memuat vendor yang diperlukan. Ganti dataset dan label pada blok halaman yang sesuai; hancurkan instance lama jika membuat ulang chart pada elemen yang sama.</p>
    <p class="mb-0">Ukuran tombol pagination diatur terpusat melalui <code>--neo-page-size</code> dan <code>--neo-page-icon-size</code> di <code>theme.css</code>. Gunakan <code>.pagination-sm</code> atau <code>.pagination-lg</code> agar panah dan nomor tetap seukuran.</p>''')

    add('icons-media', '11. Ikon, animasi, dan media', '''
    <p>Menu Icons berisi Font Awesome, Material Icons, Ionicons, Feather, Weather Icons, dan Animated Icons. Galeri mendukung pencarian serta salin kode. Feather menyalin SVG lengkap; koleksi font membutuhkan CSS dan font bundle terkait.</p>
    <p><a href="icon-animated.html">Animated Icons</a> memakai Lordicon lokal dengan enam aset animasi internal. Pilih hover/fokus, klik/sentuh, otomatis berulang, atau pemicu JavaScript. Kontrol kecepatan mengubah snippet, dan jeda global menghentikan animasi demo. Animasi di luar viewport/tab tersembunyi dihentikan, serta reduced motion dihormati.</p>'''
        + code('''<script src="assets/bundles/lordicon/lordicon.js"></script>
<button type="button" class="download-action" aria-label="Unduh">
  <lord-icon src="assets/bundles/lordicon/icons/download.json"
    trigger="hover" target=".download-action" state="hover-pinch"
    colors="primary:#232420,secondary:#a78bfa"
    style="width:80px;height:80px" aria-hidden="true"></lord-icon>
</button>''') + '''
    <p>Player cukup dimuat satu kali. Untuk event aplikasi, panggil <code>icon.play({ from: 'start' })</code>. Snippet memuat JSON melalui HTTP; galeri bawaan memakai data embedded hasil build agar juga mendukung <code>file://</code>. Tambahkan aset baru ke <code>scripts/animated_icon_pages.py</code> dan simpan sumber/lisensinya di bundle.</p>
    <p class="mb-0">Media memakai GLightbox, Bootstrap Carousel, Owl Carousel, dan ilustrasi SVG lokal. Ganti gambar dengan aset milikmu, pertahankan alt text, ukuran/aspect ratio, serta label navigasi. Kredit dan lisensi tiap library tersedia pada daftar bundle; atribusi Lordicon dan branding amCharts tetap dipertahankan.</p>''')

    add('maps-guide', '12. Google Maps dan peta vektor', '''
    <p>Delapan halaman <code>gmaps-*.html</code> menampilkan panel koneksi. Masukkan key browser milikmu pada panel tersebut; kode template tidak memuat key tetap. Pengaturan key dan pesan kegagalan ditangani oleh <code>assets/js/maps.js</code>.</p>
    <p>Siapkan proyek Google Cloud dengan billing dan layanan untuk fitur yang digunakan: Maps JavaScript API, Routes API untuk demo rute, serta Geocoding API untuk pencarian alamat. Batasi key ke origin/domain dan API yang digunakan. Tanpa key, template tetap menampilkan placeholder.</p>
    <p>Key tersimpan di <code>brutal.mapsApiKey</code>. Gunakan tombol hapus key di halaman Maps untuk menghapusnya. Geolocation memerlukan izin browser dan secure context seperti HTTPS atau localhost. Advanced Route memisahkan mode waypoint dan alternatif rute.</p>
    <p class="mb-0"><a href="vector-map.html">Vector Map</a> menggunakan jsVectorMap dan data dunia lokal; tidak memerlukan key maupun koneksi Google. Error peta tidak memengaruhi modul lain.</p>''')

    add('storage', '13. Data lokal dan reset demo', '''
    <p>Data demo disimpan di localStorage, berbeda untuk setiap origin dan profil browser. Browser privat, kuota penuh, atau storage yang diblokir dapat membuat data tidak bertahan. Refresh tidak menghapus data yang telah disimpan.</p>
    <div class="table-responsive"><table class="table"><thead><tr><th>Key</th><th>Isi / reset</th></tr></thead><tbody>
    <tr><td><code>brutal.projects</code>, <code>brutal.tasks</code>, <code>brutal.events</code></td><td>Proyek, checklist, agenda; reset dari Profil.</td></tr>
    <tr><td><code>brutal.profile</code>, <code>brutal.compact</code></td><td>Profil dan preferensi tampilan; reset dari Profil.</td></tr>
    <tr><td><code>brutal.chat</code>, <code>brutal.mail</code></td><td>Percakapan dan mailbox; reset dari Profil.</td></tr>
    <tr><td><code>brutal.editableTable</code></td><td>Edit tabel; gunakan reset di Editable Table.</td></tr>
    <tr><td><code>brutal.posts</code>, <code>brutal.subscribers</code></td><td>Post dan pendaftaran demo; hapus key terkait lewat DevTools untuk reset.</td></tr>
    <tr><td><code>brutal.mapsApiKey</code></td><td>Key Maps; hapus melalui panel Maps.</td></tr>
    </tbody></table></div>
    <p class="mb-0">Tombol reset di Profil tidak menghapus semua key template. Sebelum reset, simpan data yang masih dibutuhkan. Untuk reset spesifik di DevTools → Application/Storage → Local Storage, hapus key yang bersangkutan, lalu refresh. Jangan memakai <code>localStorage.clear()</code> jika origin dipakai aplikasi lain.</p>''')

    add('backend', '14. Menghubungkan backend', '''
    <p>Ganti sumber data dan handler demo pada modul terkait: <code>app.js</code> untuk workspace, <code>workspace.js</code> untuk chat/email, <code>special.js</code> untuk post/subscribe/kontak, <code>tables.js</code> untuk tabel. Pisahkan layanan API dari renderer agar komponen dapat dipakai ulang.</p>'''
        + code('''// Contoh pola integrasi, bukan endpoint yang disediakan template.
async function loadProjects() {
  const response = await fetch('/api/projects', {
    credentials: 'same-origin',
    headers: { Accept: 'application/json' }
  });
  if (!response.ok) throw new Error('Proyek belum dapat dimuat.');
  return response.json();
}''') + '''
    <p class="mb-0">Tentukan kontrak data, state loading/empty/error, dan cara retry. Simpan perubahan hanya setelah respons berhasil atau sediakan rollback untuk pembaruan optimistis. Server harus menangani autentikasi, otorisasi, validasi, sanitasi konten, dan penyimpanan permanen. Login demo saat ini tidak melindungi halaman.</p>''')

    add('deployment', '15. Deploy dan pemeliharaan', '''
    <p>Untuk hosting statis, salin seluruh file <code>*.html</code>, folder <code>assets/</code>, serta <code>bootstrap-5.3.8/</code>. Pertahankan struktur relatif agar URL CSS, JavaScript, font, gambar, dan navigasi tetap benar. Tidak dibutuhkan Node atau Python di server produksi.</p>
    <p><code>scripts/</code>, <code>tests/</code>, <code>node_modules/</code>, <code>.venv/</code>, catatan fase, dan laporan tes tidak perlu dideploy. File <code>errors-*.html</code> hanyalah halaman tampilan; konfigurasikan hosting untuk menggunakannya sebagai respons error dengan status HTTP yang benar.</p>
    <p>Saat memperbarui vendor, pin versi paket, salin distribusi yang diperlukan ke <code>assets/bundles/</code>, sertakan lisensi, dan perbarui dokumentasi. <code>npm ci</code> maupun build HTML tidak memperbarui bundle browser secara otomatis.</p>
    <h3>Verifikasi opsional saat pengembangan</h3>'''
        + code('''npm ci
npm test
# Linux: bila lokasi Chrome berbeda
CHROME_PATH=/path/to/chrome npm test''') + '''
    <p class="mb-0">Suite Playwright memakai Chrome lokal di <code>/usr/bin/google-chrome</code> secara default; ubah <code>CHROME_PATH</code> sesuai OS (PowerShell: <code>$env:CHROME_PATH = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'</code>). Periksa juga desktop/mobile, keyboard, form, pagination, dan fitur yang baru diubah. Hasil tes lama tidak menjamin perubahan baru sudah diverifikasi.</p>''')

    add('troubleshooting', '16. Pemecahan masalah', '''
    <div class="table-responsive"><table class="table"><thead><tr><th>Gejala</th><th>Langkah pemeriksaan</th></tr></thead><tbody>
    <tr><td>Halaman tanpa style / aset 404</td><td>Jalankan server dari root repository; pastikan folder Bootstrap dan assets ikut disalin. Periksa Network di DevTools.</td></tr>
    <tr><td><code>python3</code> tidak ditemukan</td><td>Gunakan <code>python</code> atau <code>py</code> yang tersedia. Jalankan server/build langsung dengan executable tersebut.</td></tr>
    <tr><td><code>No module named lxml</code></td><td>Instal requirements menggunakan Python yang sama dengan build di virtual environment.</td></tr>
    <tr><td>Port 4173 sudah dipakai</td><td>Hentikan server lama atau jalankan <code>python3 -m http.server 4174 --bind 127.0.0.1</code>, lalu buka port baru. Origin dan data lokal ikut berubah.</td></tr>
    <tr><td>Perubahan HTML hilang</td><td>Edit sumber di scripts, bukan hanya hasil generated; jalankan build lagi.</td></tr>
    <tr><td>Perubahan CSS/JS belum terlihat</td><td>Hard refresh atau nonaktifkan cache saat DevTools terbuka. Pastikan file yang diedit memang dimuat halaman.</td></tr>
    <tr><td>Dropdown jumlah baris kosong</td><td>Pastikan <code>pageLength</code> ada dalam pilihan length menu. DataTables bawaan memakai 10.</td></tr>
    <tr><td>Canvas proyek sulit digulir</td><td>Periksa penutupan Select2 sebelum re-render dan handler kanban. Di sentuh, swipe singkat untuk scroll, tekan-tahan untuk drag.</td></tr>
    <tr><td>Ikon animasi statis</td><td>Periksa reduced motion, tombol jeda, pemicu, visibilitas ikon, dan error player. Snippet JSON perlu HTTP lokal.</td></tr>
    <tr><td>Data berbeda / tidak tersimpan</td><td>Pastikan origin dan profil browser sama; cek izin serta kuota localStorage.</td></tr>
    <tr><td>Peta gagal tampil</td><td>Baca status pada panel Maps, periksa key, origin yang diizinkan, layanan API, billing, dan koneksi.</td></tr>
    <tr><td>Playwright tidak menemukan browser</td><td>Instal Chrome atau arahkan <code>CHROME_PATH</code> ke executable browser Chromium yang tersedia.</td></tr>
    </tbody></table></div>''')

    toc = ''.join(f'<li><a href="#{key}">{escape(title)}</a></li>' for key, title, _ in sections)
    toc += ''.join(f'<li><a href="#{key}">{title}</a></li>' for key, title in (
        ('page-directory', 'Direktori seluruh halaman'), ('library-directory', 'Library dan versi'),
        ('enhanced-controls', 'Referensi kontrol form'), ('contributing', 'Alur kontribusi'),
    ))
    return (
        heading('Panduan lengkap BRUTAL.', 'Setup, penggunaan komponen, kustomisasi, integrasi, dan deployment dalam satu halaman.')
        + '<div class="docs-layout"><aside class="docs-toc"><nav class="card" aria-label="Daftar isi dokumentasi"><div class="card-body">'
        + '<h2 class="fs-5">Daftar isi</h2><ol class="list-unstyled mb-0">' + toc + '</ol></div></nav></aside>'
        + '<div class="docs-content">' + ''.join(body for _, _, body in sections)
        + docs_appendix(nav) + '<p class="mt-4"><a href="#main">Kembali ke atas ↑</a></p></div></div>'
    )
