# BRUTAL. — Neubrutalism Bootstrap Admin

Template admin statis berbahasa Indonesia, menggunakan **Bootstrap 5.3.8 lokal**. Desain original dengan border hitam, bayangan solid, palet lilac/mint/peach/yellow, dan layout responsif. Tidak membutuhkan CDN, font eksternal, atau bundler untuk dijalankan. jQuery dimuat lokal hanya pada demo Toastr, Select2, jQuery Steps, DataTables, Sparkline, Morris.js, dan Owl Carousel.

## Menjalankan

Buka `index.html` langsung di browser, atau gunakan server lokal (Python 3):

```bash
npm run dev
# http://localhost:4173
```

Tidak perlu `npm install` untuk melihat template. Instalasi npm hanya diperlukan untuk pengujian browser.

## Halaman yang tersedia

| File | Isi |
| --- | --- |
| `index.html` | Dashboard, statistik, grafik, proyek terbaru, checklist tugas |
| `components.html` | Indeks 16 halaman komponen UI, modal dan toast workspace |
| `alert.html` hingga `typography.html` | Halaman terpisah untuk 16 komponen pada menu Komponen UI |
| `forms.html` | Overview lima demo form |
| `basic-form.html` | Input, select, floating label, checkbox, radio, switch, range, file picker |
| `forms-advanced-form.html` | Field group dua kolom, helper, tooltip, pencarian Select2 |
| `forms-editor.html` | Quill rich text editor dengan tema Snow dan Bubble |
| `forms-validation.html` | Validasi native HTML5 dan umpan balik Bootstrap per field |
| `form-wizard.html` | jQuery Steps empat langkah dengan validasi antar langkah |
| `tables.html` | Overview lima demo tabel |
| `basic-table.html` | Tabel proyek workspace dengan pencarian, filter, sorting, pagination, CSV |
| `advance-table.html` | Variasi Bootstrap striped, hover, bordered, dan sorting lokal |
| `datatables.html` | DataTables dengan pencarian, pagination, dan urut multi-kolom |
| `export-table.html` | DataTables Buttons untuk ekspor Excel, CSV, PDF, dan Print |
| `editable-table.html` | Editor sel lokal dengan validasi dan penyimpanan di browser |
| `charts.html` | Overview enam library grafik |
| `chart-chartjs.html` | Enam demo Chart.js dan showcase SVG dua periode, donut, statistik, timeline sebelumnya |
| `chart-apexchart.html`, `chart-amchart.html` | Demo ApexCharts dan amCharts 4 |
| `chart-echart.html`, `chart-sparkline.html`, `chart-morris.html` | Demo Apache ECharts, Sparkline, dan Morris.js |
| `icon-font-awesome.html`, `icon-material.html` | Grid Font Awesome Free dan Material Icons lokal |
| `icon-ionicons.html`, `icon-feather.html`, `icon-weather-icon.html` | Grid Ionicons, Feather SVG, dan Weather Icons lokal |
| `light-gallery.html`, `gallery1.html` | Lightbox GLightbox dan galeri masonry tanpa plugin |
| `carousel.html`, `owl-carousel.html` | Variasi Bootstrap Carousel dan Owl Carousel lokal |
| `timeline.html` | Timeline vertikal, zigzag, dan lampiran gambar |
| `gmaps-*.html` | Delapan demo Google Maps: peta, marker, rute, geocoding, dan geolocation |
| `vector-map.html` | Peta dunia jsVectorMap lokal dengan region dan marker interaktif |
| `projects.html` | Kanban proyek, penambahan proyek, perubahan status |
| `calendar.html` | Navigasi bulan, penambahan agenda, detail agenda |
| `widget-chart.html`, `widget-data.html` | Mini grafik SVG, KPI, progres, heatmap, kalender mini |
| `chat.html` | Percakapan demo lokal, pencarian kontak dan pesan |
| `portfolio.html`, `blog.html` | Galeri karya dengan filter; artikel, pencarian, detail dan pagination |
| `email-inbox.html`, `email-compose.html`, `email-read.html` | Kotak surat demo, folder, baca pesan, balas/forward, draft dan kirim lokal |
| `avatar.html`, `card.html`, `modal.html`, `tabs.html` | Variasi komponen lanjutan dengan Bootstrap 5 dan tema BRUTAL. |
| `sweet-alert.html`, `toastr.html` | Dialog dan notifikasi demo dengan bundle lokal |
| `empty-state.html`, `multiple-upload.html` | Empty state SVG dan pratinjau file Dropzone tanpa upload server |
| `profile.html` | Edit profil, preferensi tampilan ringkas, reset data demo |
| `auth-login.html` | Antarmuka login demo |
| `auth-register.html` | Antarmuka register demo |
| `auth-forgot-password.html` | Simulasi permintaan tautan reset password |
| `auth-reset-password.html` | Validasi password baru dan konfirmasi, tanpa menyimpan password |
| `subscribe.html` | Landing page newsletter dengan ilustrasi SVG dan pendaftaran demo lokal |
| `create-post.html`, `posts.html` | Editor Quill, cover, draft/publikasi lokal, pencarian dan filter post |
| `contact.html` | Form kontak dan informasi studio contoh dalam dua kolom |
| `multilevel.html` | Halaman tujuan demo menu sidebar tiga tingkat |
| `invoice.html` | Invoice contoh dengan stylesheet cetak/PDF |
| `pricing.html` | Contoh paket harga |
| `blank.html` | Starting point halaman baru |
| `errors-403.html`, `errors-404.html`, `errors-500.html`, `errors-503.html` | Halaman status dengan ilustrasi SVG; konfigurasi server diperlukan untuk routing error aktual |
| `docs.html` | Dokumentasi penggunaan dan kustomisasi di browser |

