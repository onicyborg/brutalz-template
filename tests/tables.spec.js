const { test, expect } = require('@playwright/test');
const { readFile } = require('node:fs/promises');

test('table overview links to each Phase 4 example', async ({ page }) => {
  await page.goto('/tables.html');
  for (const name of ['basic-table', 'advance-table', 'datatables', 'export-table', 'editable-table']) {
    await expect(page.locator(`main a[href="${name}.html"]`)).toBeVisible();
    await expect(page.locator(`#sidebar a[href="${name}.html"]`)).toHaveCount(1);
  }
});

test('advanced table sorts text and numeric columns in both directions', async ({ page }) => {
  await page.goto('/advance-table.html');
  const body = page.locator('#advancedTable tbody');
  await page.locator('#advancedTable thead button').filter({ hasText: 'Anggaran' }).click();
  await expect(body.locator('tr').first()).toContainText('PRJ-111');
  await expect(page.locator('#advancedTable th').nth(4)).toHaveAttribute('aria-sort', 'ascending');
  await page.locator('#advancedTable thead button').filter({ hasText: 'Anggaran' }).click();
  await expect(body.locator('tr').first()).toContainText('PRJ-103');
  await page.locator('#advancedTable thead button').filter({ hasText: 'Proyek' }).click();
  await expect(body.locator('tr').first()).toContainText('Acme identity');
});

test('DataTables searches, paginates, reports count, and sorts multiple columns', async ({ page }) => {
  await page.goto('/datatables.html');
  const wrapper = page.locator('#dataTableDemo_wrapper');
  await expect(wrapper.locator('tbody tr')).toHaveCount(5);
  await expect(wrapper.locator('.dt-info')).toContainText('12 data');
  await wrapper.locator('.dt-search input').fill('Website');
  await expect(wrapper.locator('tbody tr')).toHaveCount(4);
  await expect(wrapper.locator('.dt-info')).toContainText('4 data');
  await wrapper.locator('.dt-search input').fill('');
  await wrapper.locator('th').filter({ hasText: 'Kategori' }).click();
  await wrapper.locator('th').filter({ hasText: 'Status' }).click({ modifiers: ['Shift'] });
  await expect(wrapper.locator('th').filter({ hasText: 'Kategori' })).toHaveAttribute('aria-sort', 'ascending');
  await wrapper.locator('.dt-paging button').filter({ hasText: '2' }).click();
  await expect(wrapper.locator('tbody tr')).toHaveCount(5);
});

test('Buttons exports filtered rows to Excel, CSV and PDF and opens print view', async ({ page }) => {
  await page.goto('/export-table.html');
  const wrapper = page.locator('#exportTableDemo_wrapper');
  await wrapper.locator('.dt-search input').fill('Acme');
  await expect(wrapper.locator('tbody tr')).toHaveCount(1);
  for (const [name, extension] of [['Excel', '.xlsx'], ['CSV', '.csv'], ['PDF', '.pdf']]) {
    const download = page.waitForEvent('download');
    await wrapper.getByRole('button', { name }).click();
    const file = await download;
    expect(file.suggestedFilename()).toContain(extension);
    const bytes = await readFile(await file.path());
    expect(bytes.length).toBeGreaterThan(100);
    if (extension === '.xlsx') expect(bytes.subarray(0, 2).toString()).toBe('PK');
    if (extension === '.pdf') expect(bytes.subarray(0, 4).toString()).toBe('%PDF');
    if (extension === '.csv') {
      expect(bytes.toString()).toContain('Acme identity');
      expect(bytes.toString()).not.toContain('Studio website');
    }
  }
  const popup = page.waitForEvent('popup');
  await wrapper.getByRole('button', { name: 'Print' }).click();
  const printPage = await popup;
  await expect(printPage.locator('body')).toContainText('Acme identity');
  await printPage.close();
});

test('editable cells validate, persist and reset without injecting markup', async ({ page }) => {
  await page.goto('/editable-table.html');
  const row = page.locator('#editableTable tr[data-record="PRJ-101"]');
  await row.getByRole('button', { name: 'Edit nama Studio website' }).click();
  const input = row.locator('.editable-input');
  await input.fill('');
  await input.press('Enter');
  await expect(input).toHaveClass(/is-invalid/);
  await input.fill('<b>Studio baru</b>');
  await row.getByRole('button', { name: 'Simpan' }).click();
  await expect(row.locator('[data-field="name"]')).toHaveText('<b>Studio baru</b>');
  await expect(row.locator('b')).toHaveCount(0);
  await page.reload();
  await expect(row.locator('[data-field="name"]')).toHaveText('<b>Studio baru</b>');
  await page.getByRole('button', { name: 'Pulihkan contoh' }).click();
  await expect(row.locator('[data-field="name"]')).toHaveText('Studio website');
});
