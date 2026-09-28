const {test,expect}=require('@playwright/test');

test('chat changes conversations and persists plain-text messages without network delivery',async({page})=>{
  await page.goto('/chat.html');
  await page.locator('[data-chat-contact="rio"]').click();
  await expect(page.locator('#chatHeader')).toContainText('Rio Kurnia');
  await page.locator('#chatInput').fill('<img src=x onerror=alert(1)> Pesan uji');
  await page.locator('#chatForm button[type="submit"]').click();
  await expect(page.locator('.chat-message.mine')).toContainText('<img src=x onerror=alert(1)> Pesan uji');
  await expect(page.locator('#chatMessages img')).toHaveCount(0);
  await page.reload();
  await page.locator('[data-chat-contact="rio"]').click();
  await expect(page.locator('.chat-message.mine')).toContainText('Pesan uji');
  await page.getByLabel('Cari percakapan').fill('tidak-ada');
  await expect(page.locator('#chatContacts')).toContainText('Percakapan tidak ditemukan');
});

test('portfolio filtering and blog pagination/search open real local detail content',async({page})=>{
  await page.goto('/portfolio.html');
  await page.getByRole('button',{name:'Branding',exact:true}).click();
  await expect(page.locator('.portfolio-card:visible')).toHaveCount(2);
  await page.locator('.portfolio-card:visible a').first().click();
  await expect(page.locator('#portfolioModal')).toBeVisible();
  await expect(page.locator('#portfolioModalBody')).toContainText('Lingkup pekerjaan');
  await page.goto('/blog.html');
  await expect(page.locator('.blog-card:visible')).toHaveCount(3);
  await page.getByRole('button',{name:'Halaman artikel 2'}).click();
  await expect(page.locator('#blogCount')).toContainText('Halaman 2 dari 2');
  await page.getByLabel('Cari artikel').fill('Prototype');
  await expect(page.locator('.blog-card:visible')).toHaveCount(1);
  await page.locator('.blog-card:visible h2 a').click();
  await expect(page.locator('#articleModal .article-body')).toContainText('Pilih satu pertanyaan');
  await page.locator('#articleModal').getByRole('button',{name:'Tutup detail'}).click();
  await page.getByLabel('Cari artikel').fill('tidak-ada');
  await expect(page.locator('#blogCount')).toContainText('Tidak ada artikel');
});

test('mail search, selection, read state, star, trash and restore persist across pages',async({page})=>{
  await page.goto('/email-inbox.html');
  await page.getByLabel('Cari email').fill('Konsep website');
  await expect(page.locator('.mail-row')).toHaveCount(1);
  await page.getByLabel('Pilih semua',{exact:true}).check();
  await page.getByRole('button',{name:'Tandai dibaca',exact:true}).click();
  await expect(page.locator('.mail-row.unread')).toHaveCount(0);
  await page.locator('[data-mail-star="m1"]').click();
  await expect(page.locator('[data-mail-star="m1"]')).toHaveAttribute('aria-pressed','false');
  await page.getByLabel('Pilih semua',{exact:true}).check();
  await page.getByRole('button',{name:'Ke sampah',exact:true}).click();
  await expect(page.locator('.mail-row')).toHaveCount(0);
  await page.locator('[data-mail-folder="trash"]').click();
  await page.locator('[data-mail-select="m1"]').check();
  await page.getByRole('button',{name:'Pulihkan',exact:true}).click();
  await page.locator('[data-mail-folder="inbox"]').click();
  await expect(page.locator('[data-mail-star="m1"]')).toHaveAttribute('aria-pressed','false');
  await page.locator('.mail-open[href="email-read.html?id=m1"]').click();
  await expect(page.locator('#mailReadContent')).toContainText('Creative brief');
  const download=page.waitForEvent('download');
  await page.getByRole('link',{name:/Creative brief · TXT/}).click();
  expect((await download).suggestedFilename()).toBe('creative-brief.txt');
});

