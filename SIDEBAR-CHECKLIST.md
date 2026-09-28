# 📋 Checklist Sidebar Template BRUTAL. (Neobrutalism)

> **Sumber referensi**: Template Otika (`otika.namikulo.com`) — Bootstrap Admin Template
> **Project**: Neo-brutalism template web (`/home/geats/Project Pribadi/neo-brutalism-template-web`)
> **Tanggal analisis**: 27 September 2026

---

## 🎯 Ringkasan

> **Audit Phase 0 — 27 September 2026:** terdapat **32 file HTML aktual** dan semuanya terdaftar di konfigurasi navigasi bersama. Sebanyak 29 memenuhi entri target di tabel berikut; 3 halaman pendukung adalah `components.html`, `blank.html`, dan `docs.html`. Penomoran tabel mencapai 86 entri (termasuk demo multilevel), bukan 74. Jumlah lama 41 halaman belum tersedia telah dikoreksi menjadi 57 entri target. `auth-reset-password.html` ternyata belum tersedia.

> **Audit Phase 1 — 28 September 2026:** delapan halaman Widgets, Apps, dan Email telah ditambahkan. Kini terdapat **40 file HTML aktual**: 37 entri target dan 3 halaman pendukung; 49 entri target masih menunggu phase berikutnya.

> **Audit Phase 2 — 28 September 2026:** delapan halaman Komponen Lanjutan telah ditambahkan. Kini terdapat **48 file HTML aktual**: 45 entri target dan 3 halaman pendukung; 41 entri target masih menunggu phase berikutnya.

> **Audit Phase 3 — 28 September 2026:** showcase form dasar dipindah ke `basic-form.html`, `forms.html` menjadi overview, dan empat halaman form lanjutan ditambahkan. Kini terdapat **53 file HTML aktual**: 49 entri target dan 4 halaman pendukung; 37 entri target masih menunggu phase berikutnya.

> **Audit Phase 4 — 28 September 2026:** showcase tabel proyek dipindah ke `basic-table.html`, `tables.html` menjadi overview, dan empat halaman tabel lanjutan ditambahkan. Kini terdapat **58 file HTML aktual**: 53 entri target dan 5 halaman pendukung; 33 entri target masih menunggu phase berikutnya.

| Status | Jumlah |
| --- | --- |
| ✅ Entri target dengan halaman tersedia | 53 |
| ❌ Entri target belum tersedia | 33 (termasuk demo multilevel) |
| 🔁 Keputusan struktur belum diselesaikan | 0 |
| **Total entri target pada tabel bernomor** | **86** |
| File HTML aktual, termasuk 5 halaman pendukung | 58 |

---

## 📊 Struktur Sidebar Otika → Sidebar BRUTAL.

Tabel berikut memetakan **86 entri target**. Sidebar BRUTAL. memiliki **4 grup utama** dan **58 tautan halaman** dari `assets/js/sidebar-config.js`. Grup/halaman phase berikutnya baru ditautkan setelah tersedia.

---

## 🟦 MAIN (Workspace)

### Dashboard
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 1 | Dashboard | `index.html` | `index.html` | ✅ Ada |
| 2 | Projects / Workspace | `projects.html` (di Otika bukan menu utama) | `projects.html` | ✅ Ada |

### Widgets
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 3 | Chart Widgets | `widget-chart.html` | `widget-chart.html` | ✅ Phase 1 |
| 4 | Data Widgets | `widget-data.html` | `widget-data.html` | ✅ Phase 1 |

> **Catatan**: Dropdown Widgets sudah tersedia. Showcase grafik `charts.html` tetap terpisah sampai Phase 5.

### Apps
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 5 | Chat | `chat.html` | `chat.html` | ✅ Phase 1 |
| 6 | Portfolio | `portfolio.html` | `portfolio.html` | ✅ Phase 1 |
| 7 | Blog | `blog.html` | `blog.html` | ✅ Phase 1 |
| 8 | Calendar | `calendar.html` | `calendar.html` | ✅ Ada |

