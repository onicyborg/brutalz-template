const {test,expect}=require('@playwright/test');
const fs=require('node:fs');
const path=require('node:path');
const root=path.resolve(__dirname,'..');
const files=fs.readdirSync(root).filter(name=>name.endsWith('.html'));

test('every page shares one navigation, highlights its own route, and links only to existing pages',async({page})=>{
  let baseline;
  const errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  for(const file of files){
    const source=fs.readFileSync(path.join(root,file),'utf8');
    expect(source).toContain('<div id="sidebar-root"></div>');
    expect(source).not.toContain('<aside class="sidebar"');
    await page.goto('/'+file);
    const nav=page.locator('#sidebar .sidebar-nav');
    const links=await nav.locator('a').evaluateAll(els=>els.map(el=>el.getAttribute('href')));
    if(!baseline)baseline=links;
    expect(links).toEqual(baseline);
    for(const link of links)expect(fs.existsSync(path.join(root,link)),link).toBeTruthy();
    await expect(nav.locator('a[aria-current="page"]')).toHaveCount(1);
    await expect(nav.locator('a[aria-current="page"]')).toHaveAttribute('href',file);
    expect(await nav.locator('a.active').evaluate(el=>{
      for(let parent=el.parentElement;parent;parent=parent.parentElement){
        if(parent.classList.contains('collapse')&&!parent.classList.contains('show'))return false;
      }
      return true;
    })).toBeTruthy();
    expect(await page.locator('#sidebar').count()).toBe(1);
  }
  expect(errors).toEqual([]);
});

test('drawer traps focus, closes with Escape/backdrop, restores focus, and survives resize',async({page})=>{
  await page.setViewportSize({width:390,height:844});
  await page.goto('/alert.html');
  const toggle=page.locator('#sidebarToggle');
  await toggle.click();
  await expect(page.locator('#sidebar a[aria-current="page"]')).toBeFocused();
  await expect(page.locator('.app-wrap')).toHaveAttribute('inert','');
  await page.locator('#sidebar .sidebar-foot a').focus();
  await page.keyboard.press('Tab');
  await expect(page.locator('#sidebar .brand')).toBeFocused();
  await page.keyboard.press('Shift+Tab');
  await expect(page.locator('#sidebar .sidebar-foot a')).toBeFocused();
  await page.keyboard.press('Escape');
  await expect(toggle).toBeFocused();
  await expect(toggle).toHaveAttribute('aria-expanded','false');
  await toggle.click();
  await page.mouse.click(370,400);
  await expect(toggle).toHaveAttribute('aria-expanded','false');
  await toggle.click();
  await page.setViewportSize({width:1440,height:900});
  await expect(page.locator('.app-wrap')).not.toHaveAttribute('inert','');
  await expect(page.locator('body')).not.toHaveClass(/sidebar-open/);
  await page.getByRole('button',{name:'Komponen UI',exact:true}).click();
  await expect(page.locator('#uiComponentsMenu')).not.toBeVisible();
  await page.getByRole('button',{name:'Komponen UI',exact:true}).click();
  await expect(page.locator('#uiComponentsMenu')).toBeVisible();
});

test('standalone auth and error pages expose the same drawer and searchable routes',async({page})=>{
  for(const route of ['auth-login','errors-404']){
    await page.goto('/'+route+'.html');
    await page.locator('#sidebarToggle').click();
    await expect(page.locator('#sidebar')).toHaveAttribute('aria-modal','true');
    await expect(page.locator('#sidebar [aria-current="page"]')).toBeFocused();
    await page.keyboard.press('Control+k');
    await expect(page.locator('#sidebar')).toHaveAttribute('inert','');
    await page.locator('#globalSearch').fill('404');
    await expect(page.locator('#searchResults a')).toHaveAttribute('href','errors-404.html');
  }
});

test('navigation config updates rendering and search without regenerating HTML',async({page})=>{
  await page.route('**/sidebar-config.js',async route=>{
    const response=await route.fetch();
    await route.fulfill({response,body:(await response.text()).replace('"label":"Dashboard"','"label":"Beranda uji"')});
  });
  await page.goto('/index.html');
  await expect(page.locator('#sidebar a[aria-current="page"]')).toHaveText('Beranda uji');
  await page.keyboard.press('Control+k');
  await page.locator('#globalSearch').fill('Beranda uji');
  await expect(page.locator('#searchResults a')).toHaveAttribute('href','index.html');
});

test('shared navigation also works when HTML is opened directly from disk',async({page})=>{
  await page.goto(require('node:url').pathToFileURL(path.join(root,'alert.html')).href);
  await expect(page.locator('#sidebar a[aria-current="page"]')).toHaveAttribute('href','alert.html');
  await page.getByRole('button',{name:'Komponen UI',exact:true}).click();
  await expect(page.locator('#uiComponentsMenu')).not.toBeVisible();
});
