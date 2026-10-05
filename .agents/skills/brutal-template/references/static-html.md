# HTML tanpa framework dan pemeliharaan generator

Gunakan ketika tujuan tetap berupa halaman statis atau saat mengubah repository BRUTAL. sendiri. Path berikut relatif terhadap root template.

## Pilih sumber permanen

| Mode | Source yang diedit | Build |
| --- | --- | --- |
| Memperbaiki halaman bawaan BRUTAL. | Generator Python untuk markup; CSS/JS langsung untuk perilaku/style | Build setelah perubahan generator |
| Membuat situs statis turunan | HTML/partial milik situs tujuan, atau generator yang memang dipilih | Ikuti pipeline tujuan; Python BRUTAL. opsional |
| Prototipe cepat | Salinan `blank.html` dengan nama baru | Tidak perlu build jika dikelola manual |

Jangan membiarkan generator dan editor manual menulis file halaman yang sama tanpa menentukan mana sumbernya.

## Preview dan setup

```bash
# Dari root template; tidak membutuhkan npm install.
python3 -m http.server 4173 --bind 127.0.0.1
```

Pada Windows gunakan `py -m http.server 4173 --bind 127.0.0.1` jika `python3` tidak ada. `npm run dev` hanyalah wrapper server Python, bukan Vite.

Untuk generator, gunakan Python 3.10+ dan requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-build.txt
python scripts/build.py
```

Windows tanpa aktivasi:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-build.txt
.\.venv\Scripts\python.exe scripts/build.py
```

Jika executable `python3` tersedia dalam environment aktif, `npm run build` menjalankan generator yang sama. Generator memformat HTML dan memeriksa semantik; tidak ada watcher otomatis. Gunakan `npm ci` hanya untuk dependency development/vendor/Playwright yang dibutuhkan. Node 22+ diperlukan oleh sebagian paket development yang terkunci saat skill ditulis.

## Menambah halaman generated

1. Tambahkan item navigasi pada array JSON valid `window.BRUTAL_SIDEBAR` dalam `assets/js/sidebar-config.js`.
2. Pilih key kebab-case, misalnya `sales-report`. Nama file output, `body[data-page]`, dan key harus konsisten.
3. Tambahkan konten ke mapping `pages` di `main()` atau modul generator yang digabung di sana.
4. Tambahkan CSS/JS/vendor bersyarat di `page()` jika perlu. Tidak cukup membuat HTML tanpa mendaftarkan sumber generate.
5. Build; direktori halaman dokumentasi dan active navigation mengikuti konfigurasi.

Contoh entri navigasi:

```json
{"page":"sales-report","label":"Laporan penjualan","icon":"chart"}
```

Contoh pemetaan Python di dictionary `pages`:

```python
'sales-report': heading('Laporan penjualan', 'Ringkasan periode ini.')
    + card('Pendapatan', '<p>Konten laporan.</p>'),
```

Dropdown memiliki `id` unik dan `children`; `icon` harus ada di kamus `ICONS`. `sidebar-icons.js`, `feather-data.js`, dan `animated-icon-data.js` merupakan hasil generate; ubah sumbernya agar perubahan tidak hilang.

## Membuat aplikasi turunan ringan

Ambil HTML contoh yang paling dekat. Pertahankan struktur shell yang dibutuhkan, lalu:

- Ubah title, breadcrumb, brand, teks, tautan, dan data-page.
- Sediakan konfigurasi sidebar hanya untuk halaman tujuan. Renderer asli selalu menghasilkan `${page}.html`; cocok hanya jika URL tujuan mengikuti kontrak itu.
- Pastikan sidebar/footer/search/account links tidak mengarah ke halaman demo yang tidak ikut disalin.
- Jika tidak memakai `app.js`, bawa handler shell yang diperlukan secara terpisah; jangan menganggap pencarian/toast/project modal bekerja hanya karena markup tersedia.
- Jika mempertahankan `app.js`, bawa modal/toast DOM yang dipakai atau refactor dependensi menjadi opsional. ID seperti `toastMessage` bukan sekadar kosmetik.
- Saat mengambil sebagian form, bawa dependency kontrolnya atau pakai `data-native`. Jangan meninggalkan initializer tanpa plugin.
- Ganti seed ilustratif sesuai kebutuhan. Jangan menyatakan demo email/login sudah menjadi layanan nyata.

Tidak perlu mempertahankan prefix nama BRUTAL. atau seluruh direktori generator pada aplikasi turunan jika pengguna ingin identitas berbeda. Tetap pertahankan kredit lisensi aset yang dipakai.

## Path aset

Jaga struktur folder di dalam bundle. Referensi font/gambar dari CSS relatif ke **file CSS**, sedangkan URL string di JS biasanya relatif ke **URL dokumen**. HTML yang dipindah ke `/admin/reports/` akan membuat `assets/...` mengarah ke lokasi berbeda.

Gunakan root asset base yang sesuai deployment atau helper URL; jangan mengatasi semua masalah dengan tag `<base>` karena dapat mengubah anchor, submit form, dan navigasi. Jika aplikasi berada di subpath, gunakan base URL subpath tersebut. Periksa path dinamis pada JS selain atribut `src`/`href`.

## Deploy dan handoff

Untuk semua halaman template, deploy `*.html`, `assets/`, dan `bootstrap-5.3.8/`. Untuk turunan parsial, deploy hanya halaman dan dependency transitive yang dipakai, termasuk font/JSON/SVG/notice vendor. `node_modules`, venv, tes, generator, cache, serta catatan pribadi tidak diperlukan di hosting statis.

Halaman `errors-*.html` tidak mengatur status HTTP; konfigurasi hosting menentukan routing error. Hindari deployment full repository yang membuka file lingkungan atau source backend.

Laporkan file yang diubah, cara preview/build, modul yang aktif, dan mana data demo vs nyata. Jangan commit/push hanya karena skill telah selesai; ikuti scope permintaan pengguna.