### Email
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 9 | Inbox | `email-inbox.html` / `mail-inbox.html` | `email-inbox.html` | ✅ Phase 1 |
| 10 | Compose | `email-compose.html` | `email-compose.html` | ✅ Phase 1 |
| 11 | Read | `email-read.html` | `email-read.html` | ✅ Phase 1 |

---

## 🟪 UI ELEMENTS (Building Blocks)

### Basic Components
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 12 | Alert | `alert.html` | `alert.html` | ✅ Ada |
| 13 | Badge | `badge.html` | `badge.html` | ✅ Ada |
| 14 | Breadcrumb | `breadcrumb.html` | `breadcrumb.html` | ✅ Ada |
| 15 | Buttons | `buttons.html` | `buttons.html` | ✅ Ada |
| 16 | Collapse | `collapse.html` | `collapse.html` | ✅ Ada |
| 17 | Dropdown | `dropdown.html` | `dropdown.html` | ✅ Ada |
| 18 | Checkbox & Radios | `checkbox-and-radio.html` | `checkbox-and-radio.html` | ✅ Ada |
| 19 | List Group | `list-group.html` | `list-group.html` | ✅ Ada |
| 20 | Media Object | `media-object.html` | `media-object.html` | ✅ Ada |
| 21 | Navbar | `navbar.html` | `navbar.html` | ✅ Ada |
| 22 | Pagination | `pagination.html` | `pagination.html` | ✅ Ada |
| 23 | Popover | `popover.html` | `popover.html` | ✅ Ada |
| 24 | Progress | `progress.html` | `progress.html` | ✅ Ada |
| 25 | Tooltip | `tooltip.html` | `tooltip.html` | ✅ Ada |
| 26 | Flags | `flags.html` | `flags.html` | ✅ Ada |
| 27 | Typography | `typography.html` | `typography.html` | ✅ Ada |

### Advanced Components
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 28 | Avatar | `avatar.html` | `avatar.html` | ✅ Phase 2 |
| 29 | Card | `card.html` | `card.html` | ✅ Phase 2 |
| 30 | Modal | `modal.html` | `modal.html` | ✅ Phase 2 |
| 31 | Sweet Alert | `sweet-alert.html` | `sweet-alert.html` | ✅ Phase 2 |
| 32 | Toastr | `toastr.html` | `toastr.html` | ✅ Phase 2 |
| 33 | Empty State | `empty-state.html` | `empty-state.html` | ✅ Phase 2 |
| 34 | Multiple Upload | `multiple-upload.html` | `multiple-upload.html` | ✅ Phase 2 |
| 35 | Pricing | `pricing.html` | `pricing.html` | ✅ Ada |
| 36 | Tabs | `tabs.html` | `tabs.html` | ✅ Phase 2 |

---

## 🟨 OTIKA (Forms / Tables / Charts / Icons)

### Forms
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 37 | Basic Form | `basic-form.html` | `basic-form.html` | ✅ Phase 3 |
| 38 | Advanced Form | `forms-advanced-form.html` | `forms-advanced-form.html` | ✅ Phase 3 |
| 39 | Editor (WYSIWYG) | `forms-editor.html` | `forms-editor.html` | ✅ Phase 3 |
| 40 | Validation | `forms-validation.html` | `forms-validation.html` | ✅ Phase 3 |
| 41 | Form Wizard | `form-wizard.html` | `form-wizard.html` | ✅ Phase 3 |

### Tables
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 42 | Basic Tables | `basic-table.html` | `basic-table.html` | ✅ Phase 4 |
| 43 | Advanced Table | `advance-table.html` | `advance-table.html` | ✅ Phase 4 |
| 44 | Datatable | `datatables.html` | `datatables.html` | ✅ Phase 4 |
| 45 | Export Table | `export-table.html` | `export-table.html` | ✅ Phase 4 |
| 46 | Editable Table | `editable-table.html` | `editable-table.html` | ✅ Phase 4 |

### Charts
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 47 | amChart | `chart-amchart.html` | — | ❌ Belum |
| 48 | apexchart | `chart-apexchart.html` | — | ❌ Belum |
| 49 | eChart | `chart-echart.html` | — | ❌ Belum |
| 50 | Chartjs | `chart-chartjs.html` | `charts.html` | ✅ Showcase grafik dasar tersedia (SVG); migrasi dan integrasi Chart.js pada Phase 5 |
| 51 | Sparkline | `chart-sparkline.html` | — | ❌ Belum |
| 52 | Morris | `chart-morris.html` | — | ❌ Belum |

