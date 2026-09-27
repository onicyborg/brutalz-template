# 🗓️ Development Plan — BRUTAL. Template (Otika Parity)

> **Tujuan**: Mewujudkan seluruh sidebar Otika (`otika.namikulo.com`) ke dalam template BRUTAL. dengan gaya Neobrutalism yang sudah ada.
> **Referensi checklist**: [`SIDEBAR-CHECKLIST.md`](./SIDEBAR-CHECKLIST.md)
> **Stack**: Bootstrap 5.3.8 (lokal) + Bootstrap Bundle JS + library eksternal sesuai kebutuhan.
> **Bahasa UI**: Indonesia (konsisten dengan halaman yang ada).

---

## 📐 Pedoman Tetap (untuk seluruh phase)

### Prinsip Visual Neobrutalism (yang sudah dipakai di BRUTAL.)
- **Border tebal**: 3px solid `#232420` (warna hitam arang) di hampir semua container/card.
- **Bayangan hard shadow**: `box-shadow: 6px 6px 0 0 #232420` (tanpa blur), sering digunakan offset lebih besar (8px / 10px) untuk elemen hero.
- **Warna aksen** (lihat `assets/css/theme.css`):
  - `--brutal-yellow: #ffd84d`
  - `--brutal-purple: #c4a8f5`
  - `--brutal-green: #9ebba3`
  - `--brutal-orange: #f6a96a`
  - `--brutal-pink: #f4a8c4`
  - `--brutal-cream: #f4ecd8`
- **Tipografi**: Heading tebal (700/900), sans-serif (system), uppercase pada label kecil.
- **Tombol**: Kotak dengan border tebal + shadow yang "turun" saat hover/active (translasi `2px`).
- **Card/Stat**: Latar warna aksen + border 3px + hard shadow.

### Standar Halaman Baru
Setiap halaman HTML yang dibuat harus:
1. **Mengikuti struktur file yang ada**: copy kerangka dari `alert.html` atau `buttons.html`.
2. **Tag `<title>`** sesuai nama halaman: `<title>{Nama} — BRUTAL.</title>`
3. **`data-page="{slug}"`** di `<body>` agar JS sidebar bisa menandai halaman aktif.
4. **Sidebar lengkap inline** (sama dengan halaman lain), dengan link yang relevan di-*highlight* `.active`.
5. **Topbar + breadcrumb** sesuai halaman.
6. **Footer** "© 2026 BRUTAL." di akhir.
7. **Section header** dengan eyebrow + judul besar ala neobrutalism (lihat `index.html` → `.hero`, `.panel-heading`).
8. **Demo blok** dibungkus `.card` dengan border tebal + shadow.
9. **JS inisialisasi** di akhir body (Bootstrap bundle sudah include Popper).
10. **Tidak menggunakan CDN library random** — lebih baik pakai file lokal di `assets/` atau `bootstrap-5.3.8/`.

### Standar Library
Library eksternal (SweetAlert, Toastr, DataTables, FullCalendar, ApexCharts, Chart.js, Quill, Select2, Lightbox, Owl, jVectorMap, GMaps) **dimasukkan ke `assets/bundles/`** dengan struktur:

```
assets/bundles/
├── sweetalert/        # sweetalert2
├── toastr/            # toastr (jQuery optional)
├── datatables/        # datatables.net + plugins
├── fullcalendar/      # fullcalendar
├── apexcharts/        # apexcharts
├── chartjs/           # chart.js
├── quill/             # quill editor
├── select2/           # select2 (optional)
├── lightgallery/      # lightgallery
├── owlcarousel/       # owl.carousel
├── jvectormap/        # jvectormap
└── gmaps/             # GMaps.js (google maps wrapper)
```

Versi library yang dipakai mengikuti versi Otika (lihat `otika.namikulo.com/assets/bundles/`).

---

## 📦 Struktur File & Sidebar Akhir

Setelah seluruh phase selesai, struktur `sidebar` akan menjadi (konsisten di setiap halaman):

