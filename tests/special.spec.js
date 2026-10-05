const { choose } = require('./helpers/controls');
const { test, expect } = require('@playwright/test');

test('subscribe saves a demo address locally and handles duplicates', async ({ page }) => {
  await page.goto('/subscribe.html');
  await page.getByLabel('Alamat email').fill('hello@example.com');
  await page.getByRole('button', { name: 'Ikut daftar' }).click();
  await expect(page.locator('#subscribeStatus')).toContainText('demo lokal');
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('brutal.subscribers')))).toEqual(['hello@example.com']);
  await page.getByLabel('Alamat email').fill('hello@example.com');
  await page.getByRole('button', { name: 'Ikut daftar' }).click();
  await expect(page.locator('#subscribeStatus')).toContainText('sudah ada');
});

test('post editor creates a local draft and list filters without interpreting markup', async ({ page }) => {
  await page.goto('/create-post.html');
  await page.getByLabel('Judul post').fill('<img src=x onerror=alert(1)> Cerita Studio');
  await choose(page, page.locator('#postCategory'), 'Studio');
  await page.getByLabel('Tags').fill('proses, catatan');
  await page.locator('#postPublished').uncheck();
  await page.locator('#postEditor .ql-editor').fill('Ini cerita studio yang cukup panjang untuk tersimpan sebagai draft lokal.');
  await page.getByRole('button', { name: 'Simpan post' }).click();
  await expect(page).toHaveURL(/posts\.html\?created=1$/);
  await expect(page.locator('#postGrid .post-card')).toHaveCount(4);
  await expect(page.locator('#postGrid .post-card').first()).toContainText('Draft');
  await expect(page.locator('#postGrid .post-card').first()).toContainText('<img src=x onerror=alert(1)>');
  await expect(page.locator('#postGrid .post-card').first().locator('img')).toHaveCount(1);
  await page.getByLabel('Cari post').fill('catatan');
  await expect(page.locator('#postGrid .post-card')).toHaveCount(2);
  await choose(page, page.locator('#postFilter'), 'Studio');
  await expect(page.locator('#postGrid .post-card')).toHaveCount(2);
  await page.getByLabel('Cari post').fill('tidak ada hasil');
  await expect(page.locator('#postEmpty')).toBeVisible();
});

test('contact validates and previews without sending; error pages have working navigation', async ({ page }) => {
  await page.goto('/contact.html');
  await page.getByRole('button', { name: 'Pratinjau pesan' }).click();
  await expect(page.locator('#contactStatus')).toContainText('Periksa kolom');
  await page.getByLabel('Nama lengkap').fill('Alya');
  await page.getByLabel('Email').fill('alya@example.com');
  await choose(page, page.getByLabel('Topik'), 'Kolaborasi');
  await page.getByLabel('Pesan').fill('Saya ingin membahas proyek desain bersama.');
  await page.getByRole('button', { name: 'Pratinjau pesan' }).click();
  await expect(page.locator('#contactStatus')).toContainText('Pesan tidak dikirim');
  for (const code of ['403', '404', '500', '503']) {
    await page.goto(`/errors-${code}.html`);
    await expect(page.locator('h1')).toBeVisible();
    await expect(page.getByRole('link', { name: 'Kembali ke dashboard' })).toHaveAttribute('href', 'index.html');
  }
});

test('three-level sidebar keeps ancestors expanded and one active link', async ({ page }) => {
  await page.goto('/multilevel.html');
  for (const id of ['multilevelMenu', 'multilevelOne', 'multilevelTwo']) {
    await expect(page.locator(`#${id}`)).toHaveClass(/show/);
  }
  await expect(page.locator('#sidebar a[aria-current="page"]')).toHaveAttribute('href', 'multilevel.html');
  await page.locator('[aria-controls="multilevelTwo"]').click();
  await expect(page.locator('#multilevelTwo')).not.toBeVisible();
  await page.locator('[aria-controls="multilevelTwo"]').click();
  await expect(page.locator('#multilevelTwo')).toBeVisible();
});