### Icons
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 53 | Font Awesome | `icon-font-awesome.html` | — | ❌ Belum |
| 54 | Material Design | `icon-material.html` | — | ❌ Belum |
| 55 | Ion Icons | `icon-ionicons.html` | — | ❌ Belum |
| 56 | Feather Icons | `icon-feather.html` | — | ❌ Belum |
| 57 | Weather Icon | `icon-weather-icon.html` | — | ❌ Belum |

---

## 🟧 MEDIA

### Gallery
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 58 | Light Gallery | `light-gallery.html` | — | ❌ Belum |
| 59 | Gallery 2 | `gallery1.html` | — | ❌ Belum |

### Sliders
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 60 | Bootstrap Carousel | `carousel.html` | — | ❌ Belum |
| 61 | Owl Carousel | `owl-carousel.html` | — | ❌ Belum |

### Timeline
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 62 | Timeline | `timeline.html` | — | ❌ Belum |

---

## 🟫 MAPS

### Google Maps
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 63 | Advanced Route | `gmaps-advanced-route.html` | — | ❌ Belum |
| 64 | Draggable Marker | `gmaps-draggable-marker.html` | — | ❌ Belum |
| 65 | Geocoding | `gmaps-geocoding.html` | — | ❌ Belum |
| 66 | Geolocation | `gmaps-geolocation.html` | — | ❌ Belum |
| 67 | Marker | `gmaps-marker.html` | — | ❌ Belum |
| 68 | Multiple Marker | `gmaps-multiple-marker.html` | — | ❌ Belum |
| 69 | Route | `gmaps-route.html` | — | ❌ Belum |
| 70 | Simple | `gmaps-simple.html` | — | ❌ Belum |

### Vector Map
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 71 | Vector Map | `vector-map.html` | — | ❌ Belum |

---

## 🟥 PAGES

### Auth
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 72 | Login | `auth-login.html` | `auth-login.html` | ✅ Ada |
| 73 | Register | `auth-register.html` | `auth-register.html` | ✅ Ada |
| 74 | Forgot Password | `auth-forgot-password.html` | `auth-forgot-password.html` | ✅ Ada |
| 75 | Reset Password | `auth-reset-password.html` | — | ❌ Belum; audit Phase 0 mengoreksi status lama |
| 76 | Subscribe | `subscribe.html` | — | ❌ Belum |

### Errors
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 77 | 403 | `errors-403.html` | — | ❌ Belum |
| 78 | 404 | `errors-404.html` | `errors-404.html` | ✅ Rename selesai pada Phase 0 |
| 79 | 500 | `errors-500.html` | — | ❌ Belum |
| 80 | 503 | `errors-503.html` | — | ❌ Belum |

### Other Pages
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 81 | Create Post | `create-post.html` | — | ❌ Belum |
| 82 | Posts | `posts.html` | — | ❌ Belum |
| 83 | Profile | `profile.html` | `profile.html` | ✅ Ada |
| 84 | Contact | `contact.html` | — | ❌ Belum |
| 85 | Invoice | `invoice.html` | `invoice.html` | ✅ Ada |

### Multilevel
| # | Item | File Otika | File BRUTAL. | Status |
| --- | --- | --- | --- | --- |
| 86 | Multilevel (nested menu demo) | inline di `index.html` | — | ❌ Belum (demo nested dropdown) |

---

## ✅ Yang Sudah Tersedia di BRUTAL. (Highlight)