```
📦 WORKSPACE
├── Dashboard
├── Proyek
├── Kalender
├── Widgets ▾
│   ├── Chart Widgets
│   └── Data Widgets
├── Apps ▾
│   ├── Chat
│   ├── Portfolio
│   └── Blog
└── Email ▾
    ├── Inbox
    ├── Compose
    └── Baca

🧱 BUILDING BLOCKS
├── Komponen UI ▾   (16 submenu — sudah ada)
├── Komponen Lanjutan ▾
│   ├── Avatar
│   ├── Card
│   ├── Modal
│   ├── Sweet Alert
│   ├── Toastr
│   ├── Empty State
│   ├── Multiple Upload
│   ├── Tab
│   └── Pricing
├── Form & Validasi ▾
│   ├── Form dasar          (pindah dari forms.html atau tetap)
│   ├── Form lanjutan
│   ├── Editor (WYSIWYG)
│   ├── Validasi
│   └── Form Wizard
├── Tabel Data ▾
│   ├── Tabel dasar
│   ├── Tabel lanjutan
│   ├── Datatable
│   ├── Export Tabel
│   └── Tabel Editable
├── Grafik & Widget ▾
│   ├── Chart.js (default)
│   ├── amChart
│   ├── apexchart
│   ├── eChart
│   ├── Sparkline
│   └── Morris
└── Ikon ▾
    ├── Font Awesome
    ├── Material Design
    ├── Ion Icons
    ├── Feather Icons
    └── Weather Icon

🖼️ MEDIA
├── Galeri ▾
│   ├── Light Gallery
│   └── Gallery 2
├── Slider ▾
│   ├── Bootstrap Carousel
│   └── Owl Carousel
└── Timeline

🗺️ MAPS
├── Google Maps ▾
│   ├── Simple
│   ├── Marker
│   ├── Multiple Marker
│   ├── Route
│   ├── Advanced Route
│   ├── Draggable Marker
│   ├── Geocoding
│   └── Geolocation
└── Vector Map

📄 HALAMAN
├── Profil
├── Invoice
├── Kontak
├── Post ▾
│   ├── Buat Post
│   └── Daftar Post
├── Autentikasi ▾
│   ├── Login
│   ├── Daftar
│   ├── Lupa Password
│   ├── Reset Password
│   └── Subscribe
├── Errors ▾
│   ├── 403
│   ├── 404
│   ├── 500
│   └── 503
└── Multilevel (nested demo)

🚀 MULAI MEMBANGUN
├── Halaman Kosong
└── Dokumentasi
```

---

# 🟥 PHASE 0 — Fondasi & Refactor Sidebar (PRASYARAT)

> **Tujuan**: Menyiapkan infrastruktur sebelum menambah halaman baru. Tanpa fondasi ini, setiap halaman baru akan jadi salin-tempel sidebar secara manual.

## 0.1 Inventaris & Pemetaan
- [x] Baca `SIDEBAR-CHECKLIST.md` dan putuskan struktur final (entri "🔁 Item yang perlu keputusan").
- [x] Putuskan:
  - [x] File `forms.html` → dipecah atau tetap kompak? (default: **pecah 1 file form dasar + tambah 4 file baru**).
  - [x] File `tables.html` → **pecah** (pindah konten ke `basic-table.html`, sisakan `tables.html` sebagai landing/daftar tabel).
  - [x] File `charts.html` → **pecah** (pindah ke `chart-chartjs.html`, sisakan `charts.html` sebagai overview).
  - [x] File `404.html` → **rename** ke `errors-404.html`.

## 0.2 Refactor Sidebar Menjadi Single Source of Truth
- [x] Buat folder `assets/js/` tambahan atau tambahkan modul `sidebar.js`.
- [x] Pindahkan markup `<aside class="sidebar">` ke template **JS-driven**:
  - [x] Definisikan struktur menu di `assets/js/sidebar-config.js` (array of objects: `{ group, items[] }`).
  - [x] Modul `sidebar.js` akan:
    - Render `<aside>` ke dalam `<div id="sidebar-root"></div>` di setiap halaman.
    - Tandai item `.active` berdasarkan `document.body.dataset.page`.
    - Tangani expand/collapse (Bootstrap collapse API).
    - Tangani mobile drawer (backdrop + toggle).
- [x] Di **setiap halaman HTML**, ganti blok sidebar inline menjadi:
  ```html
  <div id="sidebar-root"></div>
  <script src="assets/js/sidebar-config.js"></script>
  <!-- Muat setelah Bootstrap bundle dan sebelum app.js. -->
  <script src="assets/js/sidebar-icons.js"></script>
  <script src="assets/js/sidebar.js"></script>
  ```
- [x] Verifikasi: buka `index.html`, `alert.html`, `auth-login.html`, `errors-404.html` (hasil rename `404.html`), dan halaman lain — sidebar identik & highlight benar.

## 0.3 Topbar & Footer Konstan
- [x] Evaluasi modul topbar/footer (opsional): tidak dibuat; opsi inline di bawah dipilih.
- [x] Atau biarkan inline untuk saat ini (konsisten dengan pola existing) dan cukup **disalin** saat membuat halaman baru.

