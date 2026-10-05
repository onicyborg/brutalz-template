---
name: brutal-template
description: Gunakan, kustomisasi, atau integrasikan template admin BRUTAL. berbasis Bootstrap Neubrutalism ke HTML statis, framework frontend/SSR, atau backend server-rendered termasuk Laravel Blade. Gunakan ketika BRUTAL. menjadi sumber desain/komponen proyek; bukan untuk pengembangan web umum tanpa template ini.
---

# BRUTAL. Template Integration

Skill ini memberi konteks implementasi kepada agent yang memakai BRUTAL. sebagai template. Hasil yang diharapkan adalah halaman atau aplikasi sesuai kebutuhan pengguna, mempertahankan bahasa visual template dan mengikuti arsitektur proyek tujuan. Skill bukan konverter otomatis dan tidak mengharuskan framework tertentu.

## Mulai dengan sumber yang benar

1. Identifikasi **root template** dan **root aplikasi tujuan**. Keduanya bisa sama atau berbeda. Jika skill berada di repository aslinya, root template adalah ancestor yang memiliki `scripts/build.py`, `assets/css/theme.css`, dan `assets/js/sidebar-config.js`. Jika skill dipindah, temukan checkout/aset template yang tersedia; jangan mengasumsikan path komputer pembuat.
2. Baca instruksi repository tujuan, status Git, manifest/framework/version, route, layout, pipeline aset, autentikasi, dan komponen yang sudah ada. Gunakan konteks sesi yang tersedia sebelum meminta informasi tambahan.
3. Baca [konteks template](references/template-context.md). Cari halaman contoh dari `assets/js/sidebar-config.js`, lalu baca HTML, CSS, JavaScript, dan generator modul terkait. `docs.html` adalah panduan penggunaan manusia; implementasi aktual menentukan perilaku.
4. Pilih referensi integrasi yang sesuai, bukan semuanya sekaligus:

| Kondisi tujuan | Referensi |
| --- | --- |
| Memelihara repository BRUTAL. atau memakai HTML tanpa framework | [HTML statis dan generator](references/static-html.md) |
| React, Vue, Svelte, Angular, Next/Nuxt, atau framework server lain | [Framework dan lifecycle](references/framework-integration.md) |
| Laravel dengan Blade, termasuk aset public/Vite | [Laravel Blade](references/laravel-blade.md) |
| Laravel dengan Inertia/Livewire/Turbo/fragment navigation | Baca panduan Blade untuk backend/aset serta panduan lifecycle untuk DOM yang diganti |

Jika framework lain dipilih, petakan tanggung jawab layout, route, asset URL, state, lifecycle, dan form ke fasilitas framework tersebut. Periksa dokumentasi resmi yang sesuai **versi proyek**, bukan mengasumsikan contoh skill cocok dengan setiap versi.

## Kontrak yang perlu dijaga

- **Desain:** gunakan Bootstrap 5.3.8 dan token `--neo-*` sebagai sumber gaya. Pertahankan border tegas, shadow solid, pastel, spacing, responsive layout, dan fokus keyboard. Jangan mengganti keseluruhan desain dengan framework CSS lain kecuali diminta.
- **Header:** `.topbar` pada workspace bersifat sticky di atas, tanpa menutupi konten. Sidebar/drawer, backdrop, modal, dropdown, dan offset anchor harus tetap selaras. Periksa ancestry `overflow` jika sticky gagal.
- **Sumber permanen:** dalam repo template, edit generator untuk perubahan HTML. Dalam aplikasi tujuan, layout/component/view framework adalah sumber permanen; jangan menjalankan generator template di atas view tersebut.
- **Aset:** stylesheet Bootstrap → vendor yang diperlukan → kontrol bersama → tema → style modul/override aplikasi. Urutan JS harus mengikuti dependency. Jangan menduplikasi Bootstrap, jQuery, atau initializer plugin.
- **DOM:** script demo asli banyak memakai IIFE, ID global, `document`, dan `localStorage`. Mereka bukan API komponen universal. Jangan menyisipkan semuanya ke aplikasi reaktif dan menganggap lifecycle sudah ditangani.
- **Data:** UI demo tidak memberi autentikasi, akun, endpoint, email, upload, atau persistence server. Pisahkan komponen visual dari data contoh dan ganti dengan state/API/backend tujuan sesuai scope.
- **Routing:** tautan `.html` dan pencarian sidebar statis perlu diadaptasi jika tujuan memakai router. Active state, nested menu, breadcrumb, deep link, refresh, dan hasil pencarian harus menuju route yang sama.
- **Readability:** tulis HTML/Blade/component secara terindentasi. Jaga ID dan atribut ARIA unik. Jangan memadatkan source aplikasi menjadi satu baris panjang.
- **Scope:** gunakan modul yang diminta. Jangan menyalin seluruh 93 halaman, dependency development, atau data demo ke aplikasi yang hanya butuh satu dashboard. Jangan menghapus fungsi bisnis tujuan karena tidak ada pada template.

