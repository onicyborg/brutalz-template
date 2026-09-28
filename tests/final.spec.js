const { test, expect } = require('@playwright/test');
const fs = require('node:fs');
const path = require('node:path');

test('reset password demo validates confirmation and never stores a password', async ({ page }) => {
  await page.goto('/auth-reset-password.html');
  await page.getByLabel('Email', { exact: true }).fill('demo@example.com');
  await page.getByLabel('Password', { exact: true }).fill('new-password-123');
  await page.getByLabel('Konfirmasi password').fill('different-password');
  await page.getByRole('button', { name: 'Validasi password baru' }).click();
  await expect(page.locator('#authResult')).toContainText('belum sama');
  await page.getByLabel('Konfirmasi password').fill('new-password-123');
  await page.getByRole('button', { name: 'Validasi password baru' }).click();
  await expect(page.locator('#authResult')).toContainText('Tidak ada akun nyata');
  await expect(page.locator('#authPassword')).toHaveValue('');
  await expect(page.locator('#authConfirmPassword')).toHaveValue('');
  expect(await page.evaluate(() => JSON.stringify(localStorage))).not.toContain('new-password-123');
});

test('in-browser documentation lists every generated page and pinned libraries', async ({ page }) => {
  const pages = fs.readdirSync(path.resolve(__dirname, '..')).filter(name => name.endsWith('.html'));
  await page.goto('/docs.html');
  const links = await page.locator('#page-directory a').evaluateAll(elements => elements.map(element => element.getAttribute('href')));
  expect(links.sort()).toEqual(pages.sort());
  await expect(page.locator('#library-directory')).toContainText('Bootstrap 5.3.8');
  await expect(page.locator('#library-directory')).toContainText('Quill');
  await expect(page.locator('#library-directory')).toContainText('jsVectorMap');
  await expect(page.locator('#contributing')).toContainText('lowercase-kebab-case.html');
});

test('all pages keep their title, skip link, breadcrumb, search, and copyright consistent', async ({ page }) => {
  const root = path.resolve(__dirname, '..');
  const pages = fs.readdirSync(root).filter(name => name.endsWith('.html'));
  const titles = new Set();
  for (const file of pages) {
    await page.goto(`/${file}`);
    const title = await page.title();
    expect(title, file).toMatch(/ — BRUTAL\.$/);
    expect(titles.has(title), `Duplicate title: ${title}`).toBe(false);
    titles.add(title);
    await expect(page.locator('.skip-link[href="#main"]')).toHaveCount(1);
    await expect(page.locator('#searchModal')).toHaveCount(1);
    expect(await page.locator('body').textContent()).toContain('© 2026 BRUTAL.');
    if (!await page.locator('body.standalone-page').count()) {
      await expect(page.locator('.topbar .breadcrumb-item.active')).toHaveText(title.replace(' — BRUTAL.', ''));
      await expect(page.locator('.search-trigger')).toHaveCount(1);
    }
  }
  expect(titles.size).toBe(pages.length);
});