## 0.4 Utilitas CSS Tambahan
- [x] Di `assets/css/theme.css` tambahkan utilitas:
  - [x] `.stat-card` (sudah ada, pastikan reusable untuk widget halaman).
  - [x] `.timeline` (untuk phase Timeline).
  - [x] `.map-card` (untuk phase Maps).
  - [x] `.gallery-grid` (untuk phase Gallery).
  - [x] `.code-block` (untuk menampilkan snippet demo di halaman komponen).
- [x] Pastikan tidak ada CSS framework ketiga yang bentrok.

## 0.5 Konvensi Penamaan & Folder
- [x] Library eksternal di `assets/bundles/{nama-lib}/`.
- [x] Ikon set Feather → tetap dipakai (lihat icon SVG di sidebar existing).
- [x] Halaman error menggunakan `errors-{code}.html` (rename `404.html`).

## Hasil eksekusi — 27 September 2026

**Status: ✅ selesai.** Sidebar dan pencarian memakai `assets/js/sidebar-config.js` sebagai sumber tunggal; renderer dan drawer dipisahkan ke `sidebar.js`. Ikon SVG existing dihasilkan ke `sidebar-icons.js` dari generator. Tidak ada library/CSS framework baru.

- Inventaris aktual: 32 halaman, semuanya memakai `sidebar-root`. Halaman auth/error memakai drawer yang sama melalui tombol menu pada desktop maupun mobile.
- Keputusan struktur sudah dicatat di checklist: pemisahan form/tabel/chart dilaksanakan pada Phase 3/4/5. Phase 0 hanya menetapkan keputusan, sesuai bagian 0.1.
- Rename `404.html` ke `errors-404.html` sudah dilaksanakan beserta pembaruan tautan dan generator. File lama tidak menjadi alias.
- Topbar/footer aplikasi tetap inline dari generator; pilihan modul opsional tidak diambil.
- Token CSS aktual adalah `--neo-*` (border 2px, shadow 4px), bukan nama `--brutal-*` pada rancangan awal. Utilitas baru mengikuti token existing agar tampilan tetap konsisten.
- Koreksi inventaris: `auth-reset-password.html` belum ada. Statusnya diperbaiki di checklist; halaman itu tidak dibuat pada Phase 0.
- Verifikasi: `npm run build` sukses; `npm test` **12 passed**. Cakupan meliputi 32 halaman pada 1440/390/320 px, active state dan link, drawer/fokus keyboard, konfigurasi tanpa rebuild, akses langsung `file://`, serta regresi interaksi existing. Screenshot desktop/mobile ditinjau.

## 🚦 Keluar Phase 0 jika:
- ✅ Sidebar sudah ter-render otomatis & aktif state benar.
- ✅ Keputusan struktur final sudah ditulis di `SIDEBAR-CHECKLIST.md` (status 🔁 sudah berubah).
- ✅ Utilitas CSS tersedia.

---

# 🟧 PHASE 1 — Workspace Inti (Widget, Apps, Email)

> **Tujuan**: Memperkaya menu utama WORKSPACE dengan widget dan aplikasi modern ala Otika.

## 1.1 Widgets
> File: `widget-chart.html`, `widget-data.html`

### `widget-chart.html`
- [ ] Sidebar: WORKSPACE > Widgets > Chart Widgets (active).
- [ ] Page heading: "Widget Grafik" dengan deskripsi singkat.
- [ ] Grid 12 kolom berisi:
  - [ ] **Mini line chart** (SVG/CSS sederhana, warna brutal).
  - [ ] **Mini bar chart** (SVG statis).
  - [ ] **Mini donut/pie chart** (SVG conic).
  - [ ] **Mini area chart**.
  - [ ] **Mini stacked bar**.
- [ ] Tiap widget dibungkus `.card stat-card` dengan shadow neobrutalism.
- [ ] Library: **tanpa library** — pakai SVG inline + CSS (sesuai gaya chart di `index.html`).
- [ ] Footer + breadcrumb.

### `widget-data.html`
- [ ] Sidebar: WORKSPACE > Widgets > Data Widgets (active).
- [ ] Page heading: "Widget Data".
- [ ] Komponen:
  - [ ] **KPI stat card** (4 varian warna: purple, green, orange, yellow).
  - [ ] **Progress radial**.
  - [ ] **Info card** dengan ikon Feather.
  - [ ] **List ranking** dengan progress bar.
  - [ ] **Heatmap sederhana** (CSS grid).
  - [ ] **Calendar mini widget**.
- [ ] Library: **tanpa library** — pure CSS/HTML.

## 1.2 Apps

### `chat.html`
- [ ] Layout 2 kolom: daftar percakapan (kiri) + chat aktif (kanan).
- [ ] Avatar, nama, waktu, badge unread.
- [ ] Input chat di bawah + tombol kirim.
- [ ] Styling: bubble chat dengan border tebal neobrutalism.
- [ ] Library: **tanpa** (dummy/seed data saja).

