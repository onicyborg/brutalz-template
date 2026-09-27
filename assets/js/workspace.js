/* Phase 1 demos. Loaded only by workspace pages; all data stays in this browser. */
(() => {
  'use strict';
  const $=(s,root=document)=>root.querySelector(s);
  const $$=(s,root=document)=>[...root.querySelectorAll(s)];
  const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const uid=()=>crypto.randomUUID?.() || `${Date.now()}-${Math.random().toString(36).slice(2)}`;
  const clone=v=>JSON.parse(JSON.stringify(v));
  const text=v=>typeof v==='string';
  function notify(message){$('#toastMessage').textContent=message;bootstrap.Toast.getOrCreateInstance($('#appToast')).show();}
  function read(key,fallback,valid){try{const raw=localStorage.getItem('brutal.'+key);if(raw){const value=JSON.parse(raw);if(valid(value))return value;}}catch{}return clone(fallback);}
  function save(key,value){try{localStorage.setItem('brutal.'+key,JSON.stringify(value));return true;}catch{notify('Penyimpanan browser tidak tersedia. Perubahan hanya berlaku di halaman ini.');return false;}}
  const dateTime=iso=>{const date=new Date(iso);return Number.isNaN(+date)?'Tanggal tidak tersedia':date.toLocaleString('id-ID',{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'});};
  const initials=name=>name.split(/\s+/).slice(0,2).map(n=>n[0]||'').join('').toUpperCase();
  const page=document.body.dataset.page;
  function showDetail(modalId,title,body,trigger){
    const modal=$('#'+modalId);$('.modal-title',modal).textContent=title;$('.modal-body',modal).innerHTML=body;
    modal.addEventListener('hidden.bs.modal',()=>trigger?.focus(),{once:true});bootstrap.Modal.getOrCreateInstance(modal).show(trigger);
  }

  if($('#miniCalendar')){
    const today=new Date(),year=today.getFullYear(),month=today.getMonth(),offset=(new Date(year,month,1).getDay()+6)%7,total=new Date(year,month+1,0).getDate();
    $('#miniCalendar').innerHTML=`<h3 class="mb-3">${today.toLocaleDateString('id-ID',{month:'long',year:'numeric'})}</h3><div class="mini-calendar">${['SEN','SEL','RAB','KAM','JUM','SAB','MIN'].map(d=>`<span class="day-name">${d}</span>`).join('')}${'<span aria-hidden="true"></span>'.repeat(offset)}${Array.from({length:total},(_,i)=>`<span${i+1===today.getDate()?' class="today" aria-current="date"':''}>${i+1}</span>`).join('')}</div>`;
  }

  if(page==='portfolio'){
    const projects=JSON.parse($('#portfolioData').textContent);
    $$('[data-portfolio-filter]').forEach(btn=>btn.addEventListener('click',()=>{
      let count=0;$$('[data-portfolio-category]').forEach(card=>{card.hidden=btn.dataset.portfolioFilter!=='Semua'&&card.dataset.portfolioCategory!==btn.dataset.portfolioFilter;if(!card.hidden)count++;});
      $$('[data-portfolio-filter]').forEach(b=>{const active=b===btn;b.setAttribute('aria-pressed',String(active));b.classList.toggle('btn-dark',active);b.classList.toggle('btn-outline-primary',!active);});
      $('#portfolioCount').textContent=`${count} karya`;
    }));
    $$('[data-project-detail]').forEach(link=>link.addEventListener('click',e=>{
      e.preventDefault();const p=projects.find(p=>p.id===link.dataset.projectDetail);if(!p)return;
      showDetail('portfolioModal',p.title,`<img src="assets/img/workspace/${esc(p.image)}.svg" class="case-image" alt="Konsep ${esc(p.client)}"><span class="badge bg-yellow mb-3">${esc(p.category)} · ${esc(p.year)}</span><p>${esc(p.description)}</p><h3>Lingkup pekerjaan</h3><p class="text-muted">${esc(p.deliverables)}</p><p class="small text-muted mb-0">Studi kasus ilustratif untuk showcase template.</p>`,link);
    }));
  }

  if(page==='blog'){
    const articles=JSON.parse($('#articleData').textContent);let category='Semua',current=1;const limit=3;
    function render(){
      const q=$('#blogSearch').value.trim().toLowerCase();const matches=articles.filter(a=>(category==='Semua'||a.category===category)&&`${a.title} ${a.excerpt} ${a.author}`.toLowerCase().includes(q));
      const total=Math.ceil(matches.length/limit);current=Math.min(current,Math.max(total,1));const visible=matches.slice((current-1)*limit,current*limit).map(a=>a.id);
      $$('[data-article-id]').forEach(card=>{card.hidden=!visible.includes(card.dataset.articleId);});
      $('#blogCount').textContent=matches.length?`${matches.length} artikel · Halaman ${current} dari ${total}`:'Tidak ada artikel yang cocok. Coba kata kunci atau kategori lain.';
      $('#blogPagination').innerHTML=Array.from({length:total},(_,i)=>`<li class="page-item${i+1===current?' active':''}"><button class="page-link" data-blog-page="${i+1}" aria-label="Halaman artikel ${i+1}"${i+1===current?' aria-current="page"':''}>${i+1}</button></li>`).join('');
    }
    $('#blogSearch').addEventListener('input',()=>{current=1;render();});
    $$('[data-blog-category]').forEach(btn=>btn.addEventListener('click',()=>{category=btn.dataset.blogCategory;current=1;$$('[data-blog-category]').forEach(b=>{b.classList.toggle('active',b===btn);b.setAttribute('aria-pressed',String(b===btn));});render();}));
    $('#blogPagination').addEventListener('click',e=>{const btn=e.target.closest('[data-blog-page]');if(!btn)return;current=Number(btn.dataset.blogPage);render();$(`[data-blog-page="${current}"]`)?.focus();});
    $$('[data-article-detail]').forEach(link=>link.addEventListener('click',e=>{e.preventDefault();const a=articles.find(a=>a.id===link.dataset.articleDetail);if(!a)return;showDetail('articleModal',a.title,`<img class="case-image" src="assets/img/workspace/${esc(a.image)}.svg" alt="Ilustrasi artikel"><p class="small text-muted">${esc(a.author)} · ${esc(a.date)} · ${esc(a.read)}</p><div class="article-body">${a.body.map(p=>`<p>${esc(p)}</p>`).join('')}</div>`,link);}));render();
  }

  if(page==='chat'){
    const contacts=[{id:'nina',name:'Nina Sari',role:'UI designer',color:'purple',unread:2},{id:'rio',name:'Rio Kurnia',role:'Frontend developer',color:'green',unread:1},{id:'dina',name:'Dina Putri',role:'Project manager',color:'orange',unread:0},{id:'creative',name:'Creative crew',role:'Ruang diskusi tim',color:'yellow',unread:0}];
    const seed={version:1,conversations:{nina:[{from:'them',body:'Pagi, Alex! Eksplorasi warna untuk website studio sudah siap.',time:'2026-09-28T09:10:00+08:00'},{from:'me',body:'Pagi! Aku suka arah lilac dan butter yellow. Bisa kita review setelah makan siang?',time:'2026-09-28T09:12:00+08:00'},{from:'them',body:'Bisa. Aku siapkan dua alternatif layout juga ya ✳',time:'2026-09-28T09:14:00+08:00'}],rio:[{from:'them',body:'Komponen navigasi sudah selesai. Silakan coba versi mobile-nya.',time:'2026-09-28T08:55:00+08:00'}],dina:[{from:'them',body:'Halo! Tenggat presentasi konsep hari Jumat. Kita masih punya waktu untuk eksplorasi.',time:'2026-09-27T16:10:00+08:00'}],creative:[{from:'them',body:'Selamat datang di ruang ide. Bagikan inspirasi atau progres kecilmu hari ini.',time:'2026-09-27T10:00:00+08:00'}]},read:[]};
    const state=read('chat',seed,v=>v&&v.version===1&&Array.isArray(v.read)&&v.read.every(text)&&v.conversations&&contacts.every(c=>Array.isArray(v.conversations[c.id])&&v.conversations[c.id].every(m=>m&&['me','them'].includes(m.from)&&text(m.body)&&text(m.time))));
    let active='nina';
    function contactsView(){
      const q=$('#chatSearch').value.trim().toLowerCase();const shown=contacts.filter(c=>c.name.toLowerCase().includes(q));
      $('#chatContacts').innerHTML=shown.map(c=>`<button type="button" class="chat-contact${c.id===active?' active':''}" data-chat-contact="${c.id}" aria-pressed="${c.id===active}"><span class="avatar bg-${c.color}">${initials(c.name)}</span><span class="chat-contact-copy"><strong>${c.name}</strong><small>${c.role}</small><small>${dateTime(state.conversations[c.id].at(-1)?.time||'')}</small></span>${!state.read.includes(c.id)&&c.unread?`<span class="badge bg-yellow">${c.unread}<span class="visually-hidden"> belum dibaca</span></span>`:''}</button>`).join('')||'<p class="p-4 small text-muted">Percakapan tidak ditemukan.</p>';
    }
    function conversation(){
      const c=contacts.find(c=>c.id===active);
      $('#chatHeader').innerHTML=`<span class="avatar bg-${c.color}">${initials(c.name)}</span><div><h2>${c.name}</h2><p>${c.role} · Percakapan demo</p></div>`;
      $('#chatInput').setAttribute('aria-label',`Pesan baru untuk ${c.name}`);
      $('#chatMessages').innerHTML=state.conversations[active].map(m=>`<div class="chat-message${m.from==='me'?' mine':''}"><div class="chat-bubble">${esc(m.body)}</div><time datetime="${esc(m.time)}">${m.from==='me'?'Kamu':c.name} · ${dateTime(m.time)}</time></div>`).join('');
      $('#chatMessages').scrollTop=$('#chatMessages').scrollHeight;
    }
    $('#chatSearch').addEventListener('input',contactsView);
    $('#chatContacts').addEventListener('click',e=>{const btn=e.target.closest('[data-chat-contact]');if(!btn)return;active=btn.dataset.chatContact;if(!state.read.includes(active))state.read.push(active);save('chat',state);contactsView();conversation();$(`[data-chat-contact="${active}"]`).focus();});
    $('#chatForm').addEventListener('submit',e=>{e.preventDefault();const input=$('#chatInput'),body=input.value.trim();if(!body){input.setCustomValidity('Tulis pesan terlebih dahulu.');input.reportValidity();return;}state.conversations[active].push({from:'me',body,time:new Date().toISOString()});save('chat',state);input.value='';contactsView();conversation();input.focus();});
    $('#chatInput').addEventListener('input',e=>e.target.setCustomValidity(''));
    if(!state.read.includes(active)){state.read.push(active);save('chat',state);}contactsView();conversation();
  }

  if(!page.startsWith('email-'))return;
  const folders={inbox:'Kotak masuk',starred:'Berbintang',sent:'Terkirim',draft:'Draft',spam:'Spam',trash:'Sampah'};
  const params=new URLSearchParams(location.search);
  const seedMail=(id,fromName,from,subject,body,folder='inbox',starred=false,unread=true)=>({id,fromName,from,to:'alex@example.com',cc:'',bcc:'',subject,body,folder,starred,unread,date:'2026-09-28T09:00:00+08:00',attachments:[]});
  const seed={version:1,messages:[
    {...seedMail('m1','Nina Sari','nina@example.com','Konsep website studio siap direview ✳','Halo Alex,\n\nAku sudah menyiapkan arah visual untuk website studio. Palet lilac dan mint terasa cocok untuk menonjolkan karya kita.\n\nCreative brief terlampir sebagai acuan. Bisa kita diskusikan alternatif homepage besok pagi?\n\nTerima kasih,\nNina','inbox',true),attachments:['creative-brief']},
    seedMail('m2','Rio Kurnia','rio@example.com','Update komponen untuk sprint ini','Halo tim,\n\nNavigasi mobile dan komponen form sudah siap. Silakan periksa sebelum sesi review berikutnya.\n\nSalam,\nRio'),
    seedMail('m3','Dina Putri','dina@example.com','Jadwal creative sync minggu ini','Hai Alex,\n\nKita akan membahas progres masing-masing proyek pada pertemuan berikutnya. Siapkan satu ide dan satu hal yang perlu dibantu.\n\nSampai jumpa!','inbox',false,false),
    seedMail('m4','Acme Creative','hello@example.com','Terima kasih untuk kolaborasinya','Halo BRUTAL. Studio,\n\nBrand guideline yang dikirim sudah kami terima. Tim kami menyukai arah visualnya. Sampai bertemu di proyek berikutnya.','inbox',true,false),
    {...seedMail('m5','Alex Darma','alex@example.com','Re: Timeline peluncuran','Halo Dina,\n\nTimeline sudah sesuai. Aku akan menyiapkan preview pada hari Kamis.\n\nAlex','sent',false,false),to:'dina@example.com'},
    {...seedMail('m6','Alex Darma','alex@example.com','Ide untuk kampanye berikutnya','Halo tim,\n\nAku ingin mendiskusikan konsep baru untuk kampanye bulan depan.','draft',false,false),to:'nina@example.com'},
    seedMail('m7','Promosi contoh','promo@example.com','Contoh pesan promosi','Ini pesan contoh untuk folder Spam. Tidak ada tautan atau layanan eksternal.','spam',false,false),
    seedMail('m8','Studio Archive','archive@example.com','Catatan rapat lama','Contoh pesan yang sudah dipindahkan ke Sampah. Kamu bisa memulihkannya.','trash',false,false)
  ]};
  const actualFolders=['inbox','sent','draft','spam','trash'];
  const mail=read('mail',seed,v=>v&&v.version===1&&Array.isArray(v.messages)&&v.messages.every(m=>m&&['id','fromName','from','to','cc','bcc','subject','body','date'].every(k=>text(m[k]))&&actualFolders.includes(m.folder)&&typeof m.starred==='boolean'&&typeof m.unread==='boolean'&&Array.isArray(m.attachments)&&m.attachments.every(text)));
  let folder=Object.hasOwn(folders,params.get('folder'))?params.get('folder'):'inbox';
  const matchesFolder=(m,f)=>f==='starred'?m.starred&&!['trash','spam','draft'].includes(m.folder):m.folder===f;
  function sidebar(){
    $$('[data-folder-count]').forEach(el=>el.textContent=mail.messages.filter(m=>matchesFolder(m,el.dataset.folderCount)).length);
    $$('[data-mail-folder]').forEach(el=>{const active=page==='email-inbox'&&el.dataset.mailFolder===folder;el.classList.toggle('active',active);if(active)el.setAttribute('aria-current','page');else el.removeAttribute('aria-current');});
  }
  sidebar();
  function persist(){return save('mail',mail);}
  const messageById=id=>mail.messages.find(m=>m.id===id);
  function missing(){return '<div class="mail-empty"><span aria-hidden="true">✳</span><h2>Pesan tidak ditemukan.</h2><p>Pesan ini mungkin tidak tersedia di browser kamu.</p><a class="btn btn-primary" href="email-inbox.html">Kembali ke inbox</a></div>';}
  function navigateAfterSave(url){if(persist())location.href=url;else sidebar();}

  if(page==='email-inbox'){
    const selected=new Set();
    const visible=()=>mail.messages.filter(m=>matchesFolder(m,folder)&&`${m.fromName} ${m.from} ${m.to} ${m.subject} ${m.body}`.toLowerCase().includes($('#mailSearch').value.trim().toLowerCase()));
    function toolbar(){const rows=visible(),count=rows.filter(m=>selected.has(m.id)).length;$('#mailSelectAll').checked=rows.length>0&&count===rows.length;$('#mailSelectAll').indeterminate=count>0&&count<rows.length;$('#mailSelectAll').disabled=!rows.length;$('#mailMarkRead').disabled=!count;$('#mailTrash').disabled=!count;$('#mailRestore').disabled=!count;$('#mailTrash').hidden=folder==='trash';$('#mailRestore').hidden=folder!=='trash';}
    function render(){
      const rows=visible();$('#mailFolderTitle').textContent=folders[folder];
      $('#mailRows').innerHTML=rows.length?rows.map(m=>`<div class="mail-row${m.unread?' unread':''}"><input class="form-check-input" type="checkbox" data-mail-select="${esc(m.id)}" aria-label="Pilih ${esc(m.subject||'Tanpa subjek')}"${selected.has(m.id)?' checked':''}><button class="mail-star" type="button" data-mail-star="${esc(m.id)}" aria-label="Bintang ${esc(m.subject||'Tanpa subjek')}" aria-pressed="${m.starred}">${m.starred?'★':'☆'}</button><span class="avatar bg-${m.folder==='sent'?'purple':'green'}">${esc(initials(m.fromName))}</span><a class="mail-open" href="${m.folder==='draft'?'email-compose.html?draft=':'email-read.html?id='}${encodeURIComponent(m.id)}"><span class="mail-row-heading"><span class="mail-sender">${esc(m.folder==='sent'?'Kepada: '+m.to:m.fromName)}</span><time class="mail-date" datetime="${esc(m.date)}">${dateTime(m.date)}</time></span><div class="mail-subject">${esc(m.subject||'(Tanpa subjek)')}</div><div class="mail-preview">${m.attachments.length?'↳ Lampiran · ':''}${esc(m.body||'(Pesan kosong)')}</div></a></div>`).join(''):'<div class="mail-empty"><span aria-hidden="true">✉</span><h2>Belum ada pesan di sini.</h2><p>Coba folder lain atau ubah kata pencarian.</p></div>';
      $('#mailCount').textContent=`${rows.length} pesan · ${rows.filter(m=>m.unread).length} belum dibaca`;toolbar();sidebar();
    }
    $('#mailSearch').addEventListener('input',()=>{selected.clear();render();});
    $('#mailSelectAll').addEventListener('change',e=>{visible().forEach(m=>e.target.checked?selected.add(m.id):selected.delete(m.id));render();});
    $('#mailRows').addEventListener('change',e=>{if(!e.target.matches('[data-mail-select]'))return;e.target.checked?selected.add(e.target.dataset.mailSelect):selected.delete(e.target.dataset.mailSelect);toolbar();});
    $('#mailRows').addEventListener('click',e=>{const btn=e.target.closest('[data-mail-star]');if(!btn)return;const m=messageById(btn.dataset.mailStar);m.starred=!m.starred;persist();render();$$('[data-mail-star]').find(b=>b.dataset.mailStar===m.id)?.focus();});
    $('#mailMarkRead').addEventListener('click',()=>{mail.messages.forEach(m=>{if(selected.has(m.id))m.unread=false;});persist();selected.clear();render();$('#mailNotice').textContent='Pesan terpilih sudah ditandai dibaca.';});
    $('#mailTrash').addEventListener('click',()=>{mail.messages.forEach(m=>{if(selected.has(m.id)){m.previousFolder=m.folder;m.folder='trash';}});persist();selected.clear();render();$('#mailNotice').textContent='Pesan dipindahkan ke Sampah. Kamu bisa memulihkannya dari folder tersebut.';});
    $('#mailRestore').addEventListener('click',()=>{mail.messages.forEach(m=>{if(selected.has(m.id))m.folder=actualFolders.includes(m.previousFolder)&&m.previousFolder!=='trash'?m.previousFolder:'inbox';});persist();selected.clear();render();$('#mailNotice').textContent='Pesan dikembalikan ke folder asal.';});
    const notice=params.get('notice');if(notice==='sent')$('#mailNotice').textContent='Pesan demo tersimpan di Terkirim. Tidak ada email yang dikirim ke penerima.';if(notice==='discarded')$('#mailNotice').textContent='Pesan dibuang. Draft tersimpan dapat dipulihkan dari Sampah.';
    render();
  }

  if(page==='email-read'){
    const id=params.has('id')?params.get('id'):'m1',m=messageById(id);
    if(!m){$('#mailReadContent').innerHTML=missing();return;}
    m.unread=false;persist();sidebar();
    $('#mailReadContent').innerHTML=`<span class="badge bg-green mb-3">${folders[m.folder]}</span><h2>${esc(m.subject||'(Tanpa subjek)')}</h2><div class="mail-reader-header"><span class="avatar bg-purple">${esc(initials(m.fromName))}</span><div class="mail-reader-meta"><strong>${esc(m.fromName)}</strong><small>Dari: ${esc(m.from)}</small><small>Kepada: ${esc(m.to)}</small>${m.cc?`<small>CC: ${esc(m.cc)}</small>`:''}${m.bcc&&['sent','draft'].includes(m.folder)?`<small>BCC: ${esc(m.bcc)}</small>`:''}<small>${dateTime(m.date)}</small></div></div><div class="mail-body">${esc(m.body)}</div>${m.attachments.includes('creative-brief')?'<h3>Lampiran</h3><div class="mail-attachments"><a class="mail-attachment" href="assets/files/creative-brief.txt" download>↧ Creative brief · TXT</a></div>':''}<div class="d-flex flex-wrap gap-3 no-print"><a class="btn btn-primary" href="email-compose.html?reply=${encodeURIComponent(m.id)}">Balas</a><a class="btn" href="email-compose.html?forward=${encodeURIComponent(m.id)}">Forward</a><button class="btn ms-sm-auto" type="button" id="mailPrint">Cetak</button></div>`;
    $('#mailPrint').addEventListener('click',()=>window.print());
  }

  if(page==='email-compose'){
    const form=$('#mailComposeForm');let draftId=null,dirty=false;
    const fields=['to','cc','bcc','subject','body'];
    const fill=m=>fields.forEach(k=>{form.elements[k].value=m[k]||'';});
    const draftParam=params.get('draft'),reply=params.get('reply'),forward=params.get('forward');
    if(params.has('draft')){
      const m=messageById(draftParam);if(!m||m.folder!=='draft'){form.hidden=true;form.insertAdjacentHTML('beforebegin',missing());return;}
      draftId=m.id;fill(m);$('#composeStatus').textContent='Draft tersimpan dibuka untuk diedit.';
    }else if(params.has('reply')||params.has('forward')){
      const m=messageById(reply??forward);if(!m){form.hidden=true;form.insertAdjacentHTML('beforebegin',missing());return;}
      fill({to:reply?(m.from==='alex@example.com'?m.to:m.from):'',subject:(reply?'Re: ':'Fwd: ')+m.subject,body:`\n\n--- ${reply?'Pesan sebelumnya':'Pesan diteruskan'} ---\nDari: ${m.fromName} <${m.from}>\nSubjek: ${m.subject}\n\n${m.body}`});
    }
    const data=()=>Object.fromEntries(fields.map(k=>[k,form.elements[k].value.trim()]));
    function upsert(folder){
      const values=data();let m=draftId?messageById(draftId):null;
      if(!m){m={...seedMail(uid(),'Alex Darma','alex@example.com','','',folder,false,false)};mail.messages.unshift(m);draftId=m.id;}
      Object.assign(m,values,{folder,date:new Date().toISOString(),unread:false});return m;
    }
    form.addEventListener('input',e=>{dirty=true;if(e.target.setCustomValidity)e.target.setCustomValidity('');});
    $('#mailSaveDraft').addEventListener('click',()=>{if(!Object.values(data()).some(Boolean)){$('#composeStatus').textContent='Isi minimal satu kolom sebelum menyimpan draft.';return;}const m=upsert('draft');if(persist()){dirty=false;$('#composeStatus').textContent='Draft disimpan. Kamu dapat membukanya kembali dari folder Draft.';try{history.replaceState(null,'','email-compose.html?draft='+encodeURIComponent(m.id));}catch{}}sidebar();});
    form.addEventListener('submit',e=>{e.preventDefault();for(const key of ['to','subject','body']){if(!form.elements[key].value.trim()){form.elements[key].setCustomValidity('Kolom ini tidak boleh kosong.');form.elements[key].reportValidity();return;}}if(!form.reportValidity())return;upsert('sent');if(persist()){dirty=false;location.href='email-inbox.html?folder=sent&notice=sent';}else{$('#composeStatus').textContent='Pesan belum tersimpan permanen. Aktifkan penyimpanan browser sebelum meninggalkan halaman.';}sidebar();});
    $('#mailDiscard').addEventListener('click',()=>{const m=messageById(draftId);if(m){m.previousFolder='draft';m.folder='trash';if(!persist())return;}dirty=false;location.href='email-inbox.html?notice=discarded';});
    window.addEventListener('beforeunload',e=>{if(dirty){e.preventDefault();e.returnValue='';}});
  }
})();