## Struktur dan kustomisasi

```text
assets/css/theme.css       Token, override komponen Bootstrap, layout responsif
assets/css/workspace.css   Style halaman Phase 1 (dimuat hanya di 8 halaman terkait)
assets/css/advanced.css    Style delapan halaman Komponen Lanjutan Phase 2
assets/css/forms.css       Style halaman Forms Phase 3
assets/css/tables.css      Style halaman Tables Phase 4
assets/css/charts.css      Style halaman Charts Phase 5
assets/css/icons.css       Style lima halaman Icons Phase 6
assets/css/media.css       Style lima halaman Media Phase 7
assets/css/maps.css        Style sembilan halaman Maps Phase 8
assets/css/special.css     Style halaman khusus, post, kontak, dan error Phase 9
assets/js/app.js           Interaksi demo dan penyimpanan lokal
assets/js/workspace.js     Interaksi chat, portfolio, blog, widget, dan email lokal
assets/js/advanced.js      Interaksi modal, notifikasi, empty state, dan pratinjau file
assets/js/forms.js         Interaksi Select2, Quill, validasi, dan wizard
assets/js/tables.js        Sorting, DataTables, ekspor, dan editor sel
assets/js/charts.js        Inisialisasi enam library grafik dan responsivitasnya
assets/js/icons.js         Pencarian dan salin kode ikon
assets/js/feather-data.js  Data SVG Feather resmi, dihasilkan generator
assets/js/media.js         Inisialisasi lightbox dan Owl Carousel
assets/js/maps.js          Google Maps, Routes, geocoding, geolocation, dan jsVectorMap
assets/js/special.js       Subscribe, post, kontak, dan tombol error Phase 9
assets/js/sidebar-config.js Sumber tunggal menu sidebar dan pencarian
assets/js/sidebar.js       Renderer, collapse, drawer, dan fokus keyboard
assets/js/sidebar-icons.js SVG lokal, dihasilkan dari ICONS di generator
assets/bundles/            Bundle lokal komponen, editor, tabel, grafik, ikon, dan media (lihat README di dalamnya)
assets/img/favicon.svg    Logo SVG lokal
assets/img/workspace/     Ilustrasi SVG karya dan artikel lokal
bootstrap-5.3.8/           Source Bootstrap asli dari pengguna (tidak diubah)
scripts/build.py          Generator HTML dengan shell navbar/sidebar bersama
scripts/format_html.py    Formatter HTML dengan pemeriksaan struktur dan konten
scripts/workspace_pages.py Konten, data dan ilustrasi delapan halaman Phase 1
scripts/advanced_pages.py Konten delapan halaman Komponen Lanjutan Phase 2
scripts/form_pages.py     Konten overview dan empat halaman Forms Phase 3
scripts/table_pages.py    Konten overview dan empat halaman Tables Phase 4
scripts/chart_pages.py    Konten overview dan enam halaman Charts Phase 5
scripts/icon_pages.py     Konten lima halaman Icons Phase 6
scripts/media_pages.py    Konten lima halaman Media Phase 7
scripts/map_pages.py      Konten sembilan halaman Maps Phase 8
scripts/docs_page.py      Direktori halaman dan versi library untuk docs.html
scripts/special_pages.py  Konten halaman khusus dan error Phase 9
tests/template.spec.js    Pengujian alur pengguna dengan Playwright
tests/workspace.spec.js   Pengujian interaksi Phase 1
tests/advanced.spec.js    Pengujian interaksi dan bundle Phase 2
tests/forms.spec.js       Pengujian alur form Phase 3
tests/tables.spec.js      Pengujian alur tabel dan ekspor Phase 4
tests/charts.spec.js      Pengujian keenam library grafik Phase 5
tests/icons.spec.js       Pengujian aset, pencarian, dan salin kode ikon Phase 6
tests/media.spec.js       Pengujian lightbox, carousel, dan timeline Phase 7
tests/maps.spec.js        Pengujian placeholder, peta vektor, dan interaksi Maps Phase 8
tests/final.spec.js       Audit judul, breadcrumb, dokumentasi, dan reset password
tests/special.spec.js     Pengujian subscribe, post, kontak, error, dan menu bertingkat
```