### `portfolio.html`
- [ ] Grid portfolio 3 kolom (filter kategori opsional).
- [ ] Card gambar dengan judul + kategori + link.
- [ ] Library: **tanpa** (gambar dari `assets/img/` lokal).

### `blog.html`
- [ ] Layout blog list (kiri) + sidebar widget (kanan).
- [ ] Card artikel dengan gambar, judul, excerpt, tanggal, tag.
- [ ] Pagination di bawah.
- [ ] Library: **tanpa**.

## 1.3 Email

### `email-inbox.html`
- [ ] Top toolbar: pilih semua, tandai baca, hapus.
- [ ] Sidebar kategori: Inbox, Starred, Sent, Draft, Spam, Trash.
- [ ] Daftar email dengan checkbox, star, avatar pengirim, subject, preview, waktu.
- [ ] Klik email → buka `email-read.html` (link, bukan JS).
- [ ] Library: **tanpa**.

### `email-compose.html`
- [ ] Form compose: Kepada, CC, BCC, Subject, Body.
- [ ] Toolbar formatting (tombol Bold, Italic, Underline — visual saja).
- [ ] Tombol Kirim, Draft, Discard.
- [ ] Library: **tanpa** (atau integrasi ringan dengan Quill jika Phase 5 sudah ada).

### `email-read.html`
- [ ] Header email: avatar, pengirim, tanggal, Kepada/CC.
- [ ] Body email dengan lampiran (file list).
- [ ] Tombol Reply, Forward, Print.
- [ ] Library: **tanpa**.

## 🚦 Keluar Phase 1 jika:
- ✅ 7 file baru dibuat, terdaftar di sidebar, dapat dibuka tanpa error 404.
- ✅ Style neobrutalism konsisten di seluruh halaman baru.
- ✅ Active state sidebar benar.

---

# 🟨 PHASE 2 — Building Blocks Lanjutan (Advanced UI)

> **Tujuan**: Showcase komponen lanjutan Otika yang belum ada di BRUTAL.

## 2.1 Avatar (`avatar.html`)
- [ ] Avatar bulat dengan ukuran (xs/sm/md/lg/xl).
- [ ] Avatar dengan status dot (online/offline/away).
- [ ] Avatar group / stack.
- [ ] Avatar placeholder inisial (seperti di sidebar existing).
- [ ] Library: **tanpa**.

## 2.2 Card (`card.html`)
- [ ] Card basic, dengan header/footer.
- [ ] Card dengan warna aksen (purple, green, yellow, orange).
- [ ] Card dengan ikon + judul + body.
- [ ] Card statistik (kombinasi stat-card).
- [ ] Card dengan image overlay.
- [ ] Library: **tanpa**.

## 2.3 Modal (`modal.html`)
- [ ] Demo modal basic (size sm/md/lg/xl/full).
- [ ] Modal scrollable, centered, fullscreen.
- [ ] Modal dengan form di dalam.
- [ ] Modal konfirmasi (delete).
- [ ] Library: **Bootstrap 5 modal** (sudah di bundle).

## 2.4 Sweet Alert (`sweet-alert.html`)
- [ ] Install `assets/bundles/sweetalert/sweetalert2.min.js` + CSS.
- [ ] Demo: success, error, warning, info, confirm, custom HTML, toast.
- [ ] Tombol trigger masing-masing demo.
- [ ] Library: **SweetAlert2** (versi Otika).

## 2.5 Toastr (`toastr.html`)
- [ ] Install `assets/bundles/toastr/toastr.min.js` + CSS.
- [ ] Demo: success, info, warning, error.
- [ ] Posisi toast (top-right, bottom-left, dll).
- [ ] Library: **Toastr** (versi Otika).

## 2.6 Empty State (`empty-state.html`)
- [ ] Empty state dengan ilustrasi SVG sederhana.
- [ ] Empty state dengan CTA button.
- [ ] Empty state dengan list kosong di dalam card.
- [ ] Library: **tanpa**.

## 2.7 Multiple Upload (`multiple-upload.html`)
- [ ] Install `assets/bundles/dropzone/dropzone.min.js` (atau library upload Otika).
- [ ] Area drop file dengan preview thumbnail.
- [ ] Indikator progress per file.
- [ ] Library: **Dropzone.js** (atau sesuai library Otika).

## 2.8 Tab (`tabs.html`)
- [ ] Tab basic (atas), tab bawah, tab kiri/kanan (vertikal).
- [ ] Tab dengan ikon.
- [ ] Tab pill, tab justified.
- [ ] Library: **Bootstrap 5 nav-tabs** (sudah built-in).

