# Mengintegrasikan BRUTAL. ke Laravel Blade

Gunakan ketika view utama dirender Laravel/Blade. Jika memakai Inertia atau Livewire, baca juga [framework-integration.md](framework-integration.md): backend Laravel tidak berarti DOM selalu full-page reload.

## 1. Kenali aplikasi tujuan

Baca `composer.json`, lockfile, `package.json`, `vite.config.*` jika ada, `routes/web.php`, middleware/auth, layout/components, controller, Form Request, dan model yang relevan. Gunakan versi PHP/Laravel/Node serta package manager proyek tujuan. Jangan memaksakan persyaratan Node repo template ke aplikasi yang hanya menyalin aset browser.

Tentukan apa yang diminta: mengganti tampilan halaman yang ada, membuat dashboard baru, atau membangun fitur bisnis. Pemakaian template saja tidak mengharuskan membuat tabel database, memasang starter auth, mengubah provider, atau menjalankan migrasi.

Dokumen ini menunjukkan pola Blade yang perlu disesuaikan. Referensi versi 12 untuk [Blade](https://laravel.com/docs/12.x/blade), [Vite](https://laravel.com/docs/12.x/vite), dan [validation](https://laravel.com/docs/12.x/validation) adalah sumber API contoh; pilih dokumentasi sesuai versi yang terpasang, bukan meng-upgrade framework agar cocok dengan skill.

## 2. Pilih pipeline aset

### A. Vendor statis di public

Pilihan paling dekat dengan distribusi template. Salin aset runtime yang diperlukan ke namespace khusus, misalnya:

```text
public/vendor/brutal/
  bootstrap-5.3.8/dist/css/bootstrap.min.css
  bootstrap-5.3.8/dist/js/bootstrap.bundle.min.js
  bootstrap-5.3.8/LICENSE
  assets/css/theme.css
  assets/css/controls.css
  assets/css/[modul yang dipakai].css
  assets/bundles/[vendor + font/gambar/JSON + lisensi]
  assets/img/[gambar yang dipakai]
```

Pertahankan sumber lisensi dan structure dependency; source map boleh disertakan untuk debugging. Jangan menyalin seluruh folder template beserta `.git`, skill, tests, node_modules, atau catatan kerja ke `public`.

Gunakan URL yang dihasilkan Laravel:

```blade
<link rel="stylesheet"
      href="{{ asset('vendor/brutal/bootstrap-5.3.8/dist/css/bootstrap.min.css') }}">
<link rel="stylesheet"
      href="{{ asset('vendor/brutal/assets/css/theme.css') }}">
```

Simpan JavaScript/CSS aplikasi hasil adaptasi terpisah dari vendor, mengikuti struktur proyek. URL literal `assets/...` di JS/template harus diubah menjadi base yang benar; memperbaiki `src` pada Blade saja tidak memperbaiki URL gambar yang dirakit JS.

### B. Pipeline Vite yang sudah ada

Pertahankan entry point tujuan. Tempatkan style/controller aplikasi di `resources/` dan gunakan `@vite(...)` sesuai konfigurasi yang ada. Import Bootstrap/theme sekali saja. Vendor tertentu boleh tetap di public dengan urutan loading eksplisit; lihat dokumentasi [asset bundling Laravel](https://laravel.com/docs/12.x/vite).

Jangan memakai `<script src="/resources/js/app.js">`: file resources harus melewati pipeline build. Jangan memuat Bootstrap sebagai bundle public sekaligus import npm. Periksa dependensi jQuery global untuk Select2/plugin legacy dan evaluasi ESM sebelum memilih urutan script.

`npm run dev` di aplikasi Laravel biasanya menjalankan Vite, sedangkan di repo template menjalankan server Python. Sebut working directory saat memberikan perintah agar keduanya tidak tertukar.

## 3. Ekstrak layout dan partial

Jika proyek sudah memiliki layout/component convention, ikuti itu. Struktur berikut hanya contoh untuk proyek yang belum memilikinya:

```text
resources/views/layouts/admin.blade.php
resources/views/admin/partials/sidebar.blade.php
resources/views/admin/partials/topbar.blade.php
resources/views/admin/partials/footer.blade.php
resources/views/admin/partials/flash.blade.php
resources/views/admin/projects/index.blade.php
resources/views/admin/projects/create.blade.php
resources/views/components/admin/[komponen yang dipakai].blade.php
```

Ambil shell dari generated HTML dan `shell()` pada `scripts/build.py`. Pertahankan `.app-wrap`, `.topbar`, `.main-content`, `.sidebar` jika ingin memakai aturan responsive/tema yang sama.

Contoh skeleton layout berikut memakai **partial yang perlu dibuat dari shell**, bukan file yang sudah disediakan repo template:

```blade
<!doctype html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>@yield('title', 'Dashboard') — {{ config('app.name') }}</title>
    <link rel="stylesheet"
          href="{{ asset('vendor/brutal/bootstrap-5.3.8/dist/css/bootstrap.min.css') }}">
    @stack('vendor-styles')
    <link rel="stylesheet"
          href="{{ asset('vendor/brutal/assets/css/theme.css') }}">
    @stack('styles')
</head>
<body>
    <a class="skip-link" href="#main">Lewati ke konten</a>
    @include('admin.partials.sidebar')
    <div class="app-wrap">
        @include('admin.partials.topbar')
        <main class="main-content" id="main" tabindex="-1">
            @include('admin.partials.flash')
            @yield('content')
        </main>
        @include('admin.partials.footer')
    </div>
    @stack('modals')
    <script src="{{ asset('vendor/brutal/bootstrap-5.3.8/dist/js/bootstrap.bundle.min.js') }}"></script>
    @stack('vendor-scripts')
    @stack('shell-scripts')
    @stack('scripts')
</body>
</html>
```

Stacks merakit markup; mereka bukan dependency loader. Layout/partial shell harus menambahkan handler drawer yang telah diadaptasi ke `shell-scripts` tepat satu kali. Halaman memasukkan initializer setelah vendor siap. Jika aplikasi memakai Vite, ganti blok yang sesuai dengan entry point aplikasi dan hindari urutan module/classic script yang ambigu.

Jangan menjalankan `sidebar.js` asli di atas sidebar Blade; renderer itu akan menghasilkan `.html` dan menu demo. Port perilaku drawer/collapse/focus ke controller shell aplikasi. Jangan memuat `app.js` demo sebagai pengganti controller shell: ia juga menginisialisasi state proyek dan handler demo.

## 4. Route, navigasi, dan autentikasi

Gunakan named routes yang sudah tersedia. Nama `admin.projects.*` di bawah adalah **contoh**; baca `route:list` dan ganti sesuai aplikasi sebelum menggunakannya.

```blade
<a href="{{ route('admin.projects.index') }}"
   class="sidebar-link {{ request()->routeIs('admin.projects.*') ? 'active' : '' }}"
   @if(request()->routeIs('admin.projects.*')) aria-current="page" @endif>
    Proyek
</a>
```

Sidebar group active harus mengikuti descendant route dan membuka collapse yang sesuai. Ganti breadcrumb, global search, notifikasi, logo, footer link, akun, serta URL media—bukan sidebar saja. Untuk detail `/projects/{id}`, named route menangani parameter dan base URL.

Render nama/avatar dari user session yang valid. Untuk halaman protected, gunakan middleware dan policy sesuai aplikasi; menyembunyikan menu melalui `@can` hanya kontrol UI. Logout mengikuti route/metode/CSRF sistem auth tujuan, bukan redirect ke `auth-login.html`. Jangan memasang scaffold autentikasi baru hanya untuk mengganti tampilan.

## 5. Form Blade dan validasi

Ubah demo form menjadi submit server nyata: route, method, token CSRF, nama field, old value, error per field, status sukses, dan redirect. Hapus handler demo yang mencegat submit atau menulis ke localStorage.

Contoh field untuk route create yang sudah didefinisikan:

```blade
<form method="POST" action="{{ route('admin.projects.store') }}">
    @csrf
    <label for="project-name" class="form-label">Nama proyek</label>
    <input id="project-name" name="name" type="text"
           class="form-control @error('name') is-invalid @enderror"
           value="{{ old('name') }}" required maxlength="120"
           @error('name') aria-invalid="true" aria-describedby="project-name-error" @enderror>
    @error('name')
        <div id="project-name-error" class="invalid-feedback">{{ $message }}</div>
    @enderror
    <button type="submit" class="btn btn-primary mt-3">Simpan proyek</button>
</form>
```

Sesuaikan limit HTML dengan kontrak Form Request/server; contoh 120 bukan batas wajib BRUTAL. Untuk update, pakai metode yang diharapkan route, misalnya `@method('PATCH')`; jangan hanya mengubah label tombol.

Validasi dan otorisasi berlangsung di server. Tampilkan flash/error bag aplikasi tanpa menempel konten mentah. Contoh field di atas mengikuti dukungan Blade [CSRF dan form error](https://laravel.com/docs/12.x/blade) serta [validation Laravel](https://laravel.com/docs/12.x/validation).

Jika memilih Select2/Flatpickr:

- Muat plugin, CSS, locale, dan controller yang diperlukan sekali.
- Nilai select/date berasal dari `old(...)` atau model; tampilan plugin harus sinkron setelah error/reset.
- Controller adaptasi harus mempertahankan error server dan `aria-describedby`.
- `controls.js` asli membutuhkan jQuery, plugin, serta `BRUTAL_ICONS`; jika disalin, bawa kontrak itu dan evaluasi listener globalnya. Untuk Livewire, jangan menjalankannya berkali-kali tanpa lifecycle adapter.
- File upload nyata memerlukan form encoding, endpoint, validasi, dan storage. Pratinjau Dropzone template tidak menyediakan semua itu.

## 6. Data, tabel, dan pagination

Controller/service menyediakan data; Blade merender view. Jangan melakukan query Eloquent per baris di partial kartu jika data dapat disiapkan/eager-loaded sebelumnya. Gunakan escaped echo `{{ ... }}` untuk data pengguna; raw output hanya untuk HTML yang memang sudah disanitasi.

Tabel server memakai query filter/sort dan paginator Laravel sesuai proyek. Pilih renderer pagination Bootstrap 5 yang tersedia pada versi tujuan, agar kelas pagination mengikuti tema. Pertahankan parameter filter saat berpindah halaman, aksesibilitas active/disabled, dan state kosong.

Jangan menginisialisasi DataTables client pada satu halaman paginator server lalu menganggap ia mengurutkan seluruh database. Pilih salah satu:

1. Tabel Blade dengan paginator/filter backend.
2. Dataset kecil utuh pada client, dikelola DataTables.
3. DataTables server-side dengan endpoint yang mengikuti kontrak draw/filter/order/count plugin.

Keputusan ini bagian dari kebutuhan data aplikasi; tidak diputuskan oleh tampilan demo.

## 7. Kanban dan request asinkron

Port markup kartu/kolom dan interaksi yang relevan dari `projects.html`, `app.js`, serta `kanban.js`. Event `kanban:move` membawa `{ id, status, beforeId }`; backend harus memvalidasi proyek, kolom, dan posisi, bukan mempercayai label UI.

Untuk API/session endpoint Laravel, gunakan strategi CSRF/autentikasi aplikasi yang sudah ada. Serialisasikan konfigurasi JS lewat helper framework, misalnya `Illuminate\Support\Js::from`, daripada menggabungkan string user input ke script. URL endpoint idealnya berasal dari `route()`.

Simpan perpindahan status dan urutan dalam operasi yang konsisten. Tangani konflik/izin, loading, error, rollback optimistis, scroll, dan fokus. Transaksi/locking serta schema kolom posisi dipilih berdasarkan model aktual; jangan menambah migration generik tanpa memeriksa schema existing.

## 8. Livewire / Inertia

Pada Livewire, render ulang field dapat menggandakan Select2 atau membuang instance aktif. Tentukan adapter, boundary DOM, event value, dan teardown sesuai versi Livewire. `wire:ignore` saja tidak menghubungkan value plugin ke state server.

Pada Inertia, gunakan komponen React/Vue yang dikelola router client; Blade root hanya shell awal. `@push` pada view server bukan mekanisme lifecycle halaman Inertia. Baca referensi framework dan pertahankan satu pemilik DOM.

## 9. Setup, verifikasi, dan handoff

Ikuti README aplikasi tujuan untuk `composer install`, environment lokal, database, dan asset build. Jangan menimpa `.env` existing atau menjalankan reset database/migrasi destruktif sebagai bagian kosmetik. Root web Laravel adalah `public/`; server Python root template bukan cara menjalankan Laravel.

Verifikasi yang relevan meliputi route/view compile, build Vite jika dipakai, asset URL pada nested routes, POST validation/CSRF, active nav, sticky header, drawer, modal/form, dan authorization endpoint. Gunakan tes proyek yang sesuai bila diminta/diizinkan; jika pengguna memilih manual, laporkan langkah manual tanpa mengklaim test pass.

Handoff harus menyebut layout/partial/controller yang berubah, aset yang diambil, route yang digunakan, data nyata vs demo, cara menjalankan target, dan batas yang belum diverifikasi. Menghasilkan contoh Blade di skill tidak berarti aplikasi Laravel telah dibuat atau dijalankan.
