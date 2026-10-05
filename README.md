# BRUTAL. — Neubrutalism Bootstrap Admin

Template admin HTML statis berbahasa Indonesia, berbasis **Bootstrap 5.3.8** dengan **93 halaman** siap pakai. Tema memakai garis hitam, bayangan solid, dan palet pastel. Bootstrap serta library browser disimpan lokal; preview tidak membutuhkan bundler atau instalasi npm.

**Panduan lengkap:** buka [docs.html](docs.html) melalui server lokal. Panduan tersebut mencakup setup, struktur, kustomisasi, komponen, navigasi, data lokal, integrasi backend, deployment, dan troubleshooting, dengan direktori semua halaman dan versi library.

## Setup dari repository

### 1. Persyaratan

- Git untuk clone repository.
- Python **3.10+** untuk server lokal dan generator HTML.
- Browser modern.
- Node.js **22+** dan npm hanya jika memakai perintah npm, memasang dependensi development, atau mengerjakan vendor/pengujian. Preview lewat Python langsung tidak memerlukannya.

### 2. Clone dan preview

```bash
git clone https://github.com/onicyborg/brutalz-template.git
cd brutalz-template
python3 -m http.server 4173 --bind 127.0.0.1
```

Buka:

- Dashboard: **http://127.0.0.1:4173/**
- Dokumentasi lengkap: **http://127.0.0.1:4173/docs.html**
- Animated Icons: **http://127.0.0.1:4173/icon-animated.html**

Hentikan server dengan **Ctrl+C**. Jalankan server dari root repository, tempat `index.html` berada.

Pada Windows, jika `python3` tidak tersedia:

```powershell
py -m http.server 4173 --bind 127.0.0.1
```

Jika npm dan executable `python3` tersedia, perintah yang setara adalah:

```bash
npm run dev
```

**Tidak perlu `npm install`/`npm ci` untuk preview.** HTML dan aset runtime sudah ada di Git. Sebagian besar demo juga dapat dibuka melalui `file://`, tetapi server HTTP dianjurkan untuk clipboard, pemuatan JSON pada snippet, dan penyimpanan browser yang konsisten.

### 3. Setup untuk mengedit generator

HTML permanen dikelola oleh Python di `scripts/`. Instal dependensi build di virtual environment.

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-build.txt
python scripts/build.py
```

Windows PowerShell, tanpa harus mengaktifkan environment:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-build.txt
.\.venv\Scripts\python.exe scripts/build.py
```

Jika environment aktif menyediakan `python3`, `npm run build` menjalankan generator yang sama. Build menggunakan lxml, memformat HTML, dan memeriksa kesetaraan semantiknya. Tidak ada watcher otomatis: build lagi setelah mengubah generator, lalu refresh browser. Untuk perubahan CSS/JS, cukup refresh.

**Jangan hanya mengedit HTML hasil build:** perubahan tersebut akan tertimpa. Ubah sumber halaman dalam `scripts/*_pages.py`, `scripts/documentation_page.py`, atau `scripts/build.py`. Generator tidak mengompilasi Sass dan tidak menyalin otomatis paket dari `node_modules` ke folder bundle.

### 4. Dependensi JavaScript development (opsional)

```bash
npm ci
```

Perintah ini menggunakan versi dari `package-lock.json`. Diperlukan untuk suite Playwright atau pekerjaan vendor, bukan untuk menjalankan HTML yang sudah dibundel. Paket Morris.js lama dapat mengeluarkan peringatan engine; preview template menggunakan bundle browser lokal, bukan runtime Node paket tersebut.

## Modul yang tersedia

| Modul | Isi |
| --- | --- |
| Workspace | Dashboard, canvas proyek dengan drag/drop dan pengurutan, kalender, widget, chat, portfolio, blog, email |
| Komponen UI | 16 halaman: Alert sampai Typography, termasuk tombol, navbar, pagination, tooltip, dan flag |
| Komponen lanjutan | Avatar, card, modal, SweetAlert2, Toastr, empty state, upload preview, tabs, pricing |
| Form | Input dasar, Select2, Flatpickr, Quill, validasi, wizard |
| Tabel | Proyek, variasi tabel, DataTables, ekspor Excel/CSV/PDF/cetak, editor sel |
| Grafik | Chart.js, ApexCharts, amCharts 4, ECharts, Sparkline, Morris |
| Ikon | Font Awesome, Material, Ionicons, Feather, Weather, **Animated Icons (Lordicon)** |
| Media | GLightbox, masonry, Bootstrap Carousel, Owl Carousel, timeline |
| Peta | Delapan demo Google Maps, peta vektor lokal |
| Halaman | Profil, autentikasi demo, subscribe, kontak, post, invoice, error, blank, dokumentasi |

