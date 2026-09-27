/* Shared navigation renderer. Load config + icons + Bootstrap before this file. */
(() => {
  'use strict';
  const config = window.BRUTAL_SIDEBAR || [];
  const esc = value => String(value).replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  const icon = name => `<svg class="icon" aria-hidden="true" viewBox="0 0 24 24">${window.BRUTAL_ICONS?.[name] || ''}</svg>`;
  const current = document.body.dataset.page;
  const containsPage = item => item.page === current || (item.children || []).some(containsPage);
  const pages = [];
  function renderItems(items, group, nested = false) {
    return items.map(item => {
      if (item.children) {
        const active = containsPage(item);
        return `<li><button type="button" class="sidebar-link sidebar-group-toggle${active?' active':''}" data-bs-toggle="collapse" data-bs-target="#${esc(item.id)}" aria-controls="${esc(item.id)}" aria-expanded="${active}">${item.icon?icon(item.icon):''}<span>${esc(item.label)}</span><span class="submenu-chevron" aria-hidden="true">⌄</span></button><div class="collapse${active?' show':''}" id="${esc(item.id)}"><ul class="sidebar-submenu">${renderItems(item.children,item.label,true)}</ul></div></li>`;
      }
      pages.push([item.label,item.page,group]);
      return `<li><a href="${esc(item.page)}.html" class="${nested?'sidebar-sub-link':'sidebar-link'}${item.page===current?' active':''}"${item.page===current?' aria-current="page"':''}>${item.icon?icon(item.icon):''}<span>${esc(item.label)}</span></a></li>`;
    }).join('');
  }
  const nav = config.map(section=>`<div class="nav-caption">${esc(section.group)}</div><ul class="sidebar-menu">${renderItems(section.items,section.group)}</ul>`).join('');
  window.BrutalNavigation = pages;
  const root = document.getElementById('sidebar-root');
  if (!root || document.getElementById('sidebar')) return;
  root.innerHTML = `<button class="sidebar-backdrop" aria-label="Tutup navigasi" tabindex="-1"></button><aside class="sidebar" id="sidebar" aria-label="Navigasi utama"><div class="sidebar-brand"><a href="index.html" class="brand"><span class="brand-mark">b.</span>BRUTAL.<small>v1.0</small></a><button type="button" id="sidebarClose" class="btn icon-btn sidebar-close" aria-label="Tutup menu navigasi">${icon('close')}</button></div><nav class="sidebar-nav" aria-label="Halaman template">${nav}</nav><div class="sidebar-foot"><span class="avatar">AD</span><div><strong class="d-block small">Alex Darma</strong><span class="text-muted" style="font-size:10px">Personal workspace</span></div><a class="ms-auto text-dark" href="profile.html" aria-label="Pengaturan profil">${icon('settings')}</a></div></aside>`;
  const sidebar = document.getElementById('sidebar');
  const toggle = document.getElementById('sidebarToggle');
  const closeButton = document.getElementById('sidebarClose');
  const media = matchMedia('(max-width:991px)');
  const standalone = document.body.classList.contains('standalone-page');
  const drawerMode = () => standalone || media.matches;
  const background = document.querySelector('.app-wrap, .auth-layout, body > main');
  const isOpen = () => document.body.classList.contains('sidebar-open');
  function sync() {
    if (!drawerMode()) document.body.classList.remove('sidebar-open');
    const open = drawerMode() && isOpen();
    sidebar.inert = drawerMode() && !open;
    if (background) background.inert = open;
    toggle?.setAttribute('aria-expanded',String(open));
    toggle?.setAttribute('aria-label',open?'Tutup navigasi':'Buka navigasi');
    if(open){sidebar.setAttribute('role','dialog');sidebar.setAttribute('aria-modal','true');}
    else{sidebar.removeAttribute('role');sidebar.removeAttribute('aria-modal');}
  }
  function setOpen(open, restoreFocus = true) {
    document.body.classList.toggle('sidebar-open',open && drawerMode());
    sync();
    if(isOpen()) (sidebar.querySelector('[aria-current="page"]') || closeButton).focus();
    else if(restoreFocus) toggle?.focus();
  }
  toggle?.addEventListener('click',()=>setOpen(!isOpen()));
  closeButton.addEventListener('click',()=>setOpen(false));
  root.querySelector('.sidebar-backdrop').addEventListener('click',()=>setOpen(false));
  media.addEventListener('change',()=>{
    const focusedInSidebar=sidebar.contains(document.activeElement);
    sync();
    if(sidebar.inert && focusedInSidebar) toggle?.focus();
  });
  document.addEventListener('keydown',event=>{
    if(!isOpen()) return;
    if(event.key==='Escape'){event.preventDefault();setOpen(false);return;}
    if(event.key!=='Tab') return;
    const targets=[...sidebar.querySelectorAll('a,button')].filter(el=>el.getClientRects().length&&!el.disabled);
    const first=targets[0],last=targets.at(-1);
    if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}
    else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}
  });
  // Bootstrap's data API handles toggles; initialize once for explicit API callers.
  sidebar.querySelectorAll('.collapse').forEach(el=>bootstrap.Collapse.getOrCreateInstance(el,{toggle:false}));
  sync();
  if(!sidebar.inert) sidebar.querySelector('[aria-current="page"]')?.scrollIntoView({block:'nearest'});
  window.BrutalSidebar = { close: () => setOpen(false,false) };
})();
