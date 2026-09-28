const { test, expect } = require('@playwright/test');

const iconPages = ['icon-font-awesome', 'icon-material', 'icon-ionicons', 'icon-feather', 'icon-weather-icon'];

test('five icon pages are available in the sidebar with local previews', async ({ page }) => {
  await page.goto('/icon-font-awesome.html');
  for (const name of iconPages) {
    await expect(page.locator(`#sidebar a[href="${name}.html"]`)).toHaveCount(1);
    await page.goto(`/${name}.html`);
    await expect(page.locator('.icon-item')).toHaveCount(24);
    await expect(page.locator('.icon-preview').first()).toBeVisible();
  }
  await expect(page.locator('.icon-preview .wi').first()).toBeVisible();
  expect(await page.evaluate(() => getComputedStyle(document.querySelector('.icon-preview .wi'), '::before').content)).not.toBe('none');
});

test('icon font, material ligatures, and SVG collections load locally', async ({ page }) => {
  await page.goto('/icon-font-awesome.html');
  await expect(page.locator('.fa-solid').first()).toBeVisible();
  await expect(page.locator('.fa-regular').first()).toBeVisible();
  await expect(page.locator('.fa-brands').first()).toBeVisible();
  await page.evaluate(() => document.fonts.ready);
  expect(await page.evaluate(() => document.fonts.check('32px "Font Awesome 6 Free"'))).toBeTruthy();

  await page.goto('/icon-material.html');
  await page.evaluate(() => document.fonts.ready);
  expect(await page.evaluate(() => document.fonts.check('32px "Material Icons"'))).toBeTruthy();
  await page.goto('/icon-ionicons.html');
  await expect(page.locator('.icon-preview img')).toHaveCount(24);
  await page.goto('/icon-feather.html');
  await expect(page.locator('.icon-preview img')).toHaveCount(24);
});

test('search filters icons and copy button provides complete SVG markup', async ({ page, context }) => {
  await context.grantPermissions(['clipboard-read', 'clipboard-write']);
  await page.goto('/icon-feather.html');
  await page.getByLabel('Cari ikon di halaman ini').fill('Dashboard');
  await expect(page.locator('.icon-item:visible')).toHaveCount(1);
  await expect(page.locator('#iconCount')).toHaveText('1 dari 24 ikon tampil');
  await page.getByRole('button', { name: 'Salin kode Dashboard' }).click();
  await expect(page.locator('#iconCopyStatus')).toContainText('tersalin');
  const copied = await page.evaluate(() => navigator.clipboard.readText());
  expect(copied).toContain('<svg');
  expect(copied).toContain('<rect');
  await page.getByLabel('Cari ikon di halaman ini').fill('tidak-ada');
  await expect(page.locator('#iconEmpty')).toBeVisible();
});