Daftar setiap file beserta tautannya dihasilkan langsung dari konfigurasi sidebar pada [docs.html](docs.html#page-directory).

## Struktur proyek

```text
*.html                         Halaman siap preview/deploy
assets/css/                    Tema, kontrol, dan style modul
assets/js/                     Interaksi dan konfigurasi navigasi
assets/bundles/                Distribusi browser pihak ketiga + lisensi
assets/img/                    SVG, favicon, flag, ilustrasi
assets/files/                  Contoh lampiran lokal
bootstrap-5.3.8/               Runtime Bootstrap + source map + lisensi
scripts/build.py               Shell dan proses generate HTML
scripts/*_pages.py             Sumber konten modul
scripts/documentation_page.py  Sumber dokumentasi lengkap
scripts/docs_page.py           Direktori halaman/library dokumentasi
scripts/format_html.py         Formatter dan pemeriksaan semantik
requirements-build.txt         Dependensi Python untuk generator
package.json                   Perintah npm dan versi paket
package-lock.json              Kunci dependensi JavaScript
tests/                         Suite development Playwright
playwright.config.js           Konfigurasi browser dan server tes
PHASE-PLAN.md                   Riwayat rencana implementasi
SIDEBAR-CHECKLIST.md            Riwayat dan cakupan halaman
```

Paket sumber Bootstrap upstream telah diringkas menjadi CSS/JS yang benar-benar dipakai, source map, dan lisensi. Dokumentasi upstream, contoh, tes upstream, Sass, serta distribusi alternatif tidak diperlukan oleh generator ini. Folder dependency lokal, cache, laporan tes, catatan fixing pribadi, dan screenshot referensi diabaikan Git.

## Kustomisasi dan menambah halaman

1. Ubah token warna, border, dan shadow di `assets/css/theme.css`. Style komponen khusus berada di CSS modul. Biarkan file vendor tetap asli.
2. Untuk mengubah brand/topbar/footer/modal bersama, edit `scripts/build.py`; renderer sidebar berada di `assets/js/sidebar.js`. Ganti favicon di `assets/img/favicon.svg`.
3. Tambah halaman ke `assets/js/sidebar-config.js`. `page` harus sama dengan nama file tanpa `.html`; dropdown memakai `id` unik dan `children`. Pertahankan format JSON valid pada array.
4. Tambahkan fungsi konten dan mapping halaman di generator. Muat vendor/style/script khusus hanya pada halaman terkait.
5. Jalankan build dan periksa hasil. Gunakan ID unik untuk input, modal, tab, serta semua atribut target/ARIA.

`blank.html` dapat disalin untuk prototipe manual. Ubah title, `body[data-page]`, konten, dan entri sidebar. Salinan manual tidak diperbarui generator; pindahkan kontennya ke generator untuk pemeliharaan konsisten.

jQuery, Select2, dan Flatpickr dimuat pada semua halaman karena kontrol form/modal dipakai bersama. Library lain dimuat per modul. Jangan memuat jQuery atau Bootstrap dua kali. Detail urutan aset, snippet, API kontrol, dan Animated Icons tersedia dalam panduan HTML.

## Data demo dan backend

Interaksi frontend memakai `localStorage` dengan prefix `brutal.`. Proyek, urutan kartu, tugas, agenda, profil, chat, email, edit tabel, post, dan subscriber hanya berada di browser tersebut. `localhost` dan `127.0.0.1`, port berbeda, atau profil browser berbeda memiliki data terpisah.

Reset di halaman Profil menghapus proyek/tugas/agenda/profil/preferensi/chat/email. Edit tabel, post, subscriber, dan key Maps memiliki key terpisah; lihat [referensi penyimpanan](docs.html#storage) untuk reset yang tepat. Jangan menghapus seluruh localStorage bila origin juga dipakai aplikasi lain.

Login/register/reset password tidak membuat akun atau sesi autentikasi. Chat/email, subscribe, kontak, publikasi, dan upload bukan layanan server. Statistik serta grafik memakai angka ilustratif. Hubungkan handler JavaScript terkait ke API milikmu, dengan autentikasi, otorisasi, validasi server, dan penyimpanan permanen.

## Google Maps

Google Maps adalah integrasi opsional yang memerlukan koneksi internet, API key browser, layanan API terkait, dan billing Google Cloud. Masukkan key lewat panel halaman `gmaps-*.html`; jangan menanamnya di source. Key disimpan pada `brutal.mapsApiKey` dan dapat dihapus melalui tombol pada panel.

Siapkan Maps JavaScript API untuk peta, Routes API untuk demo rute, dan Geocoding API untuk pencarian alamat. Batasi key ke origin/domain serta API yang dipakai. Geolocation memerlukan izin browser dan HTTPS/localhost. Tanpa key, placeholder tetap ditampilkan. `vector-map.html` berjalan dengan aset lokal tanpa Google Maps.

## Deploy statis

Salin seluruh `*.html`, `assets/`, dan `bootstrap-5.3.8/` ke hosting statis dengan struktur yang sama. Tidak perlu menjalankan npm/Python di hosting. Direktori `scripts`, `tests`, dependency development, cache, serta catatan fase tidak perlu diunggah.

Konfigurasikan hosting untuk memakai `errors-*.html` dan status HTTP yang sesuai jika ingin halaman error aktual. Server Python development hanya untuk preview lokal.

Saat memperbarui dependency, pin versi, salin distribusi browser yang diperlukan, pertahankan lisensi/kredit, dan perbarui dokumentasi. `npm ci` saja tidak mengganti aset yang disajikan dari `assets/bundles/`.

## Pengujian opsional

```bash
npm ci
npm test
```

Playwright dikonfigurasi menggunakan Chrome lokal di `/usr/bin/google-chrome`. Jika lokasi berbeda:

```bash
CHROME_PATH=/path/to/chrome npm test
```

Windows PowerShell:

```powershell
$env:CHROME_PATH = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
npm test
```

Tes menjalankan server pada port 4173. Pengujian bukan syarat preview atau build. Periksa juga tampilan mobile, keyboard, form, canvas proyek, dan fitur yang baru diubah secara manual. Hasil verifikasi historis ada pada catatan fase; bukan jaminan hasil perubahan terbaru.

## Troubleshooting singkat

| Masalah | Solusi |
| --- | --- |
| `python3` tidak tersedia | Pakai `python`/`py` untuk server dan build secara langsung. |
| `No module named lxml` | Instal requirements dengan Python virtual environment yang dipakai build. |
| Port 4173 dipakai | Hentikan server lama atau gunakan port lain, misalnya 4174. |
| CSS/JS 404 | Pastikan server berjalan dari root proyek dan semua folder runtime tersalin. |
| Perubahan hilang setelah build | Edit generator, bukan hanya HTML hasil generate. |
| Data demo tidak sama | Periksa origin, port, profil browser, dan izin localStorage. |
| Ikon animasi diam | Periksa reduced motion, tombol jeda, trigger, dan Network/Console. |
| Snippet JSON gagal pada `file://` | Jalankan melalui server HTTP lokal. |
| Maps tidak tampil | Periksa pesan panel, key, pembatasan origin/API, billing, serta koneksi. |

## Kredit dan lisensi

Bootstrap 5.3.8 berlisensi MIT; salinan lisensi dipertahankan di [bootstrap-5.3.8/LICENSE](bootstrap-5.3.8/LICENSE). Sumber, versi, dan lisensi library lain ada di [assets/bundles/README.md](assets/bundles/README.md). Ikon Lordicon memiliki ketentuan artwork tersendiri dari player MIT; atribusi di galeri tetap disertakan. Branding amCharts tetap ditampilkan sesuai bundle yang digunakan.

Otika menjadi referensi cakupan halaman dan navigasi. Tema, markup, SVG antarmuka, serta interaksi BRUTAL. dibuat untuk proyek ini; aset Otika tidak disalin. Penggunaan template saat ini untuk kebutuhan pribadi pemilik repository.
