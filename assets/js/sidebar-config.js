/* Single source for navigation and page search. Keep the assigned array valid JSON.
 * Add only implemented pages. Nested items may themselves contain children.
 */
window.BRUTAL_SIDEBAR = [
  {"group":"WORKSPACE","items":[
    {"page":"index","label":"Dashboard","icon":"grid"},
    {"page":"projects","label":"Proyek","icon":"folder"},
    {"page":"calendar","label":"Kalender","icon":"calendar"},
    {"id":"widgetsMenu","label":"Widgets","icon":"chart","children":[
      {"page":"widget-chart","label":"Chart Widgets"},
      {"page":"widget-data","label":"Data Widgets"}
    ]},
    {"id":"appsMenu","label":"Apps","icon":"grid","children":[
      {"page":"chat","label":"Chat"},
      {"page":"portfolio","label":"Portfolio"},
      {"page":"blog","label":"Blog"}
    ]},
    {"id":"emailMenu","label":"Email","icon":"mail","children":[
      {"page":"email-inbox","label":"Inbox"},
      {"page":"email-compose","label":"Compose"},
      {"page":"email-read","label":"Baca Email"}
    ]}
  ]},
  {"group":"BUILDING BLOCKS","items":[
    {"id":"uiComponentsMenu","label":"Komponen UI","icon":"layers","children":[
      {"page":"components","label":"Semua komponen"},
      {"page":"alert","label":"Alert"},
      {"page":"badge","label":"Badge"},
      {"page":"breadcrumb","label":"Breadcrumb"},
      {"page":"buttons","label":"Buttons"},
      {"page":"collapse","label":"Collapse"},
      {"page":"dropdown","label":"Dropdown"},
      {"page":"checkbox-and-radio","label":"Checkbox & Radios"},
      {"page":"list-group","label":"List Group"},
      {"page":"media-object","label":"Media Object"},
      {"page":"navbar","label":"Navbar"},
      {"page":"pagination","label":"Pagination"},
      {"page":"popover","label":"Popover"},
      {"page":"progress","label":"Progress"},
      {"page":"tooltip","label":"Tooltip"},
      {"page":"flags","label":"Flag"},
      {"page":"typography","label":"Typography"}
    ]},
    {"id":"advancedComponentsMenu","label":"Komponen Lanjutan","icon":"bolt","children":[
      {"page":"avatar","label":"Avatar"},
      {"page":"card","label":"Card"},
      {"page":"modal","label":"Modal"},
      {"page":"sweet-alert","label":"Sweet Alert"},
      {"page":"toastr","label":"Toastr"},
      {"page":"empty-state","label":"Empty State"},
      {"page":"multiple-upload","label":"Multiple Upload"},
      {"page":"tabs","label":"Tabs"},
      {"page":"pricing","label":"Pricing"}
    ]},
    {"id":"formsMenu","label":"Form & Validasi","icon":"form","children":[
      {"page":"forms","label":"Semua form"},
      {"page":"basic-form","label":"Form Dasar"},
      {"page":"forms-advanced-form","label":"Advanced Form"},
      {"page":"forms-editor","label":"Editor"},
      {"page":"forms-validation","label":"Validation"},
      {"page":"form-wizard","label":"Form Wizard"}
    ]},
    {"id":"tablesMenu","label":"Tabel Data","icon":"table","children":[
      {"page":"tables","label":"Semua tabel"},
      {"page":"basic-table","label":"Tabel Dasar"},
      {"page":"advance-table","label":"Advanced Table"},
      {"page":"datatables","label":"DataTables"},
      {"page":"export-table","label":"Export Table"},
      {"page":"editable-table","label":"Editable Table"}
    ]},
    {"id":"chartsMenu","label":"Grafik & Widget","icon":"chart","children":[
      {"page":"charts","label":"Semua grafik"},
      {"page":"chart-chartjs","label":"Chart.js"},
      {"page":"chart-apexchart","label":"ApexCharts"},
      {"page":"chart-amchart","label":"amCharts 4"},
      {"page":"chart-echart","label":"Apache ECharts"},
      {"page":"chart-sparkline","label":"Sparkline"},
      {"page":"chart-morris","label":"Morris.js"}
    ]},
    {"id":"iconsMenu","label":"Ikon","icon":"layers","children":[
      {"page":"icon-font-awesome","label":"Font Awesome"},
      {"page":"icon-material","label":"Material Icons"},
      {"page":"icon-ionicons","label":"Ionicons"},
      {"page":"icon-feather","label":"Feather Icons"},
      {"page":"icon-weather-icon","label":"Weather Icons"}
    ]}
  ]},
  {"group":"MEDIA","items":[
    {"id":"galleryMenu","label":"Galeri","icon":"grid","children":[
      {"page":"light-gallery","label":"Light Gallery"},
      {"page":"gallery1","label":"Gallery 2"}
    ]},
    {"id":"sliderMenu","label":"Slider","icon":"layers","children":[
      {"page":"carousel","label":"Bootstrap Carousel"},
      {"page":"owl-carousel","label":"Owl Carousel"}
    ]},
    {"page":"timeline","label":"Timeline","icon":"calendar"}
  ]},
  {"group":"HALAMAN","items":[
    {"page":"profile","label":"Profil & pengaturan","icon":"user"},
    {"page":"invoice","label":"Invoice","icon":"file"},
    {"id":"authMenu","label":"Autentikasi","icon":"lock","children":[
      {"page":"auth-login","label":"Login"},
      {"page":"auth-register","label":"Daftar"},
      {"page":"auth-forgot-password","label":"Lupa Password"}
    ]},
    {"id":"errorsMenu","label":"Errors","icon":"file","children":[
      {"page":"errors-404","label":"404"}
    ]}
  ]},
  {"group":"MULAI MEMBANGUN","items":[
    {"page":"blank","label":"Halaman kosong","icon":"code"},
    {"page":"docs","label":"Dokumentasi","icon":"book"}
  ]}
];
