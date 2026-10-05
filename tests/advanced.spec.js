const { choose } = require('./helpers/controls');
const {test, expect} = require('@playwright/test');

test('advanced pages share the sidebar and expose the expected showcases', async ({page}) => {
  for (const name of ['avatar', 'card', 'modal', 'sweet-alert', 'toastr', 'empty-state', 'multiple-upload', 'tabs']) {
    await page.goto(`/${name}.html`);
    await expect(page.locator('#sidebar a[aria-current="page"]')).toHaveAttribute('href', `${name}.html`);
    await expect(page.locator('h1')).toBeVisible();
  }
  await page.goto('/avatar.html');
  await expect(page.locator('.avatar-example')).toHaveCount(8);
  await expect(page.locator('.avatar-status-dot')).toHaveCount(3);
  await page.goto('/card.html');
  await expect(page.locator('.advanced-color-card')).toHaveCount(4);
  await expect(page.locator('.advanced-image-card img')).toBeVisible();
});

test('Bootstrap modals cover sizes, scroll, form validation and delete confirmation', async ({page}) => {
  await page.goto('/modal.html');
  await page.getByRole('button', {name:'Extra large'}).click();
  await expect(page.locator('#modalExtraLarge')).toBeVisible();
  await page.locator('#modalExtraLarge').getByRole('button', {name:'Selesai'}).click();
  await page.getByRole('button', {name:'Scrollable'}).click();
  await expect(page.locator('#modalScrollable .modal-body')).toContainText('Bagian 14');
  await page.locator('#modalScrollable').getByRole('button', {name:'Tutup'}).first().click();
  await expect(page.locator('#modalScrollable')).not.toBeVisible();
  await page.getByRole('button', {name:'Buka form'}).click();
  await page.locator('#modalIdea').fill('Ide baru');
  await page.locator('#modalForm').getByRole('button', {name:'Simpan demo'}).click();
  await expect(page.locator('#modalFormResult')).toContainText('Ide baru');
  await page.getByRole('button', {name:'Hapus item'}).click();
  await page.getByRole('button', {name:'Ya, hapus'}).click();
  await expect(page.locator('#deleteDemoItem')).toBeHidden();
});

test('SweetAlert2 and Toastr launch from local bundles', async ({page}) => {
  await page.goto('/sweet-alert.html');
  await page.locator('[data-swal-demo="success"]').click();
  await expect(page.locator('.swal2-popup')).toContainText('Berhasil!');
  await page.locator('.swal2-confirm').click();
  await page.locator('[data-swal-demo="confirm"]').click();
  await page.locator('.swal2-cancel').click();
  await expect(page.locator('#sweetAlertResult')).toContainText('dibatalkan');
  await page.goto('/toastr.html');
  await page.locator('[data-toastr-demo="success"]').click();
  await expect(page.locator('#toast-container .toast-success')).toContainText('Berhasil');
  await choose(page, page.locator('#toastrPosition'), 'toast-bottom-left');
  await page.locator('[data-toastr-demo="warning"]').click();
  await expect(page.locator('#toast-container .toast-warning')).toContainText('Peringatan');
  await expect(page.locator('#toast-container')).toHaveClass(/toast-bottom-left/);
});

test('empty state changes locally and Bootstrap tab variants switch content', async ({page}) => {
  await page.goto('/empty-state.html');
  await page.locator('#emptyAdd').click();
  await expect(page.locator('#emptyDemo')).toContainText('Ide pertama');
  await page.locator('#emptyReset').click();
  await expect(page.locator('#emptyDemo')).toContainText('masih kosong');
  await page.goto('/tabs.html');
  for (const group of ['tabsTop', 'tabsBottom', 'tabsLeft', 'tabsRight', 'tabsIcon', 'tabsPills', 'tabsJustified']) {
    await page.locator(`#${group}-tab-1`).click();
    await expect(page.locator(`#${group}-pane-1`)).toBeVisible();
  }
});

test('Dropzone previews local files with progress and never requests an upload', async ({page}) => {
  const uploads = [];
  page.on('request', request => { if (request.url().includes('upload-disabled')) uploads.push(request.url()); });
  await page.goto('/multiple-upload.html');
  const png = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVQIHWP4z8DwHwAFgAI/ScL/nwAAAABJRU5ErkJggg==', 'base64');
  await page.locator('input.dz-hidden-input').setInputFiles({name:'contoh.png', mimeType:'image/png', buffer:png});
  await expect(page.locator('.dz-preview')).toHaveCount(1);
  await expect(page.locator('.upload-read-status')).toContainText('Pratinjau siap');
  await expect(page.locator('#uploadSummary')).toContainText('1 file');
  expect(uploads).toEqual([]);
  await page.locator('#uploadClear').click();
  await expect(page.locator('.dz-preview')).toHaveCount(0);
});