## 🚦 Keluar Phase 2 jika:
- ✅ 8 file baru selesai, style konsisten neobrutalism.
- ✅ Library eksternal (SweetAlert, Toastr, Dropzone) terinstal di `assets/bundles/` dan termuat di halaman demo.

---

# 🟩 PHASE 3 — Forms (Lanjutan)

> **Tujuan**: Memperkaya showcase form yang saat ini hanya `forms.html`.

## 3.1 Form Dasar (Refactor)
- [ ] **Opsi A**: Pindahkan konten `forms.html` ke `basic-form.html` (sesuai Otika), ubah `forms.html` jadi landing/overview.
- [ ] **Opsi B**: Pertahankan `forms.html` sebagai showcase utama + buat halaman baru khusus (lebih hemat).
- [ ] Putuskan di awal phase.

## 3.2 `forms-advanced-form.html`
- [ ] Form dengan layout kompleks: 2 kolom, field group, helper text, tooltip.
- [ ] Select2 / Choices.js (jika dipakai Otika) untuk dropdown dengan pencarian.
- [ ] Library: **Select2** atau **Choices.js** sesuai Otika.

## 3.3 `forms-editor.html`
- [ ] Install `assets/bundles/quill/quill.min.js` (WYSIWYG).
- [ ] Editor full toolbar (header, bold, italic, list, link, image, code).
- [ ] Demo beberapa skin toolbar.
- [ ] Library: **Quill**.

## 3.4 `forms-validation.html`
- [ ] Form dengan validasi HTML5 native (required, pattern, min/max).
- [ ] Validasi via Bootstrap class (`is-valid`, `is-invalid`).
- [ ] Pesan error kustom per field.
- [ ] Library: **tanpa** (atau `bs-custom-file-input` jika perlu).

## 3.5 `form-wizard.html`
- [ ] Install `assets/bundles/jquery-steps/jquery.steps.min.js` (atau SmartWizard).
- [ ] Wizard 3–4 langkah: Personal Info → Account → Confirmation → Done.
- [ ] Validasi antar step.
- [ ] Library: **jQuery Steps** atau **SmartWizard** sesuai Otika.

## 🚦 Keluar Phase 3 jika:
- ✅ Form dasar dipisah/dipertahankan sesuai keputusan.
- ✅ 4 file form baru aktif.
- ✅ Library Quill, Select2, jQuery Steps terinstal dan jalan di demo.

---

# 🟦 PHASE 4 — Tables (Lanjutan)

> **Tujuan**: Sama seperti Phase 3 tapi untuk tabel.

## 4.1 Tabel Dasar (Refactor)
- [ ] Pindahkan konten `tables.html` ke `basic-table.html`.
- [ ] Buat `tables.html` jadi halaman overview/landing (daftar tipe tabel + link).

## 4.2 `advance-table.html`
- [ ] Tabel dengan sorting client-side (sortable.js atau implementasi vanilla).
- [ ] Tabel dengan row hover, striped, bordered.
- [ ] Tabel responsif di mobile.
- [ ] Library: opsional **sortable.js** (atau vanilla JS).

## 4.3 `datatables.html`
- [ ] Install `assets/bundles/datatables/datatables.min.js` + CSS.
- [ ] Tabel dengan search box, pagination, sorting multi-kolom, info jumlah data.
- [ ] Library: **DataTables.net** (versi Otika).

## 4.4 `export-table.html`
- [ ] Install plugin export: `datatables-buttons`, `jszip`, `pdfmake`, `buttons.html5`.
- [ ] Tabel dengan tombol Export ke Excel, CSV, PDF, Print.
- [ ] Library: **DataTables Buttons**.

## 4.5 `editable-table.html`
- [ ] Install plugin `datatables-editor` atau pakai library **X-editable**.
- [ ] Tabel dengan cell inline-editable (klik → edit → simpan).
- [ ] Library: **X-editable** atau **DataTables Editor**.

## 🚦 Keluar Phase 4 jika:
- ✅ Tabel dasar direfactor.
- ✅ 4 file tabel baru aktif.
- ✅ Library DataTables + plugins terinstal.

---

# 🟪 PHASE 5 — Charts (Per Library)

> **Tujuan**: Memperkaya showcase chart. Saat ini hanya `charts.html` (1 chart SVG inline). Target: 6 library.

## 5.0 Refactor `charts.html`
- [ ] Pindahkan konten chart existing ke `chart-chartjs.html`.
- [ ] `charts.html` jadi overview (daftar library + ringkasan).

## 5.1 `chart-chartjs.html`
- [ ] Library: **Chart.js** (versi Otika).
- [ ] Demo: Line, Bar, Doughnut, Pie, Radar, Mixed.
- [ ] Styling chart color pakai palet neobrutalism.

