# Library eksternal lokal

Phase 2 menambahkan bundle berikut dari paket npm resmi. Versi terkunci di
`package.json` dan `package-lock.json`; file distribusi disalin ke sini agar
halaman statis berjalan tanpa CDN dan tanpa proses build saat runtime.

| Bundle | Versi | Halaman | Lisensi dan sumber |
| --- | --- | --- | --- |
| SweetAlert2 | 11.26.25 | `sweet-alert.html` | MIT, https://github.com/sweetalert2/sweetalert2 (`sweetalert/LICENSE`) |
| Toastr | 2.1.4 | `toastr.html` | MIT, https://github.com/CodeSeven/toastr (lisensi dinyatakan pada README upstream) |
| jQuery | 3.7.1 | `toastr.html` saja, dependency Toastr | MIT, https://github.com/jquery/jquery (`jquery/LICENSE.txt`) |
| Dropzone | 5.9.3 | `multiple-upload.html` | MIT, https://github.com/dropzone/dropzone (`dropzone/LICENSE`) |

Otika memakai SweetAlert lama dan iziToast. Phase 2 memakai SweetAlert2 dan
Toastr seperti yang tertulis di `PHASE-PLAN.md`; keduanya dipisahkan per halaman.
Dropzone dipakai sebagai pratinjau lokal dengan `autoProcessQueue: false`.
Tidak ada file yang dikirim ke server. Bootstrap tetap berada di
`bootstrap-5.3.8/` dan source vendor tidak dimodifikasi.
