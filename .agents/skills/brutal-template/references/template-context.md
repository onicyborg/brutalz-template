# Konteks implementasi BRUTAL.

Baca saat pertama memakai template; selanjutnya cukup bagian modul yang relevan. Path di dokumen ini relatif terhadap **root template**, bukan folder skill.

## Peta sumber

| Tanggung jawab | Sumber |
| --- | --- |
| Halaman siap dipakai | `*.html`; direktori di `docs.html#page-directory` |
| Shell, header/footer, auth dasar, dashboard, proyek, kalender, profil | `scripts/build.py` |
| Komponen UI dasar dan ikon pagination | `scripts/component_pages.py`, `scripts/ui_icons.py` |
| Workspace/apps/email | `scripts/workspace_pages.py`, `assets/js/workspace.js`, `assets/css/workspace.css` |
| Komponen lanjutan | `scripts/advanced_pages.py`, `assets/js/advanced.js`, `assets/css/advanced.css` |
| Form/tabel/grafik/media/peta/halaman khusus | `scripts/{form,table,chart,media,map,special}_pages.py` dan JS/CSS modul terkait |
| Ikon statis | `scripts/icon_pages.py`, `assets/js/icons.js`, `assets/js/feather-data.js` |
| Animated Icons | `scripts/animated_icon_pages.py`, `assets/js/animated-icons.js`, `assets/js/animated-icon-data.js` |
| Theme dan kontrol form | `assets/css/theme.css`, `assets/css/controls.css`, `assets/js/controls.js` |
| Navigasi | `assets/js/sidebar-config.js`, `assets/js/sidebar.js`, `assets/js/sidebar-icons.js` |
| State workspace | `assets/js/app.js`; drag/drop khusus di `assets/js/kanban.js` |
| Dokumentasi | `scripts/documentation_page.py`, `scripts/docs_page.py` → `docs.html`; setup di `README.md` |
| Build | `scripts/format_html.py`, `requirements-build.txt`, `package.json` |
| Vendor | `assets/bundles/README.md`, notice tiap bundle, `package-lock.json` |

Daftar file aktual dan konfigurasi sidebar lebih otoritatif daripada jumlah halaman yang mungkin berubah. Saat skill ditulis tersedia 93 halaman, 16 kategori komponen UI, dan enam koleksi ikon.

## Aset dan ketergantungan

Bootstrap lokal hanya mempertahankan `dist/css/bootstrap.min.css`, `dist/js/bootstrap.bundle.min.js`, kedua source map, dan lisensi. Bundle JS sudah berisi Popper. Source Sass dan pipeline build upstream tidak tersedia di checkout ini.

CSS lengkap dan urutan script per halaman dirakit oleh `page()` di `scripts/build.py`. Baca fungsi itu dan halaman HTML yang dipilih sebelum melakukan ekstraksi.

| Kebutuhan | Dependency penting |
| --- | --- |
| Grid, utilities, tema | CSS Bootstrap lalu `theme.css` |
| Collapse/dropdown/modal/toast Bootstrap | Bundle Bootstrap; tooltip/popover membutuhkan inisialisasi terkait |
| Shell demo | `sidebar-config.js` + `sidebar-icons.js` → `sidebar.js`; `app.js` memakai modal/toast DOM bersama |
| Select2 | jQuery → Select2; CSS vendor + `controls.css`; initializer di `controls.js` |
| Tanggal/waktu | Flatpickr + locale `id.js`; `controls.css`, `controls.js`; ikon dari `BRUTAL_ICONS` |
| DataTables | core + integrasi Bootstrap; Buttons tambah JSZip/pdfMake/font virtual untuk fitur ekspor terkait |
| Quill | JS + CSS Snow/Bubble sesuai halaman; theme editor disesuaikan di modul form |
| Grafik | Vendor grafik yang dipilih → initializer `charts.js`; jangan memuat semua library untuk satu chart |
| Feather copy | SVG lokal + generated `feather-data.js` → `icons.js` |
| Lordicon | player lokal → generated `animated-icon-data.js` → `animated-icons.js`; `icons.js` untuk search/copy galeri |
| Media | GLightbox atau Owl; Owl membutuhkan jQuery; Bootstrap Carousel cukup bundle Bootstrap |
| Maps | Google API dimuat setelah key diberikan; jsVectorMap + data world untuk peta lokal |

Template asli memuat jQuery/Select2/Flatpickr bersama shell karena modal form tersedia lintas halaman. Aplikasi tujuan boleh menghapus kebutuhan itu jika modal/field tersebut tidak dibawa, tetapi hapus dependensi dan initializer sebagai satu kesatuan.

`npm ci` memasang paket development; tidak menyinkronkan `assets/bundles`. `npm run build` menghasilkan HTML/data demo; tidak memperbarui vendor. Pertahankan struktur relatif font, gambar CSS, dan JSON saat memindah bundle.

## Bahasa visual dan layout

Token utama: `--neo-ink`, `--neo-paper`, `--neo-surface`, `--neo-purple`, `--neo-yellow`, `--neo-green`, `--neo-orange`, `--neo-blue`, `--neo-muted`, `--neo-border`, `--neo-shadow`, `--neo-transition`. Warna tombol memakai variabel Bootstrap komponen; mengganti `--bs-primary` saja belum tentu mengganti seluruh tombol.