## 5.2 `chart-apexchart.html`
- [ ] Library: **ApexCharts** (sudah dipakai Otika di dashboard).
- [ ] Demo: Line area, Column, Pie, Radial Bar, Heatmap.
- [ ] Styling color neobrutalism.

## 5.3 `chart-amchart.html`
- [ ] Library: **amCharts 4** atau **5** (sesuai Otika).
- [ ] Demo: Bar, Pie, Line, Map (kalau ringan).

## 5.4 `chart-echart.html`
- [ ] Library: **Apache ECharts**.
- [ ] Demo: Line, Bar, Pie, Scatter, Candlestick (opsional).

## 5.5 `chart-sparkline.html`
- [ ] Library: **Sparkline** (jquery.sparkline atau vanilla).
- [ ] Demo: sparkline di dalam card stat (line, bar, tristate, pie).

## 5.6 `chart-morris.html`
- [ ] Library: **Morris.js** (membutuhkan jQuery + Raphael).
- [ ] Demo: Line, Area, Bar, Donut.

## 🚦 Keluar Phase 5 jika:
- ✅ 6 file chart library aktif.
- ✅ Semua library terinstal di `assets/bundles/`.
- ✅ Color palette konsisten neobrutalism.

---

# 🟫 PHASE 6 — Icons

> **Tujuan**: 5 halaman showcase ikon library.

## 6.0 Keputusan
- [ ] Feather Icons sudah dipakai di sidebar BRUTAL. (SVG inline). Halaman `icon-feather.html` cukup mendemokan daftar icon yang umum dipakai.
- [ ] Library lain pakai CDN lokal (file di `assets/bundles/`).

## 6.1 `icon-font-awesome.html`
- [ ] Install Font Awesome 5/6 di `assets/bundles/fontawesome/`.
- [ ] Grid ikon: solid, regular, brand. Copy-paste snippet.

## 6.2 `icon-material.html`
- [ ] Material Icons via Google Fonts (font di lokal) atau file iconfont.
- [ ] Grid ikon Material.

## 6.3 `icon-ionicons.html`
- [ ] Install `assets/bundles/ionicons/ionicons.min.css/js`.
- [ ] Grid ikon Ionicons.

## 6.4 `icon-feather.html`
- [ ] Daftar Feather icon (SVG inline) yang dipakai di template.
- [ ] Tiap ikon diklik → salin SVG path otomatis (clipboard.js).

## 6.5 `icon-weather-icon.html`
- [ ] Install `weather-icons` (CSS icon font).
- [ ] Grid ikon cuaca.

## 🚦 Keluar Phase 6 jika:
- ✅ 5 file ikon aktif.
- ✅ Semua library/icon-font terinstal di `assets/bundles/`.

---

# 🟫 PHASE 7 — Media (Gallery, Sliders, Timeline)

## 7.1 Gallery

### `light-gallery.html`
- [ ] Install `assets/bundles/lightgallery/lightgallery.min.js` + CSS.
- [ ] Grid thumbnail gambar, klik → lightbox.
- [ ] Library: **LightGallery**.

### `gallery1.html`
- [ ] Gallery sederhana dengan grid masonry (CSS columns / grid).
- [ ] Library: **tanpa**.

## 7.2 Sliders

### `carousel.html`
- [ ] Bootstrap Carousel showcase: slide tunggal, multiple, dengan caption, dengan kontrol.
- [ ] Library: **Bootstrap 5 carousel** (built-in).

### `owl-carousel.html`
- [ ] Install `assets/bundles/owlcarousel/owl.carousel.min.js` + CSS.
- [ ] Demo: carousel basic, dengan autoplay, dengan thumbnail nav.
- [ ] Library: **Owl Carousel**.

## 7.3 Timeline (`timeline.html`)
- [ ] Timeline vertikal dengan activity items (ikon, waktu, deskripsi).
- [ ] Varian: kiri-kanan (zigzag), single column, dengan image attachment.
- [ ] Library: **tanpa**.

## 🚦 Keluar Phase 7 jika:
- ✅ 5 file media baru aktif.
- ✅ Library LightGallery, Owl Carousel terinstal.

---

# 🟨 PHASE 8 — Maps (Butuh API Key)

## 8.0 Catatan
- Google Maps butuh API Key dari Google Cloud Console. Tampilkan placeholder + cara mengisi API Key.
- jVectorMap murni client-side, tanpa API key.

## 8.1 Google Maps (8 halaman)

### `gmaps-simple.html`
- [ ] Init peta dasar (center Indonesia).
- [ ] Library: **GMaps.js** (`assets/bundles/gmaps/gmaps.min.js`).

