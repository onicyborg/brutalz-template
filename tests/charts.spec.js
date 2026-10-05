const { choose } = require('./helpers/controls');
const { test, expect } = require('@playwright/test');

test('chart overview links to all six library demos', async ({ page }) => {
  await page.goto('/charts.html');
  for (const name of ['chart-chartjs', 'chart-apexchart', 'chart-amchart',
    'chart-echart', 'chart-sparkline', 'chart-morris']) {
    await expect(page.locator(`main a[href="${name}.html"]`)).toBeVisible();
    await expect(page.locator(`#sidebar a[href="${name}.html"]`)).toHaveCount(1);
  }
});

test('Chart.js renders six types alongside the migrated SVG showcase', async ({ page }) => {
  await page.goto('/chart-chartjs.html');
  await expect(page.locator('.chart-demo-wrap canvas')).toHaveCount(6);
  expect(await page.evaluate(() => ['chartjsLine', 'chartjsBar', 'chartjsDoughnut',
    'chartjsPie', 'chartjsRadar', 'chartjsMixed'].every(id => Chart.getChart(id)?.data.datasets.length))).toBeTruthy();
  await choose(page, page.getByLabel('Periode grafik'), 'previous');
  await expect(page.locator('#chartTotal')).toHaveText('Rp63.000.000');
  await expect(page.locator('#revenueChartTitle')).toContainText('Okt–Mar');
});

test('ApexCharts renders area, column, pie, radial and heatmap', async ({ page }) => {
  await page.goto('/chart-apexchart.html');
  for (const id of ['apexArea', 'apexColumn', 'apexPie', 'apexRadial', 'apexHeatmap']) {
    await expect(page.locator(`#${id} .apexcharts-svg`)).toBeVisible();
  }
});

test('amCharts 4 renders three chart types with required branding intact', async ({ page }) => {
  await page.goto('/chart-amchart.html');
  for (const id of ['amBar', 'amPie', 'amLine']) {
    await expect(page.locator(`#${id} svg`).first()).toBeVisible();
  }
  expect(await page.evaluate(() => window.am4core?.registry?.baseSprites?.length || 0)).toBeGreaterThanOrEqual(3);
  await expect(page.locator('#amBar svg title').filter({ hasText: 'Chart created using amCharts library' })).toHaveCount(1);
});

test('ECharts renders five types and handles viewport changes', async ({ page }) => {
  await page.goto('/chart-echart.html');
  for (const id of ['echLine', 'echBar', 'echPie', 'echScatter', 'echCandle']) {
    await expect(page.locator(`#${id} canvas`).first()).toBeVisible();
    expect(await page.evaluate(id => echarts.getInstanceByDom(document.getElementById(id))?.getOption().series.length, id)).toBeGreaterThan(0);
  }
  await page.setViewportSize({ width: 390, height: 844 });
  await expect(page.locator('#echCandle canvas').first()).toBeVisible();
});

test('Sparkline draws four miniature chart types in statistic cards', async ({ page }) => {
  await page.goto('/chart-sparkline.html');
  for (const id of ['sparkLine', 'sparkBar', 'sparkTristate', 'sparkPie']) {
    await expect(page.locator(`#${id} canvas`)).toBeVisible();
  }
});

test('Morris renders line, area, bar, and donut SVG charts', async ({ page }) => {
  await page.goto('/chart-morris.html');
  for (const id of ['morrisLine', 'morrisArea', 'morrisBar', 'morrisDonut']) {
    await expect(page.locator(`#${id} svg`)).toBeVisible();
  }
});
