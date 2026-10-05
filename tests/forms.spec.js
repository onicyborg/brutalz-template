const { choose } = require('./helpers/controls');
const { test, expect } = require('@playwright/test');

test('form overview and sidebar link to every Phase 3 page', async ({ page }) => {
  await page.goto('/forms.html');
  for (const name of ['basic-form', 'forms-advanced-form', 'forms-editor', 'forms-validation', 'form-wizard']) {
    await expect(page.locator(`main a[href="${name}.html"]`)).toBeVisible();
    await expect(page.locator(`#sidebar a[href="${name}.html"]`)).toHaveCount(1);
  }
});

test('Select2 searches options and advanced brief validates before summarizing', async ({ page }) => {
  await page.goto('/forms-advanced-form.html');
  await expect(page.locator('#advancedForm .select2-container')).toHaveCount(2);
  await page.getByRole('button', { name: 'Lihat ringkasan' }).click();
  await expect(page.locator('#advancedResult')).toContainText('Periksa kolom wajib');
  await page.locator('#advancedName').fill('Portal kreatif');
  await page.getByLabel('Email kontak').fill('alex@studio.id');
  await page.locator('#advancedTeam + .select2-container').click();
  await page.locator('.select2-search__field').last().fill('Engineering');
  await page.getByRole('option', { name: 'Tim Engineering' }).click();
  await page.getByRole('button', { name: 'Lihat ringkasan' }).click();
  await expect(page.locator('#advancedResult')).toContainText('Portal kreatif');
  await expect(page.locator('#advancedResult')).toContainText('Tim Engineering');
});

test('Quill Snow and Bubble editors work and preview uses plain text', async ({ page }) => {
  await page.goto('/forms-editor.html');
  await expect(page.locator('#editorSnow .ql-editor')).toBeVisible();
  await expect(page.locator('#editorBubble .ql-editor')).toBeVisible();
  await expect(page.locator('.ql-toolbar.ql-snow .ql-bold')).toBeVisible();
  await page.locator('#editorSnow .ql-editor').fill('Ide <kuat>');
  await page.getByRole('button', { name: 'Lihat hasil' }).click();
  await expect(page.locator('#editorOutput')).toHaveText('Ide <kuat>');
  await expect(page.locator('#editorOutput img')).toHaveCount(0);
  await page.getByRole('button', { name: 'Kosongkan' }).click();
  await expect(page.locator('#editorOutput')).toHaveText('Editor masih kosong.');
});

test('native validation shows field feedback and accepts valid values', async ({ page }) => {
  await page.goto('/forms-validation.html');
  await page.getByRole('button', { name: 'Periksa data' }).click();
  await expect(page.locator('#validationName')).toHaveClass(/is-invalid/);
  await expect(page.locator('#validationResult')).toContainText('Periksa kolom');
  await page.getByLabel('Nama lengkap').fill('Alex Darma');
  await page.getByLabel('Email', { exact: true }).fill('alex@example.com');
  await page.getByLabel('Kode kampanye').fill('abc-123');
  await expect(page.locator('#validationCode')).toHaveClass(/is-invalid/);
  await page.getByLabel('Kode kampanye').fill('ABC-123');
  await page.getByLabel('Jumlah peserta').fill('51');
  await expect(page.locator('#validationBudget')).toHaveClass(/is-invalid/);
  await page.getByLabel('Jumlah peserta').fill('12');
  await page.getByLabel('Saya memahami ini hanya demonstrasi.').check();
  await page.getByRole('button', { name: 'Periksa data' }).click();
  await expect(page.locator('#validationResult')).toContainText('Alex Darma valid');
  await page.getByRole('button', { name: 'Reset' }).click();
  await expect(page.locator('#validationName')).not.toHaveClass(/is-valid|is-invalid/);
});

test('wizard blocks invalid steps, reviews values, completes and restarts', async ({ page }) => {
  await page.goto('/form-wizard.html');
  const next = page.locator('#formWizard .actions a').filter({ hasText: 'Lanjut' });
  await next.click();
  await expect(page.locator('#wizardName')).toHaveClass(/is-invalid/);
  await expect(page.locator('#wizardEmail')).not.toBeVisible();
  await page.getByLabel('Nama lengkap').fill('Nina Sari');
  await page.getByLabel('Nomor telepon').fill('+62 812 3456 7890');
  await next.click();
  await expect(page.locator('#wizardEmail')).toBeVisible();
  await page.getByLabel('Email akun').fill('nina@example.com');
  await choose(page, page.getByLabel('Peran'), 'Designer');
  await next.click();
  await expect(page.locator('#reviewName')).toHaveText('Nina Sari');
  await expect(page.locator('#reviewEmail')).toHaveText('nina@example.com');
  await next.click();
  await expect(page.locator('#wizardAgree')).toHaveClass(/is-invalid/);
  await page.getByLabel('Data contoh di atas sudah benar.').check();
  await next.click();
  await expect(page.locator('#wizardStatus')).toContainText('Selesai!');
  await page.getByRole('button', { name: 'Ulangi demo' }).click();
  await expect(page.locator('#wizardName')).toBeVisible();
  await expect(page.locator('#wizardName')).toHaveValue('');
});
