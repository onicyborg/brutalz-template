# BRUTAL. — Neubrutalism Bootstrap Admin

Template admin statis berbahasa Indonesia, menggunakan **Bootstrap 5.3.8 lokal**. Desain original dengan border hitam, bayangan solid, palet lilac/mint/peach/yellow, dan layout responsif. Tidak membutuhkan CDN, font eksternal, atau bundler untuk dijalankan. jQuery dimuat lokal hanya pada demo Toastr, Select2, jQuery Steps, DataTables, Sparkline, dan Morris.js.

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
| `auth-forgot-password.html` | Simulasi permintaan reset password |
| `invoice.html` | Invoice contoh dengan stylesheet cetak/PDF |
| `pricing.html` | Contoh paket harga |
| `blank.html` | Starting point halaman baru |
| `errors-404.html` | Halaman error; konfigurasi server diperlukan untuk routing error aktual |
| `docs.html` | Dokumentasi penggunaan dan kustomisasi di browser |

## Struktur dan kustomisasi

```text
assets/css/theme.css       Token, override komponen Bootstrap, layout responsif
assets/css/workspace.css   Style halaman Phase 1 (dimuat hanya di 8 halaman terkait)
assets/css/advanced.css    Style delapan halaman Komponen Lanjutan Phase 2
assets/css/forms.css       Style halaman Forms Phase 3
assets/css/tables.css      Style halaman Tables Phase 4
assets/css/charts.css      Style halaman Charts Phase 5
assets/js/app.js           Interaksi demo dan penyimpanan lokal
assets/js/workspace.js     Interaksi chat, portfolio, blog, widget, dan email lokal
assets/js/advanced.js      Interaksi modal, notifikasi, empty state, dan pratinjau file
assets/js/forms.js         Interaksi Select2, Quill, validasi, dan wizard
assets/js/tables.js        Sorting, DataTables, ekspor, dan editor sel
assets/js/charts.js        Inisialisasi enam library grafik dan responsivitasnya
assets/js/sidebar-config.js Sumber tunggal menu sidebar dan pencarian
assets/js/sidebar.js       Renderer, collapse, drawer, dan fokus keyboard
assets/js/sidebar-icons.js SVG lokal, dihasilkan dari ICONS di generator
assets/bundles/            Bundle lokal komponen, editor, tabel, dan enam library grafik (lihat README di dalamnya)
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
tests/template.spec.js    Pengujian alur pengguna dengan Playwright
tests/workspace.spec.js   Pengujian interaksi Phase 1
tests/advanced.spec.js    Pengujian interaksi dan bundle Phase 2
tests/forms.spec.js       Pengujian alur form Phase 3
tests/tables.spec.js      Pengujian alur tabel dan ekspor Phase 4
tests/charts.spec.js      Pengujian keenam library grafik Phase 5
```

Ubah token `--neo-*` di `assets/css/theme.css` untuk mengganti warna, shadow, dan border. File ini harus dimuat **setelah** Bootstrap CSS. Komponen tetap menggunakan kelas Bootstrap seperti `.btn`, `.card`, `.form-control`, `.modal`, `.row`, dan `.col-md-*`.

HTML berisi konten halaman; navigasi dirender oleh JavaScript lokal, tanpa fetch/SPA atau proses build saat runtime. Salin `blank.html` untuk halaman baru, ubah `data-page`, lalu daftarkan halaman di `assets/js/sidebar-config.js`. Untuk memperbarui konten serta topbar/footer inline, edit `scripts/build.py`. Instal dependensi khusus build sekali, lalu jalankan generator:

```bash
python3 -m pip install -r requirements-build.txt
npm run build
```

**Build menimpa 64 file HTML hasil generate.** Generator otomatis memberi indentasi dan baris yang mudah dibaca pada semua halaman, termasuk contoh markup serta data JSON, lalu memeriksa struktur dan kontennya sebelum menulis file. Simpan perubahan permanen di generator, atau gunakan file HTML baru dengan nama berbeda. Build tidak menimpa konfigurasi menu. Dependensi `lxml` hanya diperlukan saat build; halaman statis tetap dapat dibuka tanpa instalasi Python package.

## Fondasi sidebar — Phase 0

`sidebar-config.js` berisi array `{ group, items }`. Item halaman memakai `{ page, label, icon }`; item grup memakai `{ id, label, icon, children }`. Nilai `page` sama dengan `data-page` dan nama HTML tanpa ekstensi. Gunakan ID grup yang unik. Array harus valid JSON karena generator juga membacanya untuk judul halaman.

Semua 64 halaman memakai `<div id="sidebar-root"></div>`. Urutan script dasar: Bootstrap bundle → `sidebar-config.js` → `sidebar-icons.js` → `sidebar.js` → `app.js`. Halaman Phase 1 menambah `workspace.js`; halaman Phase 2 menambah `advanced.js`; halaman Phase 3 menambah `forms.js`; halaman Phase 4 menambah `tables.js`; halaman Phase 5 menambah `charts.js`. Bundle lain hanya dimuat pada halaman demo yang memerlukannya. Menambah atau mengganti item menu langsung mengubah sidebar dan pencarian pada semua halaman tanpa build ulang. Rebuild diperlukan jika judul/breadcrumb HTML juga berubah.