```
✅ index.html              ✅ navbar.html            ✅ pricing.html
✅ alert.html              ✅ pagination.html        ✅ profile.html
✅ auth-forgot-password.html ✅ popover.html          ✅ progress.html
✅ auth-login.html         ✅ projects.html          ✅ tables.html
✅ auth-register.html      ✅ typography.html        ✅ tooltip.html
❌ auth-reset-password.html ✅ forms.html            ✅ docs.html
✅ badge.html              ✅ charts.html            ✅ components.html
✅ breadcrumb.html         ✅ flags.html             ✅ blank.html
✅ buttons.html            ✅ invoice.html           ✅ calendar.html
✅ checkbox-and-radio.html ✅ list-group.html        ✅ errors-404.html
✅ collapse.html           ✅ media-object.html      ✅ dropdown.html
✅ widget-chart.html       ✅ widget-data.html       ✅ chat.html
✅ portfolio.html          ✅ blog.html              ✅ email-inbox.html
✅ email-compose.html      ✅ email-read.html
✅ avatar.html             ✅ card.html              ✅ modal.html
✅ sweet-alert.html        ✅ toastr.html            ✅ empty-state.html
✅ multiple-upload.html    ✅ tabs.html
✅ basic-form.html         ✅ forms-advanced-form.html
✅ forms-editor.html       ✅ forms-validation.html
✅ form-wizard.html
✅ basic-table.html        ✅ advance-table.html
✅ datatables.html         ✅ export-table.html
✅ editable-table.html
```

**Total: 58 file HTML aktual; 53 masuk pemetaan target dan 5 halaman pendukung.** `forms.html` dan `tables.html` adalah overview pendukung. Baris reset password tetap belum tersedia.

---

## ❌ Yang Perlu Dibuat (33 entri target tersisa)

### 🔴 Prioritas Tinggi (inti dashboard)

### 🟢 Prioritas Rendah (visual & library)
- [ ] `chart-amchart.html` — amCharts library
- [ ] `chart-apexchart.html` — ApexCharts library
- [ ] `chart-echart.html` — ECharts library
- [ ] `chart-sparkline.html` — Sparkline charts
- [ ] `chart-morris.html` — Morris.js charts
- [ ] `icon-font-awesome.html` — Font Awesome showcase
- [ ] `icon-material.html` — Material Icons
- [ ] `icon-ionicons.html` — Ionicons
- [ ] `icon-feather.html` — Feather Icons
- [ ] `icon-weather-icon.html` — Weather Icons
- [ ] `light-gallery.html` — Lightbox gallery
- [ ] `gallery1.html` — Gallery alternatif
- [ ] `carousel.html` — Bootstrap carousel demo
- [ ] `owl-carousel.html` — Owl Carousel demo
- [ ] `timeline.html` — Timeline component

### ⚪ Optional / Maps (butuh API key)
- [ ] `gmaps-simple.html` — Google Maps simple
- [ ] `gmaps-marker.html` — Google Maps marker
- [ ] `gmaps-multiple-marker.html` — Multiple markers
- [ ] `gmaps-route.html` — Direction route
- [ ] `gmaps-advanced-route.html` — Advanced route
- [ ] `gmaps-draggable-marker.html` — Draggable marker
- [ ] `gmaps-geocoding.html` — Geocoding search
- [ ] `gmaps-geolocation.html` — User geolocation
- [ ] `vector-map.html` — Vector map (jvectormap)

### 🟤 Halaman khusus
- [ ] `subscribe.html` — Subscribe page
- [ ] `errors-403.html` — Error 403
- [x] `errors-404.html` — Error 404 (rename selesai pada Phase 0)
- [ ] `auth-reset-password.html` — Form reset password; belum tersedia saat audit
- [ ] `errors-500.html` — Error 500
- [ ] `errors-503.html` — Error 503
- [ ] `create-post.html` — Buat post
- [ ] `posts.html` — Daftar post
- [ ] `contact.html` — Halaman kontak
- [ ] **Nested multilevel menu demo** — Submenu 3-level di sidebar

---

## ✅ Keputusan Struktur Final — Phase 0

| Item | Keputusan | Waktu pelaksanaan |
| --- | --- | --- |
| `404.html` → `errors-404.html` | Rename; seluruh tautan aplikasi dan generator memakai nama baru | ✅ Selesai Phase 0; tidak menyisakan alias |
| `forms.html` | Pindah showcase dasar ke `basic-form.html`, jadikan `forms.html` overview, tambah 4 halaman lanjutan | ✅ Selesai Phase 3 (Opsi A) |
| `tables.html` | Pindah showcase ke `basic-table.html`, jadikan `tables.html` overview, tambah 4 halaman lanjutan | ✅ Selesai Phase 4 |
| `charts.html` | Pindah showcase ke `chart-chartjs.html`, jadikan `charts.html` overview, tambah demo per library | Diputuskan; implementasi pada Phase 5. Grafik saat ini masih SVG, belum Chart.js |

