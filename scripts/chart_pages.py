"""Phase 5 chart pages. Demo data is illustrative and local to each page."""

CHART_PAGES = (
    'chart-chartjs', 'chart-apexchart', 'chart-amchart',
    'chart-echart', 'chart-sparkline', 'chart-morris',
)


def demo_cards(items, kind='div'):
    cards = []
    for element_id, title, description in items:
        chart = (f'<canvas id="{element_id}" role="img" aria-label="{title}: data ilustratif"></canvas>'
                 if kind == 'canvas' else
                 f'<div id="{element_id}" class="chart-demo" role="img" aria-label="{title}: data ilustratif"></div>')
        cards.append(
            '<div class="col-xl-6"><section class="card h-100">'
            f'<div class="card-body"><h2>{title}</h2><p class="small text-muted">{description}</p>'
            f'<div class="chart-demo-wrap">{chart}</div></div></section></div>'
        )
    return '<div class="row g-4">' + ''.join(cards) + '</div>'


def build_chart_pages(heading, stats, chart_panel, source_panel, card):
    overview_items = [
        ('chart-chartjs', 'Chart.js', 'Line, bar, doughnut, pie, radar, dan mixed chart.', 'bg-yellow'),
        ('chart-apexchart', 'ApexCharts', 'Area, column, pie, radial, dan heatmap.', 'bg-purple'),
        ('chart-amchart', 'amCharts 4', 'Bar, pie, dan line chart dengan branding bawaan.', 'bg-green'),
        ('chart-echart', 'Apache ECharts', 'Line, bar, pie, scatter, dan candlestick.', 'bg-orange'),
        ('chart-sparkline', 'Sparkline', 'Grafik kecil untuk ringkasan statistik.', 'bg-blue'),
        ('chart-morris', 'Morris.js', 'Line, area, bar, dan donut berbasis SVG.', 'bg-purple'),
    ]
    overview = heading('Setiap angka punya cerita.', 'Enam pilihan pustaka grafik dengan data contoh dan warna BRUTAL.')
    overview += '<div class="row g-4">' + ''.join(
        f'<div class="col-md-6 col-xl-4"><a class="card chart-index-card h-100 text-decoration-none text-dark" href="{slug}.html"><div class="card-body"><span class="badge {color} mb-3">{name}</span><h2 class="fs-4">{name} →</h2><p class="text-muted mb-0">{description}</p></div></a></div>'
        for slug, name, description, color in overview_items
    ) + '</div><p class="small text-muted mt-4">Semua angka pada showcase ini adalah data ilustratif; halaman bekerja tanpa API atau CDN.</p>'

    chartjs = heading('Chart.js, dengan gaya sendiri.', 'Enam jenis grafik interaktif dan showcase SVG yang sudah ada.')
    chartjs += stats() + f'<div class="dashboard-grid mt-4">{chart_panel()}{source_panel()}</div>'
    chartjs += card(
        'Aktivitas workspace',
        '<div class="mt-4">' + ''.join(
            f'<div class="timeline-item"><h3>{title}</h3><p class="small text-muted mb-0">{detail}</p></div>'
            for title, detail in [
                ('Website studio masuk tahap review', 'Hari ini, 09.30 · oleh Alex Darma'),
                ('Brand identity diselesaikan', 'Kemarin, 16.45 · oleh Nina Sari'),
                ('Proyek baru ditambahkan', '25 September, 10.00 · oleh Rio Kurnia'),
            ]
        ) + '</div>',
        'mt-4 mb-4',
    )
    chartjs += demo_cards([
        ('chartjsLine', 'Line chart', 'Tren pendapatan selama enam bulan.'),
        ('chartjsBar', 'Bar chart', 'Perbandingan progres per kanal.'),
        ('chartjsDoughnut', 'Doughnut chart', 'Komposisi sumber kunjungan.'),
        ('chartjsPie', 'Pie chart', 'Pembagian status proyek.'),
        ('chartjsRadar', 'Radar chart', 'Profil keterampilan tim kreatif.'),
        ('chartjsMixed', 'Mixed chart', 'Pendapatan dan target dalam satu bidang.'),
    ], 'canvas')

    apex = heading('ApexCharts, banyak sudut pandang.', 'Garis halus, kolom tegas, dan peta intensitas dengan palet Neubrutalism.')
    apex += demo_cards([
        ('apexArea', 'Area line', 'Pergerakan kunjungan mingguan.'),
        ('apexColumn', 'Column', 'Hasil kampanye menurut kanal.'),
        ('apexPie', 'Pie', 'Porsi pekerjaan per disiplin.'),
        ('apexRadial', 'Radial bar', 'Tingkat penyelesaian proyek.'),
        ('apexHeatmap', 'Heatmap', 'Intensitas aktivitas tim selama sepekan.'),
    ])

    amcharts = heading('amCharts 4, data yang bercerita.', 'Bar, pie, dan line chart lokal dengan branding pustaka tetap tampil.')
    amcharts += demo_cards([
        ('amBar', 'Bar chart', 'Volume pekerjaan per tim.'),
        ('amPie', 'Pie chart', 'Distribusi kategori proyek.'),
        ('amLine', 'Line chart', 'Perubahan pendapatan ilustratif.'),
    ])

    echarts = heading('Apache ECharts, banyak kemungkinan.', 'Lima cara melihat data, dari tren sederhana hingga candlestick.')
    echarts += demo_cards([
        ('echLine', 'Line chart', 'Tren pendapatan dan target.'),
        ('echBar', 'Bar chart', 'Jumlah proyek per kategori.'),
        ('echPie', 'Pie chart', 'Sumber pengunjung.'),
        ('echScatter', 'Scatter chart', 'Hubungan waktu dan hasil.'),
        ('echCandle', 'Candlestick', 'Ilustrasi rentang nilai harian.'),
    ])

    spark = heading('Kecil, tapi bercerita.', 'Sparkline menambahkan konteks visual ke kartu statistik tanpa mengambil banyak ruang.')
    spark_items = [
        ('sparkLine', 'Pendapatan', 'Rp48,5 jt', 'Line', 'bg-purple'),
        ('sparkBar', 'Proyek baru', '24', 'Bar', 'bg-yellow'),
        ('sparkTristate', 'Momentum', '+18,6%', 'Tristate', 'bg-green'),
        ('sparkPie', 'Konversi', '4,82%', 'Pie', 'bg-orange'),
    ]
    spark += '<div class="row g-4">' + ''.join(
        f'<div class="col-md-6"><section class="card h-100"><div class="card-body {color}">'
        f'<span class="badge bg-white text-dark mb-3">{kind}</span><h2 class="fs-5">{title}</h2>'
        f'<div class="chart-spark-value">{value}</div><div class="sparkline-wrap">'
        f'<span id="{element_id}" class="sparkline" role="img" aria-label="Sparkline {kind.lower()} {title.lower()} dengan data ilustratif"></span>'
        '</div></div></section></div>'
        for element_id, title, value, kind, color in spark_items
    ) + '</div>'

    morris = heading('Morris.js, klasik yang tetap jelas.', 'Empat grafik SVG lokal berbasis jQuery dan Raphael.')
    morris += demo_cards([
        ('morrisLine', 'Line chart', 'Pendapatan dan target bulanan.'),
        ('morrisArea', 'Area chart', 'Volume dua jenis pekerjaan.'),
        ('morrisBar', 'Bar chart', 'Proyek selesai dan berjalan.'),
        ('morrisDonut', 'Donut chart', 'Komposisi kategori layanan.'),
    ])

    return {
        'charts': overview,
        'chart-chartjs': chartjs,
        'chart-apexchart': apex,
        'chart-amchart': amcharts,
        'chart-echart': echarts,
        'chart-sparkline': spark,
        'chart-morris': morris,
    }
