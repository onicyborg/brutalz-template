# Library eksternal lokal

Phase 2–8 menambahkan bundle berikut dari paket npm dan upstream resmi. Versi terkunci di
`package.json` dan `package-lock.json`; file distribusi disalin ke sini agar
halaman statis berjalan tanpa CDN dan tanpa proses build saat runtime.

| Bundle | Versi | Halaman | Lisensi dan sumber |
| --- | --- | --- | --- |
| SweetAlert2 | 11.26.25 | `sweet-alert.html` | MIT, https://github.com/sweetalert2/sweetalert2 (`sweetalert/LICENSE`) |
| Toastr | 2.1.4 | `toastr.html` | MIT, https://github.com/CodeSeven/toastr (lisensi dinyatakan pada README upstream) |
| jQuery | 3.7.1 | Semua halaman (Select2 dalam shared modal) dan plugin per halaman | MIT, https://github.com/jquery/jquery (`jquery/LICENSE.txt`) |
| Dropzone | 5.9.3 | `multiple-upload.html` | MIT, https://github.com/dropzone/dropzone (`dropzone/LICENSE`) |
| Select2 | 4.0.13 | Semua `.form-select`, termasuk field dinamis dan modal | MIT, https://github.com/select2/select2 (`select2/LICENSE.md`) |
| Quill | 2.0.3 | `forms-editor.html`, `create-post.html` | BSD-3-Clause, https://github.com/slab/quill (`quill/LICENSE`; bundle juga memuat notice lisensi dependensi) |
| jQuery Steps | 1.1.0 | `form-wizard.html` | MIT, https://github.com/rstaib/jquery-steps (`jquery-steps/LICENSE.txt`) |
| DataTables + Bootstrap 5 | 2.3.8 | `datatables.html`, `export-table.html` | MIT, https://github.com/DataTables/DataTablesSrc (`datatables/License.txt`, `datatables/Bootstrap5-License.txt`) |
| DataTables Buttons + Bootstrap 5 | 3.2.6 | `export-table.html` | MIT, https://github.com/DataTables/Buttons (`datatables-buttons/License.txt`, `datatables-buttons/Bootstrap5-License.txt`) |
| JSZip | 3.10.2 | `export-table.html` | MIT atau GPL-3.0-or-later, https://github.com/Stuk/jszip (`jszip/LICENSE.markdown`); digunakan menurut lisensi MIT |
| pdfMake | 0.2.23 | `export-table.html` | MIT, https://github.com/bpampuch/pdfmake (`pdfmake/LICENSE`) |
| Chart.js | 4.5.1 | `chart-chartjs.html` | MIT, https://github.com/chartjs/Chart.js (`chartjs/LICENSE.md`) |
| ApexCharts | 3.54.1 | `chart-apexchart.html` | MIT untuk versi ini, https://github.com/apexcharts/apexcharts.js (`apexcharts/LICENSE`) |
| amCharts 4 | 4.10.40 | `chart-amchart.html` | [amCharts free license](https://www.amcharts.com/download-v4/), branding wajib tetap tampil (`amcharts4/LICENSE`) |
| Apache ECharts | 6.1.0 | `chart-echart.html` | Apache-2.0, https://echarts.apache.org/ (`echarts/LICENSE`, `echarts/NOTICE`) |
| jQuery Sparkline | 2.4.0 | `chart-sparkline.html` | BSD, https://github.com/gwatts/jquery.sparkline (`sparkline/LICENSE.txt`) |
| Morris.js + Raphael | 0.5.1 (commit `14530d0`) + 2.3.0 | `chart-morris.html` | BSD-2-Clause + MIT, https://github.com/morrisjs/morris.js dan https://github.com/DmitryBaranovskiy/raphael (`morris/LICENSE-MORRIS.txt`, `morris/license.txt`) |
| Font Awesome Free | 6.7.2 | `icon-font-awesome.html` | Ikon CC BY 4.0, font SIL OFL 1.1, kode MIT, https://fontawesome.com/ (`fontawesome/LICENSE.txt`) |
| Material Icons via Fontsource | 5.3.0 | `icon-material.html` | Font SIL OFL 1.1, https://github.com/fontsource/fontsource (`material-icons/LICENSE`) |
| Ionicons | 7.4.0 | `icon-ionicons.html` | MIT, https://github.com/ionic-team/ionicons (`ionicons/LICENSE`) |
| Feather Icons | 4.29.2 | `icon-feather.html` | MIT, https://github.com/feathericons/feather (`feather/LICENSE`) |
| Weather Icons | 2.0.12 | `icon-weather-icon.html` | Font SIL OFL 1.1, CSS MIT, https://github.com/erikflowers/weather-icons (`weather-icons/LICENSE.md`) |
| GLightbox | 3.3.1 | `light-gallery.html` | MIT, https://github.com/biati-digital/glightbox (`glightbox/LICENSE.md`) |
| Owl Carousel | 2.3.4 | `owl-carousel.html` | MIT, https://github.com/OwlCarousel2/OwlCarousel2 (`owlcarousel/LICENSE`) |
| jsVectorMap | 1.7.0 | `vector-map.html` | MIT, https://github.com/themustafaomar/jsvectormap (`jsvectormap/LICENSE`) |

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

Phase 5 memakai file distribusi lokal untuk tiap grafik. Versi ApexCharts
dipin pada rilis berlisensi MIT; versi terkini memiliki ketentuan distribusi
berbeda. amCharts 4 memakai file browser resmi dan menampilkan logo bawaan
sesuai lisensi gratis. Morris.js diambil dari commit upstream yang memperbaiki
injeksi label tooltip (rilis npm 0.5.0 belum memuat patch). Semua angka grafik
adalah data ilustratif dan tidak memerlukan layanan eksternal.

Phase 6 menyediakan CSS dan webfont Font Awesome Free, Material Icons, dan
Weather Icons hanya di halaman terkait. Ionicons dan Feather memakai 24 SVG
resmi terpilih masing-masing; keduanya tidak memerlukan runtime eksternal.
Halaman Feather memakai `assets/js/feather-data.js` hasil generator untuk
menyalin SVG lengkap tanpa fetch, termasuk saat template dibuka langsung
dengan `file://`. Ikon sidebar BRUTAL. tetap memakai SVG template tersendiri.

Phase 7 memakai GLightbox sebagai pengganti LightGallery untuk demo lightbox.
Lisensi LightGallery meminta lisensi komersial untuk themes/templates,
sedangkan GLightbox tersedia di bawah MIT. Owl Carousel 2.3.4 tetap mengikuti
rencana dan dimuat bersama jQuery hanya di halaman demonya. Bootstrap Carousel,
galeri masonry, dan timeline memakai CSS/JavaScript template tanpa plugin baru.

Phase 8 memakai jsVectorMap lokal untuk peta dunia. Google Maps dimuat hanya setelah pengunjung memasukkan API key browser; Google Maps JavaScript API tidak dibundel.

Component fixes menambahkan Flatpickr 4.6.13 (MIT, https://github.com/flatpickr/flatpickr). Distribusi JS/CSS, locale `id.js`, dan `LICENSE.md` berada di `flatpickr/`. Versi dikunci di package.json; file vendor tidak dimodifikasi. Kontrol global memakai `assets/js/controls.js` dan `assets/css/controls.css`.