### Hasil fondasi Phase 0

- [x] Sidebar semua 32 halaman dirender oleh `assets/js/sidebar.js` dari `assets/js/sidebar-config.js`.
- [x] Pencarian memakai konfigurasi yang sama; menu aktif berasal dari `data-page`.
- [x] Bootstrap Collapse menangani submenu; drawer menangani backdrop, Escape, focus trap, dan fokus kembali ke pemicu.
- [x] Halaman auth dan error menggunakan sidebar yang sama dalam drawer melalui tombol menu, termasuk desktop.
- [x] Topbar/footer aplikasi tetap inline melalui generator. Modul terpisah tidak diperlukan pada phase ini.
- [x] `.stat-card`, `.timeline`, `.map-card`, `.gallery-grid`, dan `.code-block` tersedia; token aktual `--neo-*` tetap menjadi acuan.
- [x] Konvensi library lokal didokumentasikan di `assets/bundles/README.md`; ikon SVG lokal yang ada dipertahankan.
- [x] `npm run build` berhasil; **12 tes browser lulus**, termasuk semua halaman pada 1440/390/320 px, konsistensi sidebar, tautan, drawer, dan akses langsung `file://`.

**Cakupan:** Phase 0 selesai. Pemisahan konten form/tabel/grafik dan halaman baru untuk phase lain belum dieksekusi.

### Hasil Phase 1 — Workspace Inti

- [x] Delapan halaman Widgets, Apps, dan Email tersedia di dropdown WORKSPACE dengan breadcrumb serta active state sidebar.
- [x] Widget grafik SVG, KPI/progres/heatmap/kalender mini, filter portfolio, pencarian dan pagination blog, chat, serta alur inbox–baca–compose/draft/terkirim memakai aset dan interaksi lokal.
- [x] Email/chat memakai data contoh tersimpan di browser; reset profil juga menghapus `brutal.chat` dan `brutal.mail`. Tidak ada pengiriman email sungguhan.
- [x] Grafik dan ilustrasi portfolio/blog memakai SVG lokal tanpa CDN atau library baru.
- [x] `npm run build` menghasilkan 40 halaman; **19 tes browser lulus** termasuk alur Phase 1 dan pemeriksaan seluruh halaman pada desktop/mobile.

### Hasil Phase 2 — Komponen Lanjutan

- [x] Delapan halaman Avatar, Card, Modal, Sweet Alert, Toastr, Empty State, Multiple Upload, dan Tabs tersedia di dropdown Komponen Lanjutan bersama Pricing.
- [x] SweetAlert2, Toastr/jQuery, dan Dropzone dimuat lokal hanya pada halaman demo masing-masing; versi, sumber, dan lisensi tercatat di `assets/bundles/README.md`.
- [x] Modal Bootstrap, notifikasi, daftar kosong, tab, serta pratinjau file memiliki interaksi demo. Dropzone tidak mengirim file ke server.
- [x] Generator tetap menghasilkan HTML berindentasi dan memeriksa struktur/konten sebelum menulis.
- [x] `npm run build` menghasilkan 48 halaman; **24 tes browser lulus**, termasuk demo Phase 2 dan regresi desktop/mobile seluruh template.

### Hasil Phase 3 — Forms

- [x] `forms.html` menjadi overview; `basic-form.html` berisi showcase form lama tanpa kehilangan interaksi.
- [x] Empat demo lanjutan tersedia pada dropdown Form & Validasi: Advanced Form (Select2), Editor (Quill Snow/Bubble), Validation (HTML5 + Bootstrap), dan Form Wizard (jQuery Steps).
- [x] Bundle plugin dipin dan dimuat lokal per halaman. Semua submit hanya menampilkan umpan balik di browser.
- [x] `npm run build` menghasilkan 53 halaman; **29 tes browser lulus**, termasuk demo Phase 3 dan regresi desktop/mobile seluruh template.