Sidebar membuka grup halaman aktif secara otomatis. Di mobile, drawer mendukung backdrop, Escape, focus trap, dan pengembalian fokus. Halaman autentikasi/error menggunakan drawer yang sama melalui tombol menu pada semua ukuran layar agar layout standalone tetap nyaman.

Topbar/footer aplikasi tetap inline dari generator. Utilitas tersedia: `.stat-card`, `.timeline` (berisi `.timeline-item`), `.map-card` (dengan `.map-viewport`), `.gallery-grid`, dan `.code-block`. Token tema yang berlaku adalah `--neo-*`; tidak ada framework CSS tambahan.

Keputusan pemisahan form, tabel, dan grafik di `SIDEBAR-CHECKLIST.md` sudah diterapkan pada Phase 3–5. `404.html` telah dipindahkan menjadi `errors-404.html`; seluruh tautan aplikasi memakai nama baru.

## Data dan integrasi backend

- Proyek, checklist, agenda, profil, mode ringkas, chat (`brutal.chat`), dan email (`brutal.mail`) memakai localStorage. Data hanya di browser/origin yang sama. Jika storage diblokir, chat tetap berjalan dalam memori dengan notifikasi; email demo tidak akan berpindah halaman saat simpan gagal.
- Tombol Kirim email hanya menambahkan pesan ke folder Terkirim di browser; tidak ada layanan email, penerima sungguhan, atau backend. Toolbar Bold/Italic/Underline pada compose adalah contoh visual, belum mengubah teks.
- Dialog SweetAlert2 dan notifikasi Toastr adalah demo lokal. Dropzone menampilkan thumbnail dan progres pembacaan file di browser; antrean upload dimatikan, sehingga file tidak dikirim atau disimpan di server.
- Statistik dan angka chart adalah **data ilustratif**, bukan agregasi proyek demo. Dropdown grafik menukar dataset contoh.
- Form, editor Quill, wizard, login, register, reset password, dan pilihan paket merupakan demonstrasi frontend. Tidak ada akun, sesi autentikasi, email, pembayaran, atau upload server. Password tidak disimpan.
- CSV mengikuti filter tabel, mengutip nilai dan menetralkan prefix formula spreadsheet pada input pengguna.
- Hubungkan handler submit/data di `assets/js/app.js` ke API pilihanmu. Validasi server, otorisasi, autentikasi, dan penyimpanan permanen perlu diimplementasikan di backend.
- Server development hanya untuk preview. Untuk deployment statis, salin HTML, `assets/`, dan file Bootstrap `dist/css/bootstrap.min.css` serta `dist/js/bootstrap.bundle.min.js` (beserta sourcemap jika dibutuhkan). Folder source Bootstrap lainnya tidak harus dideploy.

## Analisis acuan Otika

Referensi lokal yang dianalisis: `/mnt/C80A6A9E0A6A88F0/Templete Web/otika.namikulo.com`.

Otika menyediakan admin shell, dashboard, widget, UI dasar/advanced, forms, tables, chart plugins, apps, auth, dan utility pages, dengan fondasi Bootstrap 4 dan jQuery. BRUTAL. mengambil **cakupan dan pola navigasi** sebagai acuan; markup, CSS tema, ikon, dan interaksinya dibuat ulang untuk Bootstrap 5.3.8. Tidak menyalin atau memuat aset Otika.

Komponen inti memiliki 16 halaman terpisah di bawah dropdown Komponen UI. Delapan halaman Widgets, Apps, dan Email berada di dropdown WORKSPACE; delapan halaman Phase 2 berada di dropdown Komponen Lanjutan. Lima demo form berada di dropdown Form & Validasi; lima demo tabel berada di dropdown Tabel Data; enam library grafik berada di dropdown Grafik & Widget. Versi ini belum mencakup pengiriman chat/email nyata, maps, carousel/gallery lanjutan, atau upload server. Tambahkan dependency saat kebutuhan konkret muncul; pin versi dan muat hanya pada halaman yang memakainya.

## Verifikasi

```bash
npm install
npm test
```

Tes menggunakan Chrome lokal di `/usr/bin/google-chrome`. Override dengan `CHROME_PATH=/path/to/chrome npm test`. Playwright hanya dependency development. Sebanyak 41 tes mencakup 64 halaman pada desktop/mobile, aset dan error JavaScript, sidebar, akses `file://`, interaksi workspace Phase 1–5, termasuk alur form, tabel, ekspor, dan enam library grafik.

Bootstrap memiliki lisensi MIT; lisensi aslinya tetap ada di `bootstrap-5.3.8/LICENSE` dan `assets/BOOTSTRAP-LICENSE`.