## Alur implementasi

### 1. Petakan kebutuhan ke sumber

Catat keputusan singkat yang dapat diperiksa: halaman/komponen sumber, file tujuan, mode rendering, aset yang dipakai, sumber data, dan perilaku interaktif yang harus dipertahankan. Tidak perlu membuat dokumen tambahan jika update singkat sudah cukup.

Cari implementasi yang paling dekat. Misalnya tabel server bukan otomatis memerlukan DataTables; pilih komponen tabel Bootstrap apabila pagination/filter memang dikelola backend. Pemilihan library mengikuti kebutuhan, bukan sekadar karena tersedia.

### 2. Bentuk shell dan kontrak route

Ekstrak sidebar, topbar, footer, breadcrumb, area konten, modal bersama, dan toast yang benar-benar dibutuhkan. Buat satu pemilik untuk setiap bagian DOM. Di framework tujuan, gunakan layout/component/partial yang lazim di proyek tersebut.

Tentukan base URL aset serta pemetaan route. Jangan melakukan replace global `.html` tanpa memahami link navigasi, lampiran, external URL, anchor, dan target modal.

### 3. Integrasikan modul serta perilakunya

Mulai dari markup dan CSS, lalu dependency browser, lalu initializer. Adaptasi handler data terakhir agar tampilannya tidak terikat seed demo. Untuk plugin, tetapkan siapa menginisialisasi, memperbarui, dan menghancurkannya. Hindari initializer global dan wrapper framework yang sama-sama mengontrol elemen tersebut.

Ketika memindahkan suatu komponen, cari semua kontraknya: ID, class, data attributes, event custom, file JSON/font/SVG, sumber gambar dinamis, dan listener reset/modal. Bukan hanya `<link>` atau `<script>` yang terlihat pada satu potongan HTML.

### 4. Hubungkan data sesuai kebutuhan aplikasi

Gunakan model/route/service/state yang sudah ada. Jika membangun fitur baru, definisikan kontrak loading, empty, error, success, validasi, serta persistence terlebih dahulu. Gunakan localStorage hanya bila memang diminta untuk data lokal; jangan menjadikannya pengganti database tanpa keputusan pengguna.

Untuk urutan proyek, persist ID/status/posisi sesuai domain aplikasi dan tangani kegagalan perubahan. Untuk login/logout dan data pengguna, gunakan sistem autentikasi tujuan, bukan handler form demo.

### 5. Verifikasi sesuai perubahan dan instruksi pengguna

- Jalankan build/compile yang relevan untuk source yang berubah. Pemeriksaan dokumen saja tidak memerlukan build aplikasi.
- Periksa path aset, route, duplikasi ID/dependency, dan urutan inisialisasi.
- Verifikasi perilaku yang terdampak: mobile drawer, sticky header, navigasi, popup/modal, input, sorting/pagination, drag/drop, atau lifecycle navigasi ulang.
- Jika pengguna meminta cek manual saja, jangan jalankan suite browser; jelaskan pemeriksaan yang dilakukan dan bagian yang belum diuji. Jangan mewarisi larangan tes dari riwayat lama sebagai aturan universal untuk semua proyek.
- Jangan mengklaim dukungan semua framework telah diuji. Laporkan target/version yang benar-benar diimplementasikan, build/check yang dijalankan, dan keterbatasan nyata.

## Batas tindakan

Skill ini tidak mengotorisasi commit, push, publish, deployment, perubahan akun, atau penghapusan data. Ikuti permintaan dan otorisasi sesi. Tidak perlu meminta izin ulang untuk pekerjaan yang sudah diizinkan. Pertahankan perubahan pengguna yang tidak terkait.

Jangan menanam credential atau API key ke source. Pertahankan lisensi vendor dan atribusi aset terpakai. Penggunaan pribadi tidak otomatis menghapus ketentuan artwork; rujuk notice lokal jika cakupan distribusi berubah.

## Cara membawa skill ke proyek lain

Salin **seluruh folder `brutal-template`**, termasuk `references/`, ke lokasi skill yang didukung agent tujuan. Bila agent tidak mendukung discovery skill, minta ia membaca `SKILL.md` secara eksplisit beserta referensi yang relevan. Folder ini berisi panduan, bukan salinan aset template; berikan akses ke repository/aset sumber secara terpisah.

Contoh instruksi:

> Baca `.agents/skills/brutal-template/SKILL.md`. Template sumber ada di [path template], aplikasi tujuan di [path proyek]. Implementasikan dashboard dan daftar proyek menggunakan Laravel Blade dengan route dan autentikasi yang sudah ada. Pertahankan tema BRUTAL. dan header sticky; ganti seed demo dengan data aplikasi.

Untuk target berbeda, ganti framework dan scope halaman; jangan meminta agent membuat stack baru jika proyek sudah tersedia.