Shell menggunakan `.sidebar`, `.app-wrap`, `.topbar`, `.main-content`, `.app-footer`. Sidebar fixed memiliki lebar 236px (210px pada rentang desktop lebih kecil), lalu menjadi drawer di bawah breakpoint 992px. Cocokkan margin `.app-wrap` jika lebar sidebar berubah.

Header sticky: desktop 79px, mobile 70px, `top: 0`, `z-index: 1030`, `flex-shrink: 0`. Backdrop drawer 1035 dan sidebar 1040; modal Bootstrap berada di atasnya. Offset scroll 95px desktop/86px mobile membantu anchor dan fokus. Hindari ancestor overflow yang mengalihkan scroll container tanpa sengaja. Print menyembunyikan header/sidebar.

Pertahankan skip link, focus ring, `aria-expanded` drawer, fokus kembali setelah menutup modal/drawer, dan reduced motion. Untuk menu mobile hasil porting, cegah fokus ke drawer yang tertutup dan ke konten belakang ketika drawer terbuka.

## Form dan bug yang perlu dihindari

- `.form-select` di-upgrade melalui `controls.js`; `data-native` mengecualikan field. Jangan membuat initializer Select2 kedua pada field yang sama.
- Nilai programmatic harus diikuti native `change` berbubbling; jika memakai jQuery, `change.select2` hanya menyinkronkan tampilan plugin, bukan semua logika form.
- Tanggal memakai `YYYY-MM-DD`, waktu `HH:MM`, datetime lokal `YYYY-MM-DDTHH:MM`. Jangan mengubah menjadi UTC tanpa kontrak domain. Month/week tetap native.
- Select2 di modal memakai parent modal untuk menjaga fokus; popup date juga harus berada pada konteks yang sesuai.
- Sebelum mengganti DOM berisi Select2 yang terbuka, tutup popup saat elemen dan ancestors masih terhubung. Listener scroll Select2 dapat mengunci scroll canvas jika dibersihkan terlambat.
- `controls.js` memiliki observer body dan listener global. Cleanup node yang terlepas di dalam script ini bukan lifecycle teardown lengkap untuk SPA; tidak ada API `destroyControls()` publik saat ini.
- Reset form perlu menyinkronkan UI plugin, nilai native, dan state framework; jangan hanya mengganti tampilan.
- Dropdown jumlah entri harus mencakup `pageLength`. `datatables.html` default 10; jangan menganggap semua tabel memakai limit sama.
- Pagination memakai `--neo-page-size`/`--neo-page-icon-size`; arrow SVG dan nomor harus mengikuti ukuran yang sama.
- Progress striped menggunakan `background-color`; shorthand `background` dapat menghapus pola garis.

## Canvas proyek

Kolom demo: Rencana, Berjalan, Review, Selesai. Artikel kartu memiliki `data-project-id`; state menyimpan `boardOrder`. `app.js` menyortir per kolom dan menangani event `kanban:move` dari `kanban.js` dengan detail `{ id, status, beforeId }`; `beforeId: null` menandakan akhir kolom.

Desktop drag memakai area kartu dan mengecualikan kontrol interaktif. Sentuh memakai tekan-tahan agar swipe tetap bisa scroll. Keyboard: Enter/Space ambil/letakkan, kiri/kanan pindah kolom, atas/bawah ubah urutan, Escape batal. UI menjaga scroll dan fokus saat render ulang.

Untuk backend, jangan sekadar menyimpan status baru: simpan posisi juga dan selesaikan perubahan kolom/urutan secara konsisten. Map label demo ke enum/domain tujuan secara eksplisit. Jika update optimistis, pulihkan posisi ketika API gagal; server harus menentukan izin dan konflik antar pengguna.

## Data demo dan perilaku lokal

| Key localStorage | Data |
| --- | --- |
| `brutal.projects`, `brutal.tasks`, `brutal.events` | Proyek/urutan, checklist, agenda |
| `brutal.profile`, `brutal.compact` | Profil dan preferensi |
| `brutal.chat`, `brutal.mail` | Percakapan dan mailbox lokal |
| `brutal.editableTable` | Editor sel, terpisah dari proyek |
| `brutal.posts`, `brutal.subscribers` | Konten dan subscriber demo |
| `brutal.mapsApiKey` | Key browser Maps |

Reset Profil hanya menghapus subset yang disebut pada halaman Profil, bukan semua key. Origin/port/profile browser berbeda menghasilkan storage berbeda. Jangan menyalin reset demo yang menghapus data aplikasi produksi.

Auth form hanya demonstrasi; tidak menyediakan session. Chat, email, kontak, subscribe, upload, dan publikasi tidak mengirim ke server. Statistik/grafik ilustratif tidak otomatis dihitung dari proyek. Pada port aplikasi, hapus/ubah handler seed dan `preventDefault` demo yang dapat menghalangi submit asli.

## Kredit dan batas portabilitas

Vendor memiliki lisensi sendiri; simpan notice yang dipakai. Lordicon player MIT terpisah dari artwork, dan amCharts memiliki branding bawaan. Path sumber lisensi ada pada README bundle. Otika hanya referensi cakupan; asetnya bukan bagian template.

Template bisa dilihat melalui `file://`, tetapi HTTP lokal lebih konsisten untuk clipboard, JSON/fetch, serta origin storage. Google Maps tetap eksternal. Preview HTML tidak membuktikan SSR/hydration, CSP, atau client-side navigation sudah kompatibel; verifikasi pada target nyata.
