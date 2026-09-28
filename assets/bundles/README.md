# Library eksternal lokal

Phase 2–4 menambahkan bundle berikut dari paket npm resmi. Versi terkunci di
`package.json` dan `package-lock.json`; file distribusi disalin ke sini agar
halaman statis berjalan tanpa CDN dan tanpa proses build saat runtime.

| Bundle | Versi | Halaman | Lisensi dan sumber |
| --- | --- | --- | --- |
| SweetAlert2 | 11.26.25 | `sweet-alert.html` | MIT, https://github.com/sweetalert2/sweetalert2 (`sweetalert/LICENSE`) |
| Toastr | 2.1.4 | `toastr.html` | MIT, https://github.com/CodeSeven/toastr (lisensi dinyatakan pada README upstream) |
| jQuery | 3.7.1 | `toastr.html`, `forms-advanced-form.html`, `form-wizard.html`, `datatables.html`, `export-table.html` | MIT, https://github.com/jquery/jquery (`jquery/LICENSE.txt`) |
| Dropzone | 5.9.3 | `multiple-upload.html` | MIT, https://github.com/dropzone/dropzone (`dropzone/LICENSE`) |
| Select2 | 4.0.13 | `forms-advanced-form.html` | MIT, https://github.com/select2/select2 (`select2/LICENSE.md`) |
| Quill | 2.0.3 | `forms-editor.html` | BSD-3-Clause, https://github.com/slab/quill (`quill/LICENSE`; bundle juga memuat notice lisensi dependensi) |
| jQuery Steps | 1.1.0 | `form-wizard.html` | MIT, https://github.com/rstaib/jquery-steps (`jquery-steps/LICENSE.txt`) |
| DataTables + Bootstrap 5 | 2.3.8 | `datatables.html`, `export-table.html` | MIT, https://github.com/DataTables/DataTablesSrc (`datatables/License.txt`, `datatables/Bootstrap5-License.txt`) |
| DataTables Buttons + Bootstrap 5 | 3.2.6 | `export-table.html` | MIT, https://github.com/DataTables/Buttons (`datatables-buttons/License.txt`, `datatables-buttons/Bootstrap5-License.txt`) |
| JSZip | 3.10.2 | `export-table.html` | MIT atau GPL-3.0-or-later, https://github.com/Stuk/jszip (`jszip/LICENSE.markdown`); digunakan menurut lisensi MIT |
| pdfMake | 0.2.23 | `export-table.html` | MIT, https://github.com/bpampuch/pdfmake (`pdfmake/LICENSE`) |

Otika memakai SweetAlert lama dan iziToast. Phase 2 memakai SweetAlert2 dan
Toastr seperti yang tertulis di `PHASE-PLAN.md`; keduanya dipisahkan per halaman.
Dropzone dipakai sebagai pratinjau lokal dengan `autoProcessQueue: false`.
Tidak ada file yang dikirim ke server. Bootstrap tetap berada di
`bootstrap-5.3.8/` dan source vendor tidak dimodifikasi.

Phase 3 memakai CSS lokal sendiri untuk wizard, Select2, dan editor agar selaras
dengan tema. Editor hanya menampilkan preview teks; form lanjutan dan wizard
hanya memberi umpan balik di browser. Tidak ada pengiriman data atau akun dibuat.

Phase 4 memakai DataTables + Buttons untuk pencarian, pagination, serta ekspor
Excel/CSV/PDF/Print. `advance-table.html` dan `editable-table.html` memakai
JavaScript vanilla; editor sel menyimpan data contoh pada `brutal.editableTable`
di localStorage, terpisah dari proyek workspace. Bundle hanya dimuat pada
halaman yang memerlukannya.