Ubah token `--neo-*` di `assets/css/theme.css` untuk mengganti warna, shadow, dan border. File ini harus dimuat **setelah** Bootstrap CSS. Komponen tetap menggunakan kelas Bootstrap seperti `.btn`, `.card`, `.form-control`, `.modal`, `.row`, dan `.col-md-*`.

HTML berisi konten halaman; navigasi dirender oleh JavaScript lokal, tanpa fetch/SPA atau proses build saat runtime. Salin `blank.html` untuk halaman baru, ubah `data-page`, lalu daftarkan halaman di `assets/js/sidebar-config.js`. Untuk memperbarui konten serta topbar/footer inline, edit `scripts/build.py`. Instal dependensi khusus build sekali, lalu jalankan generator:

```bash
python3 -m pip install -r requirements-build.txt
npm run build
```

**Build menimpa 92 file HTML hasil generate.** Generator otomatis memberi indentasi dan baris yang mudah dibaca pada semua halaman, termasuk contoh markup serta data JSON, lalu memeriksa struktur dan kontennya sebelum menulis file. Simpan perubahan permanen di generator, atau gunakan file HTML baru dengan nama berbeda. Build tidak menimpa konfigurasi menu. Dependensi `lxml` hanya diperlukan saat build; halaman statis tetap dapat dibuka tanpa instalasi Python package.

## Fondasi sidebar — Phase 0

`sidebar-config.js` berisi array `{ group, items }`. Item halaman memakai `{ page, label, icon }`; item grup memakai `{ id, label, icon, children }`. Nilai `page` sama dengan `data-page` dan nama HTML tanpa ekstensi. Gunakan ID grup yang unik. Array harus valid JSON karena generator juga membacanya untuk judul halaman.

Semua 92 halaman memakai `<div id="sidebar-root"></div>`. Urutan script dasar: Bootstrap bundle → `sidebar-config.js` → `sidebar-icons.js` → `sidebar.js` → `app.js`. Halaman Phase 1 menambah `workspace.js`; Phase 2 `advanced.js`; Phase 3 `forms.js`; Phase 4 `tables.js`; Phase 5 `charts.js`; Phase 6 `icons.js`; halaman Phase 7 yang memerlukan plugin menambah `media.js`; halaman Phase 8 menambah `maps.js`; dan halaman Phase 9 menambah `special.js`. Bundle lain hanya dimuat pada halaman demo yang memerlukannya. Menambah atau mengganti item menu langsung mengubah sidebar dan pencarian pada semua halaman tanpa build ulang. Rebuild diperlukan jika judul/breadcrumb HTML juga berubah.