### Hasil Phase 4 — Tables

- [x] `tables.html` menjadi overview; `basic-table.html` berisi tabel proyek workspace lama dan dashboard kini menautkan halaman dasar tersebut.
- [x] Empat demo lanjutan tersedia di dropdown Tabel Data: sorting/variasi Bootstrap, DataTables, ekspor, dan editor sel.
- [x] DataTables, Buttons, JSZip, dan pdfMake disimpan lokal. Editor sel menggunakan JavaScript vanilla dengan validasi dan penyimpanan demo terpisah di localStorage.
- [x] `npm run build` menghasilkan 58 halaman; **34 tes browser lulus**, termasuk unduhan Excel/CSV/PDF, print, dan regresi desktop/mobile.

---

## 🗂️ Rekomendasi Struktur Sidebar BRUTAL. (Final)

```
📦 WORKSPACE
├── Dashboard                  → index.html         ✅
├── Proyek                     → projects.html      ✅
├── Kalender                   → calendar.html      ✅
├── Widgets                    → (dropdown aktif)
│   ├── Chart Widgets          → widget-chart.html  ✅
│   └── Data Widgets           → widget-data.html   ✅
├── Apps                       → (dropdown aktif)
│   ├── Chat                   → chat.html          ✅
│   ├── Portfolio              → portfolio.html     ✅
│   └── Blog                   → blog.html          ✅
└── Email                      → (dropdown aktif)
    ├── Inbox                  → email-inbox.html   ✅
    ├── Compose                → email-compose.html ✅
    └── Baca                   → email-read.html    ✅

🧱 BUILDING BLOCKS
├── Komponen UI                → (group, sudah ada)
│   └── 16 submenu             → ✅ semua ada
├── Komponen Lanjutan          → (dropdown aktif)
│   ├── Avatar                 → avatar.html        ✅
│   ├── Card                   → card.html          ✅
│   ├── Modal                  → modal.html         ✅
│   ├── Sweet Alert            → sweet-alert.html   ✅
│   ├── Toastr                 → toastr.html        ✅
│   ├── Empty State            → empty-state.html   ✅
│   ├── Multiple Upload        → multiple-upload.html ✅
│   ├── Tab                    → tabs.html          ✅
│   └── Pricing                → pricing.html       ✅
├── Form & Validasi            → (dropdown aktif)
│   ├── Semua form             → forms.html         ✅
│   ├── Form dasar             → basic-form.html    ✅
│   ├── Form lanjutan          → forms-advanced-form.html ✅
│   ├── Editor                 → forms-editor.html  ✅
│   ├── Validasi               → forms-validation.html ✅
│   └── Form Wizard            → form-wizard.html   ✅
├── Tabel Data                 → (dropdown aktif)
│   ├── Semua tabel            → tables.html        ✅
│   ├── Tabel dasar            → basic-table.html   ✅
│   ├── Tabel lanjutan         → advance-table.html ✅
│   ├── Datatable              → datatables.html    ✅
│   ├── Export Tabel           → export-table.html  ✅
│   └── Tabel Editable         → editable-table.html ✅
├── Grafik & Widget            → charts.html        ✅ (pemisahan Phase 5)
│   ├── Chart.js               → (merge)
│   ├── amChart                → chart-amchart.html ❌
│   ├── apexchart              → chart-apexchart.html ❌
│   ├── eChart                 → chart-echart.html  ❌
│   ├── Sparkline              → chart-sparkline.html ❌
│   └── Morris                 → chart-morris.html  ❌
└── Ikon                       → (group baru)
    ├── Font Awesome           → icon-font-awesome.html ❌
    ├── Material Design        → icon-material.html ❌
    ├── Ion Icons              → icon-ionicons.html ❌
    ├── Feather Icons          → icon-feather.html  ❌
    └── Weather Icon           → icon-weather-icon.html ❌

🖼️ MEDIA
├── Galeri                     → (group baru)
│   ├── Light Gallery          → light-gallery.html ❌
│   └── Gallery 2              → gallery1.html      ❌
├── Slider                     → (group baru)
│   ├── Bootstrap Carousel     → carousel.html      ❌
│   └── Owl Carousel           → owl-carousel.html  ❌
└── Timeline                   → timeline.html      ❌

🗺️ MAPS
├── Google Maps                → (group baru, 8 submenu) ❌
└── Vector Map                 → vector-map.html    ❌

📄 HALAMAN
├── Profil                     → profile.html       ✅
├── Invoice                    → invoice.html       ✅
├── Kontak                     → contact.html       ❌
├── Post                       → (group baru)
│   ├── Buat Post              → create-post.html   ❌
│   └── Daftar Post            → posts.html         ❌
├── Autentikasi                → (dropdown bersama) ✅
│   ├── Login                  → auth-login.html    ✅
│   ├── Daftar                 → auth-register.html ✅
│   ├── Lupa Password          → auth-forgot-password.html ✅
│   ├── Reset Password         → auth-reset-password.html ❌
│   └── Subscribe              → subscribe.html     ❌
├── Errors                     → (group baru)
│   ├── 403                    → errors-403.html    ❌
│   ├── 404                    → errors-404.html    ✅
│   ├── 500                    → errors-500.html    ❌
│   └── 503                    → errors-503.html    ❌
└── Multilevel                 → (nested dropdown demo) ❌

🚀 MULAI MEMBANGUN
├── Halaman Kosong             → blank.html         ✅
└── Dokumentasi                → docs.html          ✅
```

