# Library eksternal lokal

Phase 2–3 menambahkan bundle berikut dari paket npm resmi. Versi terkunci di
`package.json` dan `package-lock.json`; file distribusi disalin ke sini agar
halaman statis berjalan tanpa CDN dan tanpa proses build saat runtime.

| Bundle | Versi | Halaman | Lisensi dan sumber |
| --- | --- | --- | --- |
| SweetAlert2 | 11.26.25 | `sweet-alert.html` | MIT, https://github.com/sweetalert2/sweetalert2 (`sweetalert/LICENSE`) |
| Toastr | 2.1.4 | `toastr.html` | MIT, https://github.com/CodeSeven/toastr (lisensi dinyatakan pada README upstream) |
| jQuery | 3.7.1 | `toastr.html`, `forms-advanced-form.html`, `form-wizard.html` | MIT, https://github.com/jquery/jquery (`jquery/LICENSE.txt`) |
| Dropzone | 5.9.3 | `multiple-upload.html` | MIT, https://github.com/dropzone/dropzone (`dropzone/LICENSE`) |
| Select2 | 4.0.13 | `forms-advanced-form.html` | MIT, https://github.com/select2/select2 (`select2/LICENSE.md`) |
| Quill | 2.0.3 | `forms-editor.html` | BSD-3-Clause, https://github.com/slab/quill (`quill/LICENSE`; bundle juga memuat notice lisensi dependensi) |
| jQuery Steps | 1.1.0 | `form-wizard.html` | MIT, https://github.com/rstaib/jquery-steps (`jquery-steps/LICENSE.txt`) |

Otika memakai SweetAlert lama dan iziToast. Phase 2 memakai SweetAlert2 dan
Toastr seperti yang tertulis di `PHASE-PLAN.md`; keduanya dipisahkan per halaman.
Dropzone dipakai sebagai pratinjau lokal dengan `autoProcessQueue: false`.
Tidak ada file yang dikirim ke server. Bootstrap tetap berada di
`bootstrap-5.3.8/` dan source vendor tidak dimodifikasi.

Phase 3 memakai CSS lokal sendiri untuk wizard, Select2, dan editor agar selaras
dengan tema. Editor hanya menampilkan preview teks; form lanjutan dan wizard
hanya memberi umpan balik di browser. Tidak ada pengiriman data atau akun dibuat.
