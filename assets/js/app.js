/* BRUTAL. demo interactions. No framework, no network requests. */
(() => {
  'use strict';
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];
  const esc = value => String(value ?? '').replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]));
  const arrowIcon = name => `<svg class="icon" aria-hidden="true" viewBox="0 0 24 24">${window.BRUTAL_ICONS[name]}</svg>`;
  const prefix = 'brutal.';
  const memory = new Map();
  let storageWarningShown = false;
  const read = (key, fallback) => {
    if (memory.has(key)) return memory.get(key);
    try { const raw = localStorage.getItem(prefix + key); return raw ? JSON.parse(raw) : fallback; }
    catch { return fallback; }
  };
  const write = (key, value) => {
    memory.set(key, value);
    try { localStorage.setItem(prefix + key, JSON.stringify(value)); }
    catch {
      if (!storageWarningShown) {
        storageWarningShown = true;
        window.setTimeout(() => toast('Penyimpanan browser tidak tersedia. Perubahan hanya berlaku selama halaman ini terbuka.'), 300);
      }
    }
  };
  function toast(message) {
    $('#toastMessage').textContent = message;
    bootstrap.Toast.getOrCreateInstance($('#appToast'), {delay:4500}).show();
  }
  const uid = () => window.crypto?.randomUUID?.() || `${Date.now()}-${Math.random().toString(36).slice(2)}`;
  function downloadCSV(filename, rows) {
    // Prefix spreadsheet formulas, including formula-like user input.
    const cell = value => {
      let text = String(value ?? '');
      if (/^[\s]*[=+@-]/.test(text) || /^[\t\r\n]/.test(text)) text = "'" + text;
      return '"' + text.replace(/"/g, '""') + '"';
    };
    const blob = new Blob(['\uFEFF' + rows.map(row => row.map(cell).join(',')).join('\r\n')], {type:'text/csv;charset=utf-8'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = filename; a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }
  const statuses = ['Rencana','Berjalan','Review','Selesai'];
  const colors = {Rencana:'blue',Berjalan:'purple',Review:'yellow',Selesai:'green'};
  const seedProjects = [
    {id:'p1',name:'Studio website',category:'Website',status:'Berjalan',due:'2026-09-30',team:['AD','NS'],color:'purple'},
    {id:'p2',name:'Acme brand identity',category:'Branding',status:'Review',due:'2026-10-02',team:['RK','NS'],color:'orange'},
    {id:'p3',name:'Finance mobile app',category:'Mobile app',status:'Berjalan',due:'2026-10-08',team:['AD','RK'],color:'blue'},
    {id:'p4',name:'Summer campaign',category:'Marketing',status:'Selesai',due:'2026-09-24',team:['NS','RK'],color:'yellow'},
    {id:'p5',name:'Coffee shop landing',category:'Website',status:'Rencana',due:'2026-10-12',team:['AD'],color:'green'},
    {id:'p6',name:'Creative portfolio',category:'Website',status:'Rencana',due:'2026-10-15',team:['RK'],color:'orange'},
    {id:'p7',name:'Studio social kit',category:'Marketing',status:'Selesai',due:'2026-09-20',team:['NS'],color:'purple'},
    {id:'p8',name:'Motion brand system',category:'Branding',status:'Review',due:'2026-10-04',team:['AD','NS'],color:'green'},
  ];
  const safeArray = (value, fallback, validator) => Array.isArray(value) && value.every(validator) ? value : fallback;
  let projects = safeArray(read('projects',seedProjects), seedProjects, p => p && typeof p.id === 'string' && typeof p.name === 'string' && typeof p.category === 'string' && statuses.includes(p.status) && /^\d{4}-\d{2}-\d{2}$/.test(p.due) && Array.isArray(p.team) && p.team.every(x => typeof x === 'string'));
  let tablePage = 1;
  const dateLabel = value => {
    const date = new Date(value+'T12:00:00');
    return Number.isNaN(date.getTime()) ? '—' : date.toLocaleDateString('id-ID',{day:'numeric',month:'short'});
  };
  const team = members => `<div class="avatar-stack">${members.map((m,i) => `<span class="avatar avatar-sm bg-${i ? 'green':'orange'}" title="${esc(m)}">${esc(m)}</span>`).join('')}</div>`;
  function filteredProjects() {
    const query = ($('#tableSearch')?.value || '').toLowerCase();
    const status = $('#tableStatus')?.value || '';
    const sort = $('#tableSort')?.value || 'newest';
    const filtered = projects.filter(p => (!status || p.status === status) && `${p.name} ${p.category}`.toLowerCase().includes(query));
    if (sort === 'name') filtered.sort((a,b) => a.name.localeCompare(b.name,'id'));
    if (sort === 'due') filtered.sort((a,b) => a.due.localeCompare(b.due));
    return filtered;
  }
  function renderTable() {
    const tbody = $('#projectRows'); if (!tbody) return;
    const items = filteredProjects(); const limit = Number(tbody.dataset.limit);
    const totalPages = Math.max(1, Math.ceil(items.length/limit)); tablePage = Math.min(tablePage,totalPages);
    const shown = items.slice((tablePage-1)*limit,tablePage*limit);
    tbody.innerHTML = shown.length ? shown.map(p => `<tr><td><div class="table-project"><span class="project-icon bg-${esc(['purple','orange','blue','green','yellow'].includes(p.color) ? p.color : 'purple')}">${esc(p.name.slice(0,1).toUpperCase())}</span><div><div class="table-title">${esc(p.name)}</div><div class="table-sub">${esc(p.category)}</div></div></div></td><td>${team(p.team)}</td><td><span class="badge bg-${colors[p.status]}">${p.status}</span></td><td class="text-nowrap">${dateLabel(p.due)}</td></tr>`).join('') : '<tr><td colspan="4" class="text-center py-5 text-muted">Tidak ada proyek yang cocok. Coba kata kunci atau filter lain.</td></tr>';
    if ($('#tableCount')) $('#tableCount').textContent = items.length ? `${(tablePage-1)*limit+1}–${Math.min(tablePage*limit,items.length)} dari ${items.length} proyek` : '0 proyek';
    if ($('#tablePagination')) $('#tablePagination').innerHTML = `<li class="page-item ${tablePage === 1 ? 'disabled' : ''}"><button type="button" class="page-link" data-table-page="${tablePage-1}" aria-label="Halaman sebelumnya" ${tablePage === 1 ? 'disabled' : ''}>${arrowIcon('arrow-left')}</button></li>` + Array.from({length:totalPages},(_,i) => `<li class="page-item ${tablePage === i+1 ? 'active':''}"><button class="page-link" data-table-page="${i+1}" ${tablePage === i+1 ? 'aria-current="page"':''} aria-label="Halaman ${i+1}">${i+1}</button></li>`).join('') + `<li class="page-item ${tablePage === totalPages ? 'disabled' : ''}"><button type="button" class="page-link" data-table-page="${tablePage+1}" aria-label="Halaman berikutnya" ${tablePage === totalPages ? 'disabled' : ''}>${arrowIcon('arrow')}</button></li>`;
  }
  ['tableSearch','tableStatus','tableSort'].forEach(id => $('#'+id)?.addEventListener(id==='tableSearch' ? 'input':'change', () => {tablePage=1;renderTable();}));
  $('#tablePagination')?.addEventListener('click', e => {const btn=e.target.closest('[data-table-page]');if(btn && !btn.disabled){tablePage=Number(btn.dataset.tablePage);renderTable();$('#tablePagination [aria-current="page"]')?.focus();}});
  $('#exportTable')?.addEventListener('click', () => {downloadCSV('brutal-proyek.csv',[['Nama proyek','Kategori','Status','Tenggat'],...filteredProjects().map(p=>[p.name,p.category,p.status,p.due])]);toast('Data sesuai filter telah diekspor.');});
  $('#exportDashboard')?.addEventListener('click', () => {downloadCSV('brutal-ringkasan-demo.csv',[['Metrik demo','Nilai'],['Pendapatan bulanan',48500000],['Proyek aktif',24],['Pelanggan',1284],['Konversi','4.82%']]);toast('Ringkasan dashboard demo diekspor.');});
  function kanbanProjects(status) {
    return projects.filter(project => project.status === status)
      .map((project, index) => ({ project, order: Number.isFinite(project.boardOrder) ? project.boardOrder : index }))
      .sort((left, right) => left.order - right.order)
      .map(item => item.project);
  }
  function renderKanban() {
    const board = $('#kanbanBoard');
    if (!board) return;
    // Close while the original ancestors still exist, so Select2 can detach its scroll listeners.
    board.querySelectorAll('select').forEach(field => {
      if (window.jQuery?.(field).data('select2')) window.jQuery(field).select2('close');
    });
    board.innerHTML = statuses.map((status, index) => {
      const items = kanbanProjects(status);
      const cards = items.map(project => `
        <article class="card kanban-card" data-project-id="${esc(project.id)}" tabindex="0" role="group" aria-label="Proyek ${esc(project.name)}" aria-describedby="kanbanKeyboardHelp">
          <div class="card-body">
            <div class="kanban-card-top">
              <span class="badge bg-${colors[status]}">${status}</span>

            </div>
            <h3>${esc(project.name)}</h3>
            <p>${esc(project.category)} · ${dateLabel(project.due)}</p>
            <div class="kanban-assignees">${team(project.team)}<span class="small text-muted">Tim proyek</span></div>
            <div class="kanban-status-control">
              <label class="visually-hidden" for="status-${esc(project.id)}">Status ${esc(project.name)}</label>
              <select class="form-select form-select-sm" id="status-${esc(project.id)}" data-project-status="${esc(project.id)}">
                ${statuses.map(value => `<option ${value === status ? 'selected' : ''}>${value}</option>`).join('')}
              </select>
            </div>
          </div>
        </article>`).join('');
      return `<section class="kanban-column" data-kanban-status="${status}" aria-labelledby="kanban-title-${index}">
        <div class="kanban-heading"><h2 class="mb-0 fs-6" id="kanban-title-${index}"><span class="kanban-status-dot bg-${colors[status]}"></span>${status}</h2><span class="badge bg-${colors[status]}" aria-label="${items.length} proyek">${items.length}</span></div>
        <div class="kanban-card-list">${cards || '<p class="kanban-empty">Belum ada proyek.<br>Letakkan kartu di sini.</p>'}</div>
      </section>`;
    }).join('');
  }
  function moveProject(id, status, fromDrag = false, beforeId = null) {
    const project = projects.find(item => item.id === id);
    if (!project || !statuses.includes(status) || (!fromDrag && project.status === status)) return;
    const previousStatus = project.status;
    const original = kanbanProjects(status);
    const destination = original.filter(item => item.id !== id);
    const beforeIndex = destination.findIndex(item => item.id === beforeId);
    destination.splice(beforeIndex < 0 ? destination.length : beforeIndex, 0, project);
    if (previousStatus === status && original.every((item, index) => item.id === destination[index].id)) {
      $('#kanbanFeedback').textContent = `${project.name} tetap pada posisi semula.`;
      return;
    }
    kanbanProjects(previousStatus).filter(item => item.id !== id)
      .forEach((item, index) => { item.boardOrder = index; });
    project.status = status;
    destination.forEach((item, index) => { item.boardOrder = index; });
    write('projects', projects);
    const canvas = $('#kanbanCanvas');
    const scroll = { top: canvas.scrollTop, left: canvas.scrollLeft };
    renderKanban();
    canvas.scrollTo(scroll);
    const position = destination.indexOf(project) + 1;
    const message = `${project.name} ditempatkan di ${status}, urutan ${position}.`;
    $('#kanbanFeedback').textContent = message;
    toast(message);
    const moved = $$('[data-project-id]').find(card => card.dataset.projectId === id);
    (fromDrag ? moved : moved?.querySelector('select'))?.focus({ preventScroll: true });
  }
  $('#kanbanBoard')?.addEventListener('change', event => {
    const select = event.target.closest('[data-project-status]');
    if (select) moveProject(select.dataset.projectStatus, select.value);
  });
  $('#kanbanBoard')?.addEventListener('kanban:move', event => {
    moveProject(event.detail.id, event.detail.status, true, event.detail.beforeId);
  });
  $('#projectForm')?.addEventListener('submit', e => {
    e.preventDefault(); const data=new FormData(e.target); const name=data.get('name').trim();
    if(!name){$('#projectName').setCustomValidity('Isi nama proyek.');$('#projectName').reportValidity();return;}
    projects.unshift({id:uid(),name,category:data.get('category'),due:data.get('due'),status:'Rencana',team:['AD'],color:'purple'});
    write('projects',projects);tablePage=1;renderTable();renderKanban();e.target.reset();bootstrap.Modal.getInstance($('#projectModal')).hide();toast(`Proyek “${name}” ditambahkan. Lihat di halaman Proyek atau Tabel data.`);
  });
  $('#projectName')?.addEventListener('input',e=>e.target.setCustomValidity(''));
  renderTable();renderKanban();

  // Daily focus: label/input controls work with keyboard and pointer.
  let tasks=safeArray(read('tasks',[{id:'t1',name:'Review desain landing page',done:false},{id:'t2',name:'Kirim proposal ke Acme',done:false},{id:'t3',name:'Update komponen UI kit',done:true},{id:'t4',name:'Siapkan ide untuk besok',done:false}]),[],t=>t&&typeof t.id==='string'&&typeof t.name==='string'&&typeof t.done==='boolean');
  function renderTasks(){
    if(!$('#taskList'))return;
    $('#taskList').innerHTML=tasks.map(t=>`<label class="task" for="task-${esc(t.id)}"><input id="task-${esc(t.id)}" class="form-check-input" type="checkbox" data-task-id="${esc(t.id)}" ${t.done?'checked':''}><span><span class="task-title">${esc(t.name)}</span><small>${t.done?'Sudah beres. Nice!':'Personal workspace'}</small></span></label>`).join('');
    $('#taskCount').textContent=`${tasks.filter(t=>t.done).length}/${tasks.length}`;
  }
  $('#taskList')?.addEventListener('change', e=>{const t=tasks.find(t=>t.id===e.target.dataset.taskId);if(!t)return;t.done=e.target.checked;write('tasks',tasks);renderTasks();$$('[data-task-id]').find(el=>el.dataset.taskId===t.id)?.focus();});
  $('#taskForm')?.addEventListener('submit',e=>{e.preventDefault();const name=$('#taskInput').value.trim();if(!name)return;tasks.push({id:uid(),name,done:false});write('tasks',tasks);renderTasks();e.target.reset();$('#taskInput').focus();toast('Satu fokus baru ditambahkan.');});renderTasks();

  // Page search uses the same source as the shared sidebar.
  document.addEventListener('keydown',e=>{
    if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();window.BrutalSidebar?.close();bootstrap.Modal.getOrCreateInstance($('#searchModal')).show();}
  });
  const pageLinks=window.BrutalNavigation || [];
  function renderSearch(){const q=$('#globalSearch').value.toLowerCase();const found=pageLinks.filter(p=>p.join(' ').toLowerCase().includes(q));$('#searchResults').innerHTML=found.length?found.map(([title,path,group])=>`<a href="${esc(path)}.html">${esc(title)}<small>${esc(group)} ↗</small></a>`).join(''):'<p class="text-muted p-3">Tidak ada halaman yang cocok.</p>';}
  $('#searchModal')?.addEventListener('shown.bs.modal',()=>{$('#globalSearch').focus();renderSearch();});$('#globalSearch')?.addEventListener('input',renderSearch);
  $$('[data-bs-toggle="tooltip"]').forEach(el=>new bootstrap.Tooltip(el));$$('[data-bs-toggle="popover"]').forEach(el=>new bootstrap.Popover(el));
  document.addEventListener('click',e=>{const el=e.target.closest('[data-toast]');if(el)toast(el.dataset.toast);});

  // Standalone component examples.
  $$('[data-indeterminate]').forEach(el=>{el.indeterminate=true;});
  $$('[data-pagination-demo]').forEach(demo=>{
    let current=1;
    demo.addEventListener('click',e=>{
      const btn=e.target.closest('[data-demo-page], [data-page-step]');
      if(!btn||btn.disabled)return;
      current=Math.max(1,Math.min(3,btn.dataset.demoPage?Number(btn.dataset.demoPage):current+Number(btn.dataset.pageStep)));
      $$('[data-demo-page]',demo).forEach(el=>{
        const active=Number(el.dataset.demoPage)===current;
        el.parentElement.classList.toggle('active',active);
        if(active)el.setAttribute('aria-current','page');else el.removeAttribute('aria-current');
      });
      $$('[data-page-step]',demo).forEach(el=>{
        el.disabled=Number(el.dataset.pageStep)<0?current===1:current===3;
        el.parentElement.classList.toggle('disabled',el.disabled);
      });
      $('[data-page-result]',demo).textContent=`Halaman ${current} · Menampilkan item ${(current-1)*5+1}–${current*5} dari 15.`;
    });
  });
  $('.navbar-demo-search')?.addEventListener('submit',e=>{
    e.preventDefault();const query=$('input',e.target).value.trim();
    $('#navbarSearchResult').textContent=query?`Pencarian demo: “${query}”. Hubungkan form ini ke pencarian aplikasimu.`:'Ketik kata kunci untuk mencoba pencarian.';
  });
  $('#progressAnimation')?.addEventListener('click',e=>{
    const paused=e.currentTarget.getAttribute('aria-pressed')!=='true';
    e.currentTarget.setAttribute('aria-pressed',String(paused));
    e.currentTarget.textContent=paused?'Lanjutkan animasi':'Jeda animasi';
    $$('.progress-bar-animated').forEach(el=>{el.style.animationPlayState=paused?'paused':'running';});
  });
  $('#flagSearch')?.addEventListener('input',e=>{
    const query=e.target.value.trim().toLocaleLowerCase('id');let count=0;
    $$('[data-flag-name]').forEach(el=>{el.hidden=!el.dataset.flagName.includes(query);if(!el.hidden)count++;});
    $('#flagCount').textContent=count?`${count} bendera`:'Tidak ada bendera yang cocok. Coba nama atau kode negara lain.';
  });

  // Native form validation, files are never uploaded.
  $('#demoForm')?.addEventListener('submit',e=>{e.preventDefault();const valid=e.target.checkValidity();e.target.classList.add('was-validated');if(valid){$('#formResult').textContent='Data demo valid. Tidak ada data dikirim ke server.';toast('Form berhasil divalidasi.');}else{$('#formResult').textContent='Periksa kembali kolom yang ditandai.';e.target.querySelector(':invalid')?.focus();}});
  $('#demoForm')?.addEventListener('reset',e=>{e.target.classList.remove('was-validated');$('#formResult').textContent='';});
  $('#budget')?.addEventListener('input',e=>$('#budgetOutput').value=e.target.value);
  $('#fileUpload')?.addEventListener('change',e=>{$('#fileNames').textContent=[...e.target.files].map(f=>f.name).join(', ')||'File tidak diunggah ke server.';});
  $('#togglePassword')?.addEventListener('click',e=>{const input=$('#authPassword');const shown=input.type==='password';input.type=shown?'text':'password';e.currentTarget.setAttribute('aria-label',shown?'Sembunyikan password':'Tampilkan password');e.currentTarget.setAttribute('aria-pressed',String(shown));});
  $('#authConfirmPassword')?.addEventListener('input',e=>e.currentTarget.setCustomValidity(''));
  $('#authForm')?.addEventListener('submit',e=>{
    e.preventDefault();const page=document.body.dataset.page;
    if(page==='auth-forgot-password'){$('#authResult').textContent='Simulasi selesai. Pada aplikasi nyata, backend mengirim tautan reset ke email. Tidak ada email dikirim dalam demo ini.';}
    else if(page==='auth-reset-password'){
      const password=$('#authPassword'), confirm=$('#authConfirmPassword');
      if(password.value!==confirm.value){$('#authResult').textContent='Konfirmasi password belum sama. Coba lagi.';confirm.setCustomValidity('Password tidak sama');confirm.reportValidity();return;}
      confirm.setCustomValidity('');
      password.value='';confirm.value='';
      $('#authResult').textContent='Password baru valid untuk demo. Tidak ada akun nyata yang diubah atau password disimpan.';
    }
    else {if($('#authPassword'))$('#authPassword').value='';window.location.href='index.html';}
  });

  // Profile and display preferences.
  const profile=read('profile',{});
  if(profile && typeof profile === 'object') {
    if(typeof profile.name==='string'){$('#profileName')&&($('#profileName').value=profile.name);$('#profileDisplayName')&&($('#profileDisplayName').textContent=profile.name);$('.sidebar-foot strong')&&($('.sidebar-foot strong').textContent=profile.name);}
    if(typeof profile.email==='string'&&$('#profileEmail'))$('#profileEmail').value=profile.email;
    if(typeof profile.role==='string'){$('#profileRole')&&($('#profileRole').value=profile.role);$('#profileDisplayRole')&&($('#profileDisplayRole').textContent=profile.role);}
  }
  $('#profileForm')?.addEventListener('submit',e=>{e.preventDefault();const data=Object.fromEntries(new FormData(e.target));data.name=data.name.trim();if(!data.name){$('#profileName').setCustomValidity('Nama tidak boleh kosong.');$('#profileName').reportValidity();return;}write('profile',data);$('#profileDisplayName').textContent=data.name;$('#profileDisplayRole').textContent=data.role;$('.sidebar-foot strong').textContent=data.name;toast('Profil demo disimpan di browser.');});
  $('#profileName')?.addEventListener('input',e=>e.target.setCustomValidity(''));
  const compact=read('compact',false)===true;document.body.classList.toggle('compact',compact);if($('#compactMode'))$('#compactMode').checked=compact;
  $('#compactMode')?.addEventListener('change',e=>{document.body.classList.toggle('compact',e.target.checked);write('compact',e.target.checked);});
  $('#resetData')?.addEventListener('click',()=>{memory.clear();try{['projects','tasks','events','profile','compact','chat','mail'].forEach(key=>localStorage.removeItem(prefix+key));window.location.reload();}catch{toast('Penyimpanan browser tidak dapat diakses.');}});
  $('#printInvoice')?.addEventListener('click',()=>window.print());

  // Accessible, local SVG chart; changing period updates every series and label.
  $('#chartPeriod')?.addEventListener('change',e=>{
    const previous=e.target.value==='previous';const data=previous?[6,8,7,12,14,16]:[8,11,9,16,14,20];const target=previous?[5,6,7,9,10,11]:[5,8,7,11,9,14];
    const path=values=>values.map((n,i)=>`${i?'L':'M'}${40+i*104} ${222-n*9.6}`).join(' ');
    $('#chartLine').setAttribute('d',path(data));$('#chartTarget').setAttribute('d',path(target));$('#chartArea').setAttribute('d',path(data)+'V205H40Z');
    $('#chartDots').innerHTML=data.map((n,i)=>`<circle cx="${40+i*104}" cy="${222-n*9.6}" r="4" fill="#c4a8f5" stroke="#232420" stroke-width="2"/>`).join('');
    const months=previous?['Okt','Nov','Des','Jan','Feb','Mar']:['Apr','Mei','Jun','Jul','Agu','Sep'];
    $$('.revenue-chart text.chart-label').slice(-6).forEach((el,i)=>el.textContent=months[i]);
    $('#chartTotal').textContent=previous?'Rp63.000.000':'Rp78.000.000';$('#chartGrowth').textContent=previous?'↗ 15,2%':'↗ 23,8%';
    $('#revenueChartTitle').textContent=`Pendapatan contoh ${months[0]}–${months[5]}: ${data.join(', ')} juta rupiah. Target: ${target.join(', ')} juta.`;
  });

  // Calendar uses local dates to avoid UTC/day boundary shifts.
  const now=new Date();let calendarDate=new Date(now.getFullYear(),now.getMonth(),1);
  const isoLocal=date=>`${date.getFullYear()}-${String(date.getMonth()+1).padStart(2,'0')}-${String(date.getDate()).padStart(2,'0')}`;
  const defaultEvents=[{id:'e1',name:'Weekly creative sync',date:isoLocal(new Date(now.getFullYear(),now.getMonth(),8)),time:'09:00'},{id:'e2',name:'Review brand identity',date:isoLocal(new Date(now.getFullYear(),now.getMonth(),16)),time:'14:00'},{id:'e3',name:'Launch day! ✳',date:isoLocal(new Date(now.getFullYear(),now.getMonth(),24)),time:'10:00'}];
  let events=safeArray(read('events',defaultEvents),defaultEvents,e=>e&&typeof e.id==='string'&&typeof e.name==='string'&&/^\d{4}-\d{2}-\d{2}$/.test(e.date)&&typeof e.time==='string');
  function renderCalendar(){
    if(!$('#calendarGrid'))return;
    $('#calendarTitle').textContent=calendarDate.toLocaleDateString('id-ID',{month:'long',year:'numeric'});
    const year=calendarDate.getFullYear(),month=calendarDate.getMonth(),offset=(calendarDate.getDay()+6)%7,days=new Date(year,month+1,0).getDate();
    let html=['SEN','SEL','RAB','KAM','JUM','SAB','MIN'].map(d=>`<div class="calendar-day-label">${d}</div>`).join('');
    const total=Math.ceil((offset+days)/7)*7;
    for(let i=0;i<total;i++){
      const day=i-offset+1;if(day<1||day>days){html+='<div class="calendar-cell empty" aria-hidden="true"></div>';continue;}
      const date=isoLocal(new Date(year,month,day));const today=date===isoLocal(now);
      html+=`<div class="calendar-cell ${today?'today':''}"><span class="calendar-date" ${today?'aria-current="date"':''}>${day}</span>${events.filter(e=>e.date===date).sort((a,b)=>a.time.localeCompare(b.time)).map(e=>`<button class="calendar-event bg-purple" data-event-id="${esc(e.id)}" title="${esc(e.time+' · '+e.name)}">${esc(e.name)}</button>`).join('')}</div>`;
    }
    $('#calendarGrid').innerHTML=html;
  }
  $('#prevMonth')?.addEventListener('click',()=>{calendarDate.setMonth(calendarDate.getMonth()-1);renderCalendar();});
  $('#nextMonth')?.addEventListener('click',()=>{calendarDate.setMonth(calendarDate.getMonth()+1);renderCalendar();});
  $('#todayMonth')?.addEventListener('click',()=>{calendarDate=new Date(now.getFullYear(),now.getMonth(),1);renderCalendar();});
  $('#calendarGrid')?.addEventListener('click',e=>{const btn=e.target.closest('[data-event-id]');if(btn){const event=events.find(e=>e.id===btn.dataset.eventId);if(event)toast(`${dateLabel(event.date)} · ${event.time} — ${event.name}`);}});
  if($('#eventDate'))$('#eventDate').value=isoLocal(now);
  $('#eventForm')?.addEventListener('submit',e=>{e.preventDefault();const data=Object.fromEntries(new FormData(e.target));data.name=data.name.trim();if(!data.name){$('#eventName').setCustomValidity('Isi nama agenda.');$('#eventName').reportValidity();return;}events.push({id:uid(),...data});write('events',events);const [year,month]=data.date.split('-').map(Number);calendarDate=new Date(year,month-1,1);renderCalendar();bootstrap.Modal.getInstance($('#eventModal')).hide();e.target.reset();$('#eventDate').value=isoLocal(now);toast('Agenda baru ditambahkan.');});
  $('#eventName')?.addEventListener('input',e=>e.target.setCustomValidity(''));renderCalendar();
})();
