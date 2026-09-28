const { test, expect } = require('@playwright/test');
const pages = require('node:fs').readdirSync(require('node:path').resolve(__dirname,'..')).filter(name=>name.endsWith('.html')).map(name=>name.slice(0,-5));

test('all pages work on desktop and mobile without broken assets or page overflow', async ({ page }) => {
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  page.on('response', response => { if (response.status() >= 400) errors.push(`${response.status()} ${response.url()}`); });
  for (const width of [1440, 390, 320]) {
    await page.setViewportSize({ width, height: 900 });
    for (const name of pages) {
      await page.goto(`/${name}.html`);
      await expect(page.locator('h1')).toBeVisible();
      expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth), `${name} overflow at ${width}px`).toBeTruthy();
    }
  }
  expect(errors).toEqual([]);
});

test('project creation persists, filters, pagination, export and status work together', async ({ page }) => {
  await page.goto('/basic-table.html');
  await page.getByRole('button', {name:'Proyek baru'}).click();
  await page.getByLabel('Nama proyek', {exact:true}).fill('Website uji <studio>');
  await page.getByLabel('Tenggat', {exact:true}).fill('2026-12-15');
  await page.getByRole('button', {name:'Buat proyek',exact:true}).click();
  await expect(page.locator('#projectRows')).toContainText('Website uji <studio>');
  await page.reload();
  await page.getByLabel('Cari proyek').fill('Website uji');
  await expect(page.locator('#projectRows tr')).toHaveCount(1);
  await page.getByLabel('Filter status').selectOption('Selesai');
  await expect(page.locator('#projectRows')).toContainText('Tidak ada proyek');
  await page.getByLabel('Filter status').selectOption('');
  const downloadPromise = page.waitForEvent('download');
  await page.getByRole('button', {name:'CSV'}).click();
  expect((await downloadPromise).suggestedFilename()).toBe('brutal-proyek.csv');
  await page.getByLabel('Cari proyek').fill('');
  await page.getByRole('button', {name:'Halaman 2',exact:true}).click();
  await expect(page.locator('#tableCount')).toHaveText('6–9 dari 9 proyek');
  await page.goto('/projects.html');
  await page.getByLabel('Status Website uji <studio>').selectOption('Selesai');
  await expect(page.locator('.kanban-column').last()).toContainText('Website uji <studio>');
});

test('focus tasks survive reload and user markup stays plain text', async ({ page }) => {
  await page.goto('/index.html');
  await page.getByLabel('Tugas baru').fill('<img src=x onerror=alert(1)>');
  await page.getByRole('button', {name:'Tambah tugas',exact:true}).click();
  await expect(page.locator('#taskList img')).toHaveCount(0);
  await page.locator('#taskList input').last().check();
  await page.reload();
  await expect(page.locator('#taskList input').last()).toBeChecked();
  await expect(page.locator('#taskCount')).toHaveText('2/5');
});

test('Bootstrap tabs, modal, dropdown and form validation respond correctly', async ({ page }) => {
  await page.goto('/list-group.html');
  await page.getByRole('tab', {name:'Aktivitas',exact:true}).click();
  await expect(page.locator('#listPane1')).toBeVisible();
  await page.goto('/dropdown.html');
  await page.getByRole('button', {name:'Pilih aksi',exact:true}).click();
  await expect(page.locator('.component-preview .dropdown-menu.show').getByRole('link', {name:'Profil',exact:true})).toBeVisible();
  await page.keyboard.press('Escape');
  await page.goto('/components.html');
  await page.getByRole('button', {name:'Buka modal'}).click();
  await expect(page.locator('#projectModal')).toBeVisible();
  await page.locator('#projectModal').getByRole('button', {name:'Batal'}).click();
  await page.goto('/basic-form.html');
  await page.getByRole('button', {name:'Simpan data demo'}).click();
  await expect(page.locator('#formResult')).toContainText('Periksa kembali');
  await page.getByLabel('Nama depan').fill('Alex');
  await page.getByLabel('Nama belakang').fill('Darma');
  await page.getByLabel('Alamat email').fill('demo@example.com');
  await page.getByLabel('Peran', {exact:true}).selectOption('Developer');
  await page.getByLabel('Mulai bergabung').fill('2026-09-27');
  await page.getByLabel('Saya paham ini adalah form demonstrasi.').check();
  await page.getByRole('button', {name:'Simpan data demo'}).click();
  await expect(page.locator('#formResult')).toContainText('Data demo valid');
});