Sidebar membuka grup halaman aktif secara otomatis. Di mobile, drawer mendukung backdrop, Escape, focus trap, dan pengembalian fokus. Halaman autentikasi, subscribe, dan error menggunakan drawer yang sama melalui tombol menu pada semua ukuran layar agar layout standalone tetap nyaman.

Topbar/footer aplikasi tetap inline dari generator. Utilitas tersedia: `.stat-card`, `.timeline` (berisi `.timeline-item`), `.map-card` (dengan `.map-viewport`), `.gallery-grid`, dan `.code-block`. Token tema yang berlaku adalah `--neo-*`; tidak ada framework CSS tambahan.

Keputusan pemisahan form, tabel, dan grafik di `SIDEBAR-CHECKLIST.md` sudah diterapkan pada Phase 3–5. `404.html` telah dipindahkan menjadi `errors-404.html`; seluruh tautan aplikasi memakai nama baru.

## Data dan integrasi backend

- Proyek, checklist, agenda, profil, mode ringkas, chat (`brutal.chat`), dan email (`brutal.mail`) memakai localStorage. Data hanya di browser/origin yang sama. Jika storage diblokir, chat tetap berjalan dalam memori dengan notifikasi; email demo tidak akan berpindah halaman saat simpan gagal.
- Subscribe menyimpan alamat contoh pada `brutal.subscribers`; form kontak hanya menampilkan pratinjau dan tidak mengirim pesan. Post disimpan di `brutal.posts` dengan cover gambar maksimal 500 KB; Quill dipakai untuk menulis, tetapi isi disimpan dan ditampilkan sebagai teks. Status terbit/draft hanya simulasi.
- Tombol Kirim email hanya menambahkan pesan ke folder Terkirim di browser; tidak ada layanan email, penerima sungguhan, atau backend. Toolbar Bold/Italic/Underline pada compose adalah contoh visual, belum mengubah teks.
- Dialog SweetAlert2 dan notifikasi Toastr adalah demo lokal. Dropzone menampilkan thumbnail dan progres pembacaan file di browser; antrean upload dimatikan, sehingga file tidak dikirim atau disimpan di server.
- Statistik dan angka chart adalah **data ilustratif**, bukan agregasi proyek demo. Dropdown grafik menukar dataset contoh.
- Form, editor Quill, wizard, login, register, reset password, dan pilihan paket merupakan demonstrasi frontend. Tidak ada akun, sesi autentikasi, email, pembayaran, atau upload server. Password tidak disimpan.
- CSV mengikuti filter tabel, mengutip nilai dan menetralkan prefix formula spreadsheet pada input pengguna.
- Hubungkan handler submit/data di `assets/js/app.js` ke API pilihanmu. Validasi server, otorisasi, autentikasi, dan penyimpanan permanen perlu diimplementasikan di backend.
- Server development hanya untuk preview. Untuk deployment statis, salin HTML, `assets/`, dan file Bootstrap `dist/css/bootstrap.min.css` serta `dist/js/bootstrap.bundle.min.js` (beserta sourcemap jika dibutuhkan). Folder source Bootstrap lainnya tidak harus dideploy.

## Google Maps dan API key

Buka salah satu halaman `gmaps-*.html`, lalu masukkan API key browser pada panel **Hubungkan Google Maps**. Aktifkan billing dan Maps JavaScript API di Google Cloud; demo rute juga memerlukan Routes API, sedangkan pencarian alamat memerlukan Geocoding API. Batasi key ke domain situs dan API yang dipakai. Key disimpan di `localStorage` browser (`brutal.mapsApiKey`) agar berlaku lintas delapan halaman; tombol **Hapus key tersimpan** menghapusnya. Jangan memasukkan key yang tidak dibatasi. Tanpa key, halaman menampilkan placeholder dan tidak memuat request Google. Geolocation memerlukan HTTPS atau `localhost` serta izin browser.