### `gmaps-marker.html`
- [ ] Peta + 1 marker dengan info window.

### `gmaps-multiple-marker.html`
- [ ] Peta + banyak marker (data array).

### `gmaps-route.html`
- [ ] Peta + direction route A→B.

### `gmaps-advanced-route.html`
- [ ] Peta + multi-waypoint + alternatif.

### `gmaps-draggable-marker.html`
- [ ] Peta + marker yang bisa di-drag, koordinat update realtime.

### `gmaps-geocoding.html`
- [ ] Input alamat → peta pindah + marker.

### `gmaps-geolocation.html`
- [ ] Tombol "Lokasi saya" → peta zoom ke user location.

## 8.2 `vector-map.html`
- [ ] Install `assets/bundles/jvectormap/jquery-jvectormap.min.js` + CSS + world map data.
- [ ] Peta dunia interaktif dengan warna per-region.

## 🚦 Keluar Phase 8 jika:
- ✅ 9 file peta aktif (8 gmaps + 1 vector).
- ✅ Dokumentasi cara isi API Key tercantum di setiap halaman gmaps.

---

# 🟥 PHASE 9 — Halaman Khusus & Errors

## 9.1 Subscribe (`subscribe.html`)
- [ ] Landing page sederhana: headline besar neobrutalism + form subscribe email + CTA.
- [ ] Varian dengan ilustrasi SVG.

## 9.2 Error Pages

### `errors-403.html`
- [ ] 403: "Akses ditolak", ilustrasi + tombol kembali.

### `errors-404.html` (rename dari `404.html`)
- [ ] 404: "Halaman tidak ditemukan".
- [ ] Update semua link `404.html` di seluruh halaman agar pointing ke `errors-404.html`.

### `errors-500.html`
- [ ] 500: "Terjadi kesalahan server".

### `errors-503.html`
- [ ] 503: "Layanan sedang maintenance".

## 9.3 Post Pages

### `create-post.html`
- [ ] Form buat post: judul, kategori, tags, cover image, body (Quill editor), publish toggle.
- [ ] Library: **Quill** (re-use dari Phase 3).

### `posts.html`
- [ ] Daftar post (card grid) + filter kategori + search.

## 9.4 Contact (`contact.html`)
- [ ] Layout 2 kolom: form kontak (kiri) + info alamat/telepon/social (kanan).
- [ ] Peta statis opsional (gambar).

## 9.5 Multilevel Nested Menu Demo
- [ ] Tambah entry di sidebar: **Multilevel** (icon `chevrons-down`).
- [ ] Submenu level 1, level 2 (nested collapse), level 3 (deepest).
- [ ] Tujuannya untuk demo kemampuan nested dropdown.
- [ ] Halaman tujuannya bisa `#` atau halaman demo khusus.

## 🚦 Keluar Phase 9 jika:
- ✅ 7 file baru (subscribe, 3 errors tambahan, create-post, posts, contact) + multilevel entry aktif.
- ✅ Semua link `404.html` diupdate ke `errors-404.html`.

---

# 🟪 PHASE 10 — Polish, Konsistensi, & Final QA

> **Tujuan**: Memastikan hasil akhir setara kualitas Otika dengan style neobrutalism.

## 10.1 Konsistensi Sidebar
- [ ] Pastikan semua halaman (lama + baru) memakai sidebar hasil Phase 0 (auto-render).
- [ ] Pastikan `data-page` di setiap halaman benar.
- [ ] Pastikan `active` highlight benar di tiap halaman.

## 10.2 Konsistensi Topbar
- [ ] Breadcrumb sesuai halaman.
- [ ] Tombol search (`#searchModal`) berfungsi dari semua halaman (sudah ada di `index.html` — pastikan ada di semua halaman).

## 10.3 Konsistensi Footer
- [ ] "© 2026 BRUTAL." di semua halaman.

## 10.4 Validasi & Aksesibilitas
- [ ] Setiap halaman punya `<title>` unik.
- [ ] Skip link "Lewati ke konten" di setiap halaman.
- [ ] Ikon SVG punya `aria-hidden="true"`, elemen interaktif punya `aria-label`.
- [ ] Lighthouse Accessibility ≥ 90.

## 10.5 Performance
- [ ] Library eksternal hanya di-load di halaman yang butuh (tidak global).
- [ ] Kompres gambar jika perlu.
- [ ] Inline critical CSS opsional.

## 10.6 Dokumentasi
- [ ] Update `docs.html` dengan:
  - [ ] Daftar seluruh halaman.
  - [ ] Library apa saja yang dipakai + versi.
  - [ ] Cara menambah halaman baru (panduan kontribusi).
  - [ ] Konvensi penamaan file & folder.