test('calendar event persists in the chosen month and chart changes period', async ({ page }) => {
  await page.goto('/calendar.html');
  await page.getByRole('button', {name:'Agenda baru'}).click();
  await page.getByLabel('Nama agenda').fill('Launch uji');
  await page.getByLabel('Tanggal', {exact:true}).fill('2026-11-18');
  await page.getByRole('button', {name:'Simpan agenda'}).click();
  await expect(page.locator('#calendarTitle')).toHaveText('November 2026');
  await expect(page.getByRole('button', {name:'Launch uji'})).toBeVisible();
  await page.getByRole('button', {name:'Launch uji'}).click();
  await expect(page.locator('#toastMessage')).toContainText('Launch uji');
  expect(await page.evaluate(() => JSON.parse(localStorage.getItem('brutal.events')).some(e => e.name==='Launch uji'))).toBeTruthy();
  await page.goto('/charts.html');
  await page.getByLabel('Periode grafik').selectOption('previous');
  await expect(page.locator('#chartTotal')).toHaveText('Rp63.000.000');
  await expect(page.locator('#revenueChartTitle')).toContainText('Okt–Mar');
});

test('mobile menu, keyboard search and profile preferences remain usable', async ({ page }) => {
  await page.setViewportSize({width:390,height:844});
  await page.goto('/index.html');
  await expect(page.locator('#sidebar')).toHaveAttribute('inert','');
  await page.getByRole('button', {name:'Buka navigasi'}).click();
  await expect(page.locator('#sidebarToggle')).toHaveAttribute('aria-expanded','true');
  await page.getByRole('link', {name:'Profil & pengaturan',exact:true}).first().click();
  await page.getByLabel('Nama lengkap').fill('Nina Sari');
  await page.getByRole('button', {name:'Simpan profil'}).click();
  await page.getByLabel('Tampilan lebih ringkas').check();
  await page.reload();
  await expect(page.locator('#profileDisplayName')).toHaveText('Nina Sari');
  await expect(page.locator('body')).toHaveClass('compact');
  await page.keyboard.press('Control+k');
  await page.getByRole('searchbox', {name:'Cari halaman',exact:true}).fill('invoice');
  await page.locator('#searchResults').getByRole('link', {name:/Invoice/}).click();
  await expect(page).toHaveURL(/invoice.html$/);
});

test('authentication demo redirects without persisting passwords; reset is explicitly simulated', async ({ page }) => {
  await page.goto('/auth-login.html');
  await page.getByLabel('Email', {exact:true}).fill('demo@example.com');
  await page.getByLabel('Password', {exact:true}).fill('demo-pass-123');
  await page.getByRole('button', {name:'Tampilkan password'}).click();
  await expect(page.locator('#authPassword')).toHaveAttribute('type','text');
  await page.getByRole('button', {name:'Masuk ke workspace'}).click();
  await expect(page).toHaveURL(/index.html$/);
  expect(await page.evaluate(() => JSON.stringify(localStorage))).not.toContain('demo-pass-123');
  await page.goto('/auth-forgot-password.html');
  await page.getByLabel('Email', {exact:true}).fill('demo@example.com');
  await page.getByRole('button', {name:'Coba reset password'}).click();
  await expect(page.locator('#authResult')).toContainText('Tidak ada email dikirim');
});