---

## 📈 Progress Tracker

```
Total entri target pada tabel: 86 (termasuk demo multilevel)
Total file HTML aktual: 58 (53 target + 5 halaman pendukung)
Sudah selesai: 53/86 (61.6%)
Belum selesai: 33/86 (38.4%)
```

### Checklist Ringkasan per Kategori

- [x] **Main**: Dashboard, Proyek, Kalender (3/8)
- [x] **Widgets**: 2/2
- [x] **Apps**: 4/4 (Chat, Portfolio, Blog, Calendar)
- [x] **Email**: 3/3
- [x] **Basic Components**: 16/16 ✅ **100%**
- [x] **Advanced Components**: 9/9 (termasuk Pricing)
- [x] **Forms**: 5/5 (overview di forms.html)
- [x] **Tables**: 5/5 (overview di tables.html)
- [ ] **Charts**: 1/6 showcase dasar SVG; integrasi library pada Phase 5
- [ ] **Icons**: 0/5
- [ ] **Gallery**: 0/2
- [ ] **Sliders**: 0/2
- [ ] **Timeline**: 0/1
- [ ] **Google Maps**: 0/8
- [ ] **Vector Map**: 0/1
- [ ] **Auth**: 3/5 (Reset Password dan Subscribe belum)
- [ ] **Errors**: 1/4 (404 via `errors-404.html`)
- [x] **Other Pages**: 2/5 (Profile, Invoice)
- [ ] **Nested multilevel demo**: 0/1

---

## 🛠️ Langkah Selanjutnya yang Disarankan

1. **Keputusan struktur selesai pada Phase 0**: pecah Form/Tabel/Chart pada Phase 3/4/5 sesuai tabel keputusan.
2. **Lanjutkan grup sidebar baru**: Widgets, Apps, Email, dan Advanced Components selesai; Icons, Media, Maps, Errors, Posts menyusul.
3. **Phase 1–4 selesai**: Workspace Inti, Advanced Components, Forms, dan Tables sudah aktif.
4. **Lanjut Phase 5**: pecah Charts sesuai keputusan Phase 0.
5. **Charts & Icons**: tergantung library mana yang akan di-include.
6. **Maps & Galeri**: optional, butuh API key (Google Maps) / library tambahan.
7. **Error pages**: cepat dibuat, tidak butuh library.

---

> 📌 **Setelah Phase 2**: Tambahkan halaman baru phase berikutnya ke `assets/js/sidebar-config.js` setelah tersedia. Sidebar dan pencarian seluruh halaman otomatis diperbarui. Jangan menambahkan sidebar inline per-file. Struktur akhir di atas masih mencakup target phase mendatang.
