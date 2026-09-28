/* Phase 5 chart demos. All data is illustrative and bundled locally. */
(() => {
  'use strict';
  const palette = {
    ink: '#232420', purple: '#c4a8f5', green: '#c7e8cc',
    yellow: '#f9de6e', orange: '#f7b68b', blue: '#b8dcef',
  };
  const colors = [palette.purple, palette.green, palette.yellow, palette.orange, palette.blue];
  const months = ['Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep'];
  const amount = [8, 11, 9, 16, 14, 20];
  const target = [5, 8, 7, 11, 9, 14];

  if (document.querySelector('#chartjsLine')) {
    const base = {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { labels: { color: palette.ink, font: { weight: 'bold' } } } },
      scales: { x: { ticks: { color: palette.ink } }, y: { beginAtZero: true, ticks: { color: palette.ink } } },
    };
    const make = (id, type, data, options = base) => new Chart(document.getElementById(id), { type, data, options });
    make('chartjsLine', 'line', { labels: months, datasets: [
      { label: 'Pendapatan · jt', data: amount, borderColor: palette.ink, backgroundColor: palette.purple, tension: .35, fill: true },
      { label: 'Target · jt', data: target, borderColor: palette.green, borderWidth: 3, tension: .35 },
    ] });
    make('chartjsBar', 'bar', { labels: ['Organik', 'Sosial', 'Referral', 'Email'], datasets: [
      { label: 'Kunjungan', data: [48, 32, 20, 27], backgroundColor: colors, borderColor: palette.ink, borderWidth: 2 },
    ] });
    const circleOptions = { responsive: true, maintainAspectRatio: false,
      plugins: { legend: { position: 'bottom', labels: { color: palette.ink } } } };
    make('chartjsDoughnut', 'doughnut', { labels: ['Organik', 'Langsung', 'Referral'], datasets: [
      { data: [48, 32, 20], backgroundColor: colors.slice(0, 3), borderColor: palette.ink, borderWidth: 2 },
    ] }, circleOptions);
    make('chartjsPie', 'pie', { labels: ['Berjalan', 'Review', 'Selesai', 'Rencana'], datasets: [
      { data: [12, 6, 4, 2], backgroundColor: colors.slice(0, 4), borderColor: palette.ink, borderWidth: 2 },
    ] }, circleOptions);
    make('chartjsRadar', 'radar', { labels: ['Desain', 'Riset', 'Frontend', 'Konten', 'Strategi'], datasets: [
      { label: 'Tim kreatif', data: [88, 65, 74, 82, 71], borderColor: palette.ink, backgroundColor: '#c4a8f588', pointBackgroundColor: palette.ink },
    ] }, { responsive: true, maintainAspectRatio: false,
      plugins: { legend: { labels: { color: palette.ink } } },
      scales: { r: { suggestedMin: 0, suggestedMax: 100, pointLabels: { color: palette.ink } } },
    });
    make('chartjsMixed', 'bar', { labels: months, datasets: [
      { type: 'bar', label: 'Pendapatan · jt', data: amount, backgroundColor: palette.purple, borderColor: palette.ink, borderWidth: 2 },
      { type: 'line', label: 'Target · jt', data: target, borderColor: palette.ink, borderWidth: 3, tension: .25 },
    ] });
  }

  if (document.querySelector('#apexArea')) {
    const common = { chart: { height: 250, toolbar: { show: false }, foreColor: palette.ink,
      fontFamily: 'system-ui, sans-serif', animations: { enabled: false } },
      colors, dataLabels: { enabled: false }, grid: { borderColor: '#deded8' },
      stroke: { width: 3, curve: 'smooth' }, legend: { position: 'bottom' } };
    const render = (id, options) => new ApexCharts(document.querySelector(`#${id}`),
      { ...common, ...options, chart: { ...common.chart, ...options.chart } }).render();
    render('apexArea', { chart: { type: 'area' }, series: [{ name: 'Kunjungan', data: [24, 31, 28, 39, 35, 48] }],
      xaxis: { categories: months }, fill: { type: 'solid', opacity: .55 } });
    render('apexColumn', { chart: { type: 'bar' }, plotOptions: { bar: { borderRadius: 3, columnWidth: '50%' } },
      series: [{ name: 'Klik', data: [38, 29, 17, 22] }], xaxis: { categories: ['Organik', 'Sosial', 'Referral', 'Email'] } });
    render('apexPie', { chart: { type: 'pie' }, series: [42, 30, 18, 10],
      labels: ['Desain', 'Engineering', 'Konten', 'Riset'], legend: { position: 'bottom' } });
    render('apexRadial', { chart: { type: 'radialBar' }, series: [76, 58, 91], labels: ['Desain', 'Dev', 'Konten'],
      plotOptions: { radialBar: { dataLabels: { total: { show: true, label: 'Progres' } } } } });
    render('apexHeatmap', { chart: { type: 'heatmap' }, series: [
      { name: 'Sen', data: [15, 27, 39, 18, 30].map((y, x) => ({ x: `${x + 8}.00`, y })) },
      { name: 'Sel', data: [22, 34, 26, 41, 19].map((y, x) => ({ x: `${x + 8}.00`, y })) },
      { name: 'Rab', data: [18, 29, 43, 31, 24].map((y, x) => ({ x: `${x + 8}.00`, y })) },
    ], plotOptions: { heatmap: { colorScale: { ranges: [
      { from: 0, to: 20, color: palette.blue }, { from: 21, to: 35, color: palette.purple },
      { from: 36, to: 50, color: palette.orange },
    ] } } } });
  }

  if (document.querySelector('#amBar')) {
    am4core.options.autoDispose = true;
    const bar = am4core.create('amBar', am4charts.XYChart);
    bar.colors.list = colors.map(am4core.color);
    bar.data = [{ team: 'Desain', value: 12 }, { team: 'Produk', value: 9 },
      { team: 'Konten', value: 7 }, { team: 'Engineering', value: 10 }];
    const barCategory = bar.yAxes.push(new am4charts.CategoryAxis());
    barCategory.dataFields.category = 'team';
    barCategory.renderer.inversed = true;
    const barValue = bar.xAxes.push(new am4charts.ValueAxis());
    barValue.min = 0;
    const columns = bar.series.push(new am4charts.ColumnSeries());
    columns.dataFields.valueX = 'value';
    columns.dataFields.categoryY = 'team';
    columns.columns.template.tooltipText = '{categoryY}: {valueX} proyek';
    columns.columns.template.fill = am4core.color(palette.purple);
    columns.columns.template.stroke = am4core.color(palette.ink);
    columns.columns.template.strokeWidth = 2;

    const pie = am4core.create('amPie', am4charts.PieChart);
    pie.colors.list = colors.map(am4core.color);
    pie.data = [{ category: 'Website', value: 42, color: palette.purple },
      { category: 'Branding', value: 28, color: palette.green },
      { category: 'Mobile', value: 18, color: palette.yellow },
      { category: 'Marketing', value: 12, color: palette.orange }];
    const slices = pie.series.push(new am4charts.PieSeries());
    slices.dataFields.category = 'category';
    slices.dataFields.value = 'value';
    slices.slices.template.propertyFields.fill = 'color';
    slices.slices.template.stroke = am4core.color(palette.ink);
    slices.slices.template.strokeWidth = 2;
    pie.legend = new am4charts.Legend();

    const line = am4core.create('amLine', am4charts.XYChart);
    line.colors.list = colors.map(am4core.color);
    line.data = months.map((month, index) => ({ month, value: amount[index] }));
    const lineCategory = line.xAxes.push(new am4charts.CategoryAxis());
    lineCategory.dataFields.category = 'month';
    line.yAxes.push(new am4charts.ValueAxis());
    const series = line.series.push(new am4charts.LineSeries());
    series.dataFields.valueY = 'value';
    series.dataFields.categoryX = 'month';
    series.stroke = am4core.color(palette.ink);
    series.strokeWidth = 3;
    series.tooltipText = '{categoryX}: {valueY} jt';
    series.bullets.push(new am4charts.CircleBullet());
    line.cursor = new am4charts.XYCursor();
  }

  if (document.querySelector('#echLine')) {
    const instances = [];
    const render = (id, option) => {
      const instance = echarts.init(document.getElementById(id));
      instance.setOption({ color: colors, textStyle: { color: palette.ink, fontFamily: 'system-ui' }, ...option });
      instances.push(instance);
    };
    render('echLine', { tooltip: { trigger: 'axis' }, legend: { bottom: 0 }, grid: { left: 35, right: 20, top: 20, bottom: 55 },
      xAxis: { type: 'category', data: months }, yAxis: { type: 'value' },
      series: [{ name: 'Pendapatan', type: 'line', smooth: true, data: amount, areaStyle: {} },
        { name: 'Target', type: 'line', smooth: true, data: target }] });
    render('echBar', { tooltip: {}, grid: { left: 35, right: 20, top: 20, bottom: 35 },
      xAxis: { type: 'category', data: ['Website', 'Branding', 'Mobile', 'Marketing'] }, yAxis: { type: 'value' },
      series: [{ type: 'bar', data: [14, 9, 6, 8], itemStyle: { borderColor: palette.ink, borderWidth: 2 } }] });
    render('echPie', { tooltip: { trigger: 'item' }, legend: { bottom: 0 },
      series: [{ type: 'pie', radius: '60%', data: [
        { name: 'Organik', value: 48 }, { name: 'Langsung', value: 32 }, { name: 'Referral', value: 20 },
      ], itemStyle: { borderColor: palette.ink, borderWidth: 2 } }] });
    render('echScatter', { tooltip: { trigger: 'item' }, grid: { left: 35, right: 20, top: 20, bottom: 35 },
      xAxis: { type: 'value', name: 'Jam' }, yAxis: { type: 'value', name: 'Hasil' },
      series: [{ type: 'scatter', symbolSize: 16, data: [[2, 12], [3, 17], [4, 16], [5, 25], [6, 28], [7, 35]] }] });
    render('echCandle', { tooltip: { trigger: 'axis' }, grid: { left: 35, right: 20, top: 20, bottom: 35 },
      xAxis: { type: 'category', data: ['Sen', 'Sel', 'Rab', 'Kam', 'Jum'] }, yAxis: { type: 'value', scale: true },
      series: [{ type: 'candlestick', data: [[12, 18, 10, 21], [18, 15, 13, 20],
        [15, 22, 14, 25], [22, 20, 18, 24], [20, 27, 19, 30]],
      itemStyle: { color: palette.green, color0: palette.orange, borderColor: palette.ink, borderColor0: palette.ink } }] });
    window.addEventListener('resize', () => instances.forEach(instance => instance.resize()));
  }

  if (document.querySelector('#sparkLine')) {
    const jq = window.jQuery;
    jq('#sparkLine').sparkline([8, 12, 10, 15, 13, 19, 18, 24],
      { type: 'line', width: '100%', height: 68, lineColor: palette.ink, fillColor: '#ffffff88', lineWidth: 3, spotColor: palette.ink });
    jq('#sparkBar').sparkline([4, 7, 5, 9, 6, 11, 8, 13],
      { type: 'bar', width: '100%', height: 68, barColor: palette.ink, barWidth: 14, barSpacing: 6 });
    jq('#sparkTristate').sparkline([1, -1, 1, 0, 1, 1, -1, 1],
      { type: 'tristate', width: '100%', height: 68, posBarColor: palette.ink, negBarColor: '#e57868', zeroBarColor: '#ffffff' });
    jq('#sparkPie').sparkline([48, 32, 20],
      { type: 'pie', width: 74, height: 74, sliceColors: [palette.purple, palette.ink, palette.green], borderColor: palette.ink, borderWidth: 2 });
  }

  if (document.querySelector('#morrisLine')) {
    const base = { resize: true, gridTextColor: palette.ink, gridLineColor: '#deded8',
      hideHover: 'auto', parseTime: false };
    const data = months.map((period, index) => ({ period, income: amount[index], target: target[index] }));
    new Morris.Line({ ...base, element: 'morrisLine', data, xkey: 'period', ykeys: ['income', 'target'],
      labels: ['Pendapatan', 'Target'], lineColors: [palette.purple, palette.ink], lineWidth: 3, pointSize: 4 });
    new Morris.Area({ ...base, element: 'morrisArea', data: [
      { period: 'Apr', design: 5, dev: 3 }, { period: 'Mei', design: 7, dev: 4 },
      { period: 'Jun', design: 6, dev: 6 }, { period: 'Jul', design: 9, dev: 7 },
      { period: 'Agu', design: 8, dev: 9 }, { period: 'Sep', design: 11, dev: 10 },
    ], xkey: 'period', ykeys: ['design', 'dev'], labels: ['Desain', 'Engineering'],
    lineColors: [palette.purple, palette.green] });
    new Morris.Bar({ ...base, element: 'morrisBar', data: [
      { period: 'Apr', done: 4, active: 6 }, { period: 'Mei', done: 6, active: 7 },
      { period: 'Jun', done: 7, active: 5 }, { period: 'Jul', done: 9, active: 8 },
    ], xkey: 'period', ykeys: ['done', 'active'], labels: ['Selesai', 'Berjalan'],
    barColors: [palette.green, palette.purple] });
    new Morris.Donut({ element: 'morrisDonut', resize: true, colors: colors.slice(0, 4),
      data: [{ label: 'Website', value: 42 }, { label: 'Branding', value: 28 },
        { label: 'Mobile', value: 18 }, { label: 'Marketing', value: 12 }] });
  }
})();