test('draft edit and send update one message including CC/BCC and safely rendered body',async({page})=>{
  await page.goto('/email-compose.html');
  await page.getByLabel('Kepada',{exact:true}).fill('team@example.com');
  await page.getByLabel('CC (opsional)',{exact:true}).fill('cc@example.com');
  await page.getByLabel('BCC (opsional)',{exact:true}).fill('bcc@example.com');
  await page.getByLabel('Subjek',{exact:true}).fill('Draft uji phase 1');
  await page.getByLabel('Isi pesan',{exact:true}).fill('<script>alert(1)</script> Halo tim.');
  await page.getByRole('button',{name:'Simpan draft',exact:true}).click();
  await expect(page.locator('#composeStatus')).toContainText('Draft disimpan');
  await page.reload();
  await expect(page.getByLabel('Subjek',{exact:true})).toHaveValue('Draft uji phase 1');
  await page.getByRole('button',{name:'Kirim demo'}).click();
  await expect(page).toHaveURL(/folder=sent/);
  await expect(page.locator('#mailNotice')).toContainText('Tidak ada email');
  await page.getByRole('link',{name:/Draft uji phase 1/}).click();
  await expect(page.locator('.mail-body')).toHaveText('<script>alert(1)</script> Halo tim.');
  await expect(page.locator('.mail-body script')).toHaveCount(0);
  await expect(page.locator('.mail-reader-meta')).toContainText('CC: cc@example.com');
  await expect(page.locator('.mail-reader-meta')).toContainText('BCC: bcc@example.com');
  const stored=await page.evaluate(()=>JSON.parse(localStorage.getItem('brutal.mail')).messages.filter(m=>m.subject==='Draft uji phase 1'));
  expect(stored).toHaveLength(1);expect(stored[0].folder).toBe('sent');
});

test('reply and forward prefill forms, discard is confirmed and unknown message IDs show an empty state',async({page})=>{
  await page.goto('/email-read.html?id=m1');
  await page.getByRole('link',{name:'Balas',exact:true}).click();
  await expect(page.getByLabel('Kepada',{exact:true})).toHaveValue('nina@example.com');
  await expect(page.getByLabel('Subjek',{exact:true})).toHaveValue(/^Re:/);
  await page.goto('/email-read.html?id=m1');
  await page.getByRole('link',{name:'Forward',exact:true}).click();
  await expect(page.getByLabel('Kepada',{exact:true})).toBeEmpty();
  await expect(page.getByLabel('Isi pesan',{exact:true})).toHaveValue(/Pesan diteruskan/);
  await page.goto('/email-compose.html?draft=m6');
  await page.getByRole('button',{name:'Buang',exact:true}).click();
  await page.getByRole('button',{name:'Batal',exact:true}).click();
  await expect(page.getByLabel('Subjek',{exact:true})).toHaveValue('Ide untuk kampanye berikutnya');
  await page.getByRole('button',{name:'Buang',exact:true}).click();
  await page.getByRole('button',{name:'Ya, buang pesan',exact:true}).click();
  await expect(page).toHaveURL(/notice=discarded/);
  await page.locator('[data-mail-folder="trash"]').click();
  await expect(page.locator('#mailRows')).toContainText('Ide untuk kampanye berikutnya');
  await page.goto('/email-read.html?id=missing');
  await expect(page.locator('#mailReadContent')).toContainText('Pesan tidak ditemukan');
});

test('workspace survives unavailable storage',async({page})=>{
  await page.addInitScript(()=>{const set=Storage.prototype.setItem;Storage.prototype.setItem=function(k,v){if(k.startsWith('brutal.'))throw new DOMException('Denied','QuotaExceededError');return set.call(this,k,v);};});
  await page.goto('/chat.html');
  await page.locator('#chatInput').fill('Pesan dalam memori');
  await page.locator('#chatForm button[type="submit"]').click();
  await expect(page.locator('#chatMessages')).toContainText('Pesan dalam memori');
  await expect(page.locator('#toastMessage')).toContainText('Penyimpanan browser tidak tersedia');
});

test('profile reset clears chat and mail demo data without removing unrelated storage',async({page})=>{
  await page.goto('/chat.html');
  await page.locator('#chatInput').fill('Data sementara');
  await page.locator('#chatForm button[type="submit"]').click();
  await page.goto('/email-read.html?id=m1');
  await page.evaluate(()=>localStorage.setItem('unrelated.workspace','keep'));
  await page.goto('/profile.html');
  await page.getByRole('button',{name:'Reset data demo',exact:true}).click();
  await page.getByRole('button',{name:'Ya, reset demo',exact:true}).click();
  await expect(page.locator('#resetModal')).not.toBeVisible();
  expect(await page.evaluate(()=>[localStorage.getItem('brutal.chat'),localStorage.getItem('brutal.mail'),localStorage.getItem('unrelated.workspace')])).toEqual([null,null,'keep']);
});