## 10.7 README Project
- [ ] Update `README.md` dengan:
  - [ ] Deskripsi project.
  - [ ] Cara menjalankan (statis HTML, bisa langsung buka `index.html` atau pakai static server).
  - [ ] Struktur folder.
  - [ ] Credits.

## 10.8 Smoke Test
- [ ] Buka **setiap** halaman baru, cek:
  - [ ] Sidebar render benar.
  - [ ] Active state benar.
  - [ ] Topbar breadcrumb benar.
  - [ ] Library eksternal termuat (cek console log error).
  - [ ] Style neobrutalism konsisten.
- [ ] Cek **mobile view** untuk beberapa halaman kompleks (forms-wizard, charts, gmaps).

## 🚦 Selesai Phase 10 = Project COMPLETE.

---

# 📊 Progress Tracker Kumulatif

Update checklist di bawah setiap phase selesai. Hubungkan dengan `SIDEBAR-CHECKLIST.md`.

| Phase | Tema | File Baru | File Diubah | Status |
| --- | --- | --- | --- | --- |
| 0 | Fondasi & Sidebar | 3 JS sidebar + panduan bundles + tes sidebar | 32 HTML (termasuk rename 404), generator, app.js, CSS, dokumentasi | ✅ Selesai — 12 tes lulus |
| 1 | Workspace Inti | 7 (widget-chart, widget-data, chat, portfolio, blog, email-inbox, email-compose, email-read) | 0 | ⬜ |
| 2 | Building Blocks Lanjutan | 8 (avatar, card, modal, sweet-alert, toastr, empty-state, multiple-upload, tabs) | 0 | ⬜ |
| 3 | Forms Lanjutan | 4 (+refactor forms.html) | 1 | ⬜ |
| 4 | Tables Lanjutan | 4 (+refactor tables.html) | 1 | ⬜ |
| 5 | Charts | 5 (+refactor charts.html) | 1 | ⬜ |
| 6 | Icons | 5 | 0 | ⬜ |
| 7 | Media | 5 | 0 | ⬜ |
| 8 | Maps | 9 | 0 | ⬜ |
| 9 | Halaman Khusus & Errors | 7 + multilevel entry | rename `404.html` | ⬜ |
| 10 | Polish & QA | 0 | 2 (docs.html, README.md) | ⬜ |

**Total**: ~57 file baru, ~5 file diubah.

---

# 🤖 Prompt untuk Agent (Template)

Saat meminta agent lain untuk melanjutkan phase tertentu, gunakan template berikut:

```
Baca dan pahami dua file ini:
1. /home/geats/Project Pribadi/neo-brutalism-template-web/SIDEBAR-CHECKLIST.md
2. /home/geats/Project Pribadi/neo-brutalism-template-web/PHASE-PLAN.md

Tugas kamu: kerjakan PHASE {N} — {Judul Phase}.

Sebelum mulai:
- Baca phase {N} secara lengkap.
- Cek halaman referensi di folder Otika:
  /mnt/C80A6A9E0A6A88F0/Templete Web/otika.namikulo.com/{file-referensi-otika}.html
  (lihat konten + komponen apa saja yang ditampilkan)
- Cek style neobrutalism di:
  /home/geats/Project Pribadi/neo-brutalism-template-web/assets/css/theme.css
  dan contoh halaman BRUTAL. yang sudah ada (alert.html, buttons.html, dll).

Aturan penting:
- Setiap halaman baru WAJIB menyertakan:
  • Sidebar lengkap (pakai pola auto-render dari Phase 0, atau inline seperti halaman existing — sesuai konvensi saat agent mulai).
  • Topbar dengan breadcrumb.
  • Footer "© 2026 BRUTAL."
  • Tag <body data-page="{slug}">.
  • Title "<title>{Nama} — BRUTAL.</title>".
- Style konsisten neobrutalism: border tebal #232420, hard shadow 6-8px, palet warna di theme.css.
- Bahasa UI: Indonesia.
- Library eksternal disimpan di assets/bundles/{nama-lib}/.

Setelah selesai:
- Verifikasi halaman bisa dibuka, tidak ada error console.
- Update status di SIDEBAR-CHECKLIST.md dari ❌ ke ✅.
- Update kolom Status di tabel progress PHASE-PLAN.md dari ⬜ ke ✅.

Jangan kerjakan phase lain di luar {N} kecuali eksplisit diminta.
```

---

> 📌 **Tips Eksekusi**: Karena setiap phase berdiri sendiri (kecuali Phase 0), kamu bisa kerjakan paralel dengan beberapa agent pada phase berbeda sekaligus, **setelah** Phase 0 selesai.