Key demo yang diberikan untuk Phase 8 berhasil memuat peta dasar dan rute pada pengujian lokal. Permintaan geocoding ditolak oleh konfigurasi key saat ini; aktifkan Geocoding API dan periksa pembatasan API key di Google Cloud untuk menjalankan demo pencarian alamat. Key tidak disimpan di repository.

Rute menggunakan Routes Library resmi. Di Advanced Route, mode via Cirebon dan alternatif Jakarta–Bandung terpisah karena Google tidak menyediakan alternatif ketika request memuat waypoint. `vector-map.html` memakai jsVectorMap dan data dunia lokal tanpa key atau layanan eksternal.

## Kontribusi dan kredit

Nama halaman menggunakan huruf kecil dan tanda hubung (`lowercase-kebab-case.html`); nilai `data-page` dan item `page` di `assets/js/sidebar-config.js` sama dengan nama file tanpa ekstensi. Edit konten permanen melalui `scripts/*_pages.py` atau `scripts/build.py`, lalu jalankan `npm run build` dan `npm test`. Direktori 92 halaman dan versi library tersedia di `docs.html`; lisensi setiap bundle ada di `assets/bundles/README.md`.

BRUTAL. dibuat dengan [Bootstrap 5.3.8](https://getbootstrap.com/) (MIT). Library pihak ketiga dan kredit sumbernya tercatat di [daftar bundle](assets/bundles/README.md). Ilustrasi dan ikon antarmuka khusus BRUTAL. dibuat untuk proyek ini. Otika dipakai sebagai acuan cakupan halaman dan pola navigasi; tidak ada aset Otika yang disalin.

## Analisis acuan Otika

Referensi lokal yang dianalisis: `/mnt/C80A6A9E0A6A88F0/Templete Web/otika.namikulo.com`.

Otika menyediakan admin shell, dashboard, widget, UI dasar/advanced, forms, tables, chart plugins, apps, auth, dan utility pages, dengan fondasi Bootstrap 4 dan jQuery. BRUTAL. mengambil **cakupan dan pola navigasi** sebagai acuan; markup, CSS tema, ikon, dan interaksinya dibuat ulang untuk Bootstrap 5.3.8. Tidak menyalin atau memuat aset Otika.

Komponen inti memiliki 16 halaman terpisah di bawah dropdown Komponen UI. Delapan halaman Widgets, Apps, dan Email berada di dropdown WORKSPACE; delapan halaman Phase 2 berada di dropdown Komponen Lanjutan. Lima demo form berada di dropdown Form & Validasi; lima demo tabel berada di dropdown Tabel Data; enam library grafik berada di dropdown Grafik & Widget; lima koleksi ikon berada di dropdown Ikon. Grup Media menyediakan dua galeri, dua carousel, dan timeline. Grup Maps menyediakan delapan demo Google Maps dan peta vektor dunia. Grup Halaman berisi subscribe, empat error, kontak, post, dan demo menu tiga tingkat. Versi ini belum mencakup pengiriman chat/email nyata atau upload server. Tambahkan dependency saat kebutuhan konkret muncul; pin versi dan muat hanya pada halaman yang memakainya.

## Verifikasi

```bash
npm install
npm test
```

Tes menggunakan Chrome lokal di `/usr/bin/google-chrome`. Override dengan `CHROME_PATH=/path/to/chrome npm test`. Playwright hanya dependency development. Sebanyak 60 tes mencakup 92 halaman pada desktop/mobile, aset dan error JavaScript, sidebar, akses `file://`, seluruh fase komponen, form, tabel, grafik, media, peta, halaman khusus, reset password, dan dokumentasi. Audit Lighthouse Accessibility pada 11 halaman sampel mobile menghasilkan skor 92–100; amCharts 4 mendapat 92 karena kontrol yang dibuat library tersebut.

Bootstrap memiliki lisensi MIT; lisensi aslinya tetap ada di `bootstrap-5.3.8/LICENSE` dan `assets/BOOTSTRAP-LICENSE`.
