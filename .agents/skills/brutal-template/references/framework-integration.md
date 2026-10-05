# Integrasi lintas framework dan lifecycle

Gunakan untuk SPA, SSR/hybrid, atau backend server-rendered selain alur Blade khusus. Tujuannya memetakan desain dan interaksi BRUTAL. ke arsitektur yang sudah dipilih; bukan memaksa satu stack.

## Tentukan mode rendering dulu

| Target | Strategi |
| --- | --- |
| Server templates dengan full-page navigation | Ekstrak layout/partial; URL aset dan route dari helper framework; initializer berjalan setelah DOM tersedia |
| React/Vue/Svelte/Angular SPA | Ekstrak komponen; state/router milik framework; plugin dibungkus lifecycle lokal |
| Next/Nuxt atau SSR/hybrid lain | Render markup deterministik di server, inisialisasi plugin DOM hanya di client; jangan mengeksekusi IIFE browser saat import server |
| Inertia, Livewire, Turbo, HTMX, atau fragment replacement | Tetapkan batas DOM yang diganti dan teardown/remount plugin; jangan mengandalkan `DOMContentLoaded` untuk setiap navigasi |
| Backend lain: Django/Jinja, Rails/ERB, ASP.NET/Razor, PHP biasa | Ikuti layout, URL helper, CSRF, validation, pagination, dan asset pipeline yang sudah digunakan |

Untuk teknologi/version yang tidak ada di checkout, verifikasi API melalui dokumentasi resmi sebelum menulis kode. Skill ini menyediakan kontrak adaptasi, bukan jaminan semua API antar framework identik.

## Strategi aset

**Aset public:** salin vendor dan tema ke namespace seperti `public/vendor/brutal/`, pertahankan struktur, lalu gunakan helper base URL target. Cocok untuk integrasi awal yang ingin mempertahankan distribusi lokal.

**Bundler:** gunakan pipeline yang sudah ada; pisahkan CSS tema, modul aplikasi, dan import vendor. Sesuaikan URL font/gambar/JSON dan bundler handling untuk plugin legacy. Jangan sekaligus memuat versi CDN/public dan import package library yang sama.

**Campuran:** vendor statis + aplikasi dibundel boleh dipakai dengan urutan eksplisit. Static imports ESM dievaluasi sebelum body module: menulis `window.jQuery = ...` di bawah import tidak menjamin plugin legacy sudah melihat global tersebut. Pilih import/package adapter yang benar atau loader sekuensial dan verifikasi hasilnya.

Pertahankan Bootstrap CSS sebelum override tema. Jika target sudah memakai Bootstrap versi lain, periksa selisih markup/data API dan migrasikan secara sengaja; jangan memuat dua versi. Jika target memakai reset/Tailwind/CSS framework lain, tentukan scoping atau area tema agar reset/button/table tidak saling menimpa. Jangan mengganti sistem styling aplikasi tanpa kebutuhan.

## Shell dan route

Buat komponen/partial untuk `Sidebar`, `Topbar`, `Breadcrumb`, `Footer`, dan slot konten. Gunakan kelas layout BRUTAL. bila ingin mempertahankan CSS tanpa menulis ulang.

Sidebar asli memiliki dua tanggung jawab yang harus dipisahkan saat porting:

1. Membangun markup dari konfigurasi yang mengasumsikan `${page}.html`.
2. Mengatur drawer mobile, fokus, collapse, dan status active.

Di router framework, map item ke route/path yang benar. Jika server sudah merender sidebar, jangan jalankan renderer asli untuk menimpa DOM tersebut. Port handler drawer atau gunakan component controller yang setara. Pencarian global menggunakan daftar navigasi yang sama; jangan memperbaiki sidebar tetapi membiarkan search mengarah ke `.html`.

Periksa link akun/logout: logout aplikasi bukan tautan ke halaman demo login. Tautan eksternal, download, hash, dan target modal jangan diperlakukan sebagai route internal.

## Satu pemilik DOM per bagian

Framework mengelola data/state dan markup komponen. Plugin imperatif hanya mengelola subtree yang diberikan secara eksplisit. Contoh: container editor, canvas grafik, root peta, atau field select wrapper.

Jangan membiarkan renderer framework mengubah `<option>` atau children yang sedang dipindah plugin tanpa prosedur update/destroy. Jangan biarkan `app.js` merender ulang tabel yang sama dengan komponen framework. Pertahankan ID/refs stabil dan jangan memakai ID global yang sama pada dua instance komponen.

Rancang kontrak adapter lokal, misalnya:

```text
mountWidget(element, initialData) -> { update(nextData), destroy() }
```

Ini **kontrak yang perlu diimplementasikan**, bukan fungsi yang sudah tersedia pada BRUTAL. `controls.js`, `kanban.js`, `sidebar.js`, dan sebagian besar initializer asli belum mengekspor lifecycle API seperti itu.

Adapter harus:

- Menginisialisasi setelah elemen terpasang dan dependency siap, satu instance per elemen.
- Memperbarui data tanpa memulai ulang plugin bila plugin punya API update.
- Melepas event handler, observer, timer, RAF, pointer capture, instance plugin, backdrop/portal yang dibuatnya ketika subtree dibongkar.
- Menutup popup Select2 saat elemen dan ancestor masih terhubung, sebelum destroy/replace DOM.
- Menyinkronkan event plugin ke state framework tanpa loop perubahan dua arah.
- Menangani mount → unmount → mount dengan benar, termasuk development double initialization.

## React

Ubah `class` menjadi `className`, `for` menjadi `htmlFor`, atribut/style SVG ke bentuk JSX yang sesuai. Gunakan refs untuk container plugin; pertahankan data/ARIA attributes yang valid. Native Bootstrap data attributes boleh dipakai jika instance dan lifecycle-nya dikelola konsisten; jangan dicampur dengan library wrapper lain pada elemen sama.

Effect tepat untuk sinkronisasi plugin eksternal; cleanup harus membalik setup yang memiliki resource/listener. Efek tidak berjalan saat server rendering. Lihat [useEffect resmi](https://react.dev/reference/react/useEffect) dan [sinkronisasi efek](https://react.dev/learn/synchronizing-with-effects).

Pola penggunaan adapter buatan aplikasi (bukan kode drop-in):

```jsx
const elementRef = useRef(null);

useEffect(() => {
  const widget = mountWidget(elementRef.current, initialData);
  return () => widget.destroy();
}, [initialData]);
```

Import `useRef`/`useEffect` dan implementasikan adapter sebelum memakai contoh. Stabilkan dependency atau pisahkan effect inisialisasi dan update agar data baru tidak selalu menghancurkan widget. Jangan membaca `document`/localStorage pada import module yang dapat dievaluasi server.

## Vue dan framework reaktif lain

Pada Vue gunakan template ref, inisialisasi sesudah mounted, update lewat watcher terkontrol, dan cleanup sebelum node plugin dihapus. DOM-only effects tidak dikerjakan saat SSR. Rujukan: [lifecycle Vue](https://vuejs.org/api/composition-api-lifecycle).

Untuk Svelte/Angular/framework lain, cari lifecycle mount/view-ready, update, dan destroy yang setara pada versi tujuan. Angular/Svelte bukan alasan untuk meng-copy IIFE ke file component tanpa teardown. Jika custom element `lord-icon` digunakan, ikuti konfigurasi compiler/custom-element dan typing framework tersebut.

## SSR dan navigasi parsial

- Markup server dan client awal harus konsisten. Jangan membangun HTML awal dari data localStorage yang tidak diketahui server sehingga hydration berubah.
- Pisahkan data server dari preference client. Terapkan preference setelah mount bila tidak disediakan server.
- Import browser-only library di client boundary atau setelah mount sesuai framework. Menambahkan guard pada satu baris belum menyelesaikan efek import dependency yang mengakses `window`.
- Untuk navigasi client, perbarui active route/title/breadcrumb, tutup drawer, bersihkan popup, dan restore fokus secara tepat.
- Untuk Livewire/HTMX/Turbo, kontrol kapan DOM plugin diabaikan atau dibongkar. Mekanisme ignore saja tidak menyinkronkan value ke backend; perlu jembatan event/state. Periksa API lifecycle versi yang terpasang.
- Jangan memasang observer global baru pada setiap navigasi. Jangan memuat script IIFE yang sama berkali-kali.

## Data dan perilaku aplikasi

Pilih model data tujuan. Adapter dari `brutal.projects` hanya membantu memahami UI; bukan schema database wajib. Tentukan operasi status/urutan Kanban, ID stabil, kontrol konkurensi, dan rollback. Jangan menganggap urutan array global sama dengan urutan per kolom.

Tabel: pilih server pagination atau client pagination secara sadar. Jangan membungkus satu halaman hasil pagination server dengan DataTables yang mengaku menampilkan seluruh dataset. Routing sort/filter harus sinkron dengan query URL bila itu pola aplikasi.

Form: pertahankan nama field, state validation/error, aksesibilitas, reset, dan submit state. Pindahkan logika demo `preventDefault` agar tidak mencegat submit nyata. Auth/CSRF/otorisasi mengikuti backend tujuan. Escape plain text, sanitasi rich text, dan serialisasikan data server dengan helper framework; jangan menempel JSON mentah dari input pengguna ke script.

## Verifikasi integrasi

Periksa hard refresh deep route, navigasi bolak-balik, mount berulang, popup dalam modal, drawer mobile, anchor di bawah header sticky, filter/pagination, dan error API. Jalankan build/SSR compile target sesuai scope. Bila tes browser dilarang pengguna, tulis skenario manual dan jelaskan bahwa lifecycle interaktif belum diuji, bukan menyatakan integrasi seluruh framework sudah terbukti.
