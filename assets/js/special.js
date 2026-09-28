/* Phase 9 frontend demos. All user content stays in this browser. */
(() => {
  'use strict';
  const page = document.body.dataset.page;
  const $ = selector => document.querySelector(selector);
  const POST_KEY = 'brutal.posts';
  const samplePosts = [
    { id: 'seed-1', title: 'Buat ruang untuk ide berikutnya', category: 'Desain', tags: ['ide', 'visual'], body: 'Desain yang berani memberi setiap ide ruang untuk tumbuh. Mulai dari bentuk sederhana dan detail yang terasa dekat.', cover: 'assets/img/workspace/studio.svg', published: true },
    { id: 'seed-2', title: 'Produk kecil, dampak besar', category: 'Produk', tags: ['produk', 'proses'], body: 'Sebuah pengalaman yang baik lahir dari pertanyaan yang tepat, percobaan kecil, dan kemauan untuk terus belajar.', cover: 'assets/img/workspace/pocket.svg', published: true },
    { id: 'seed-3', title: 'Di balik meja studio', category: 'Studio', tags: ['studio', 'cerita'], body: 'Kumpulan catatan dari hari-hari ketika tim membuat, menguji, dan merapikan hal yang penting.', cover: 'assets/img/workspace/forma.svg', published: true },
  ];

  function readPosts() {
    try {
      const saved = JSON.parse(localStorage.getItem(POST_KEY));
      return Array.isArray(saved) ? saved : samplePosts;
    } catch { return samplePosts; }
  }

  function safeCover(source) {
    return typeof source === 'string' && (/^assets\/img\/workspace\/[a-z-]+\.svg$/.test(source) || /^data:image\/(png|jpeg|webp|gif);base64,[A-Za-z0-9+/=]+$/.test(source));
  }

  if (page === 'subscribe') {
    $('#subscribeForm').addEventListener('submit', event => {
      event.preventDefault();
      const email = $('#subscribeEmail').value.trim().toLowerCase();
      const status = $('#subscribeStatus');
      if (!event.currentTarget.reportValidity()) return;
      try {
        const saved = JSON.parse(localStorage.getItem('brutal.subscribers') || '[]');
        const list = Array.isArray(saved) ? saved : [];
        if (list.includes(email)) { status.textContent = 'Alamat ini sudah ada di daftar demo browser ini.'; return; }
        list.push(email);
        localStorage.setItem('brutal.subscribers', JSON.stringify(list));
        status.textContent = 'Berhasil masuk daftar demo lokal. Tidak ada email yang dikirim.';
        event.currentTarget.reset();
      } catch { status.textContent = 'Penyimpanan browser tidak tersedia. Coba izinkan localStorage.'; }
    });
  }

  if (page === 'create-post') {
    const editor = new Quill('#postEditor', { theme: 'snow', modules: { toolbar: [
      [{ header: [2, 3, false] }], ['bold', 'italic', 'underline'],
      [{ list: 'ordered' }, { list: 'bullet' }], ['link'], ['clean'],
    ] } });
    editor.root.setAttribute('aria-labelledby', 'postEditorLabel');
    const coverInput = $('#postCover');
    const coverPreview = $('#postCoverPreview');
    let coverData = '';
    coverInput.addEventListener('change', () => {
      const file = coverInput.files?.[0];
      const status = $('#postCoverStatus');
      coverData = '';
      coverPreview.hidden = true;
      coverPreview.removeAttribute('src');
      if (!file) { status.textContent = ''; return; }
      if (!['image/png', 'image/jpeg', 'image/webp', 'image/gif'].includes(file.type) || file.size > 500 * 1024) {
        status.textContent = 'Pilih PNG, JPG, WebP, atau GIF maksimal 500 KB.';
        coverInput.value = '';
        return;
      }
      const reader = new FileReader();
      reader.onload = () => {
        coverData = String(reader.result || '');
        coverPreview.src = coverData;
        coverPreview.hidden = false;
        status.textContent = `Cover siap: ${file.name}`;
      };
      reader.onerror = () => { status.textContent = 'Cover gagal dibaca. Coba file lain.'; };
      reader.readAsDataURL(file);
    });

    $('#createPostForm').addEventListener('submit', event => {
      event.preventDefault();
      const form = event.currentTarget;
      form.classList.add('was-validated');
      if (!form.checkValidity()) { $('#createPostStatus').textContent = 'Periksa judul dan kategori.'; return; }
      const body = editor.getText().trim();
      if (body.length < 20) { $('#postEditorError').textContent = 'Tulis isi post minimal 20 karakter.'; return; }
      $('#postEditorError').textContent = '';
      const tags = $('#postTags').value.split(',').map(tag => tag.trim()).filter(Boolean).slice(0, 5);
      const post = {
        id: crypto.randomUUID ? crypto.randomUUID() : String(Date.now()),
        title: $('#postTitle').value.trim(), category: $('#postCategory').value,
        tags, body: body.slice(0, 10000), cover: coverData || 'assets/img/workspace/bloom.svg',
        published: $('#postPublished').checked, createdAt: new Date().toISOString(),
      };
      try {
        localStorage.setItem(POST_KEY, JSON.stringify([post, ...readPosts()]));
        location.href = 'posts.html?created=1';
      } catch { $('#createPostStatus').textContent = 'Penyimpanan browser penuh atau tidak tersedia. Gunakan cover yang lebih kecil.'; }
    });
  }

  if (page === 'posts') {
    const grid = $('#postGrid');
    const empty = $('#postEmpty');
    const count = $('#postCount');
    const render = () => {
      const query = $('#postSearch').value.trim().toLocaleLowerCase('id');
      const category = $('#postFilter').value;
      const all = readPosts();
      const matches = all.filter(post => (!category || post.category === category) &&
        (!query || [post.title, post.body, ...(post.tags || [])].join(' ').toLocaleLowerCase('id').includes(query)));
      grid.replaceChildren();
      for (const post of matches) {
        const card = document.createElement('article');
        card.className = 'card post-card';
        const image = document.createElement('img');
        image.src = safeCover(post.cover) ? post.cover : 'assets/img/workspace/bloom.svg';
        image.alt = `Cover ${post.title}`;
        const content = document.createElement('div');
        content.className = 'card-body';
        const badge = document.createElement('span');
        badge.className = 'badge bg-yellow align-self-start';
        badge.textContent = `${post.category} · ${post.published ? 'Terbit' : 'Draft'}`;
        const title = document.createElement('h2');
        title.textContent = post.title;
        const excerpt = document.createElement('p');
        excerpt.textContent = post.body.length > 140 ? `${post.body.slice(0, 140)}…` : post.body;
        const tags = document.createElement('div');
        tags.className = 'post-card-tags';
        for (const tag of post.tags || []) {
          const label = document.createElement('span');
          label.textContent = `#${tag}`;
          tags.append(label);
        }
        content.append(badge, title, excerpt, tags);
        card.append(image, content);
        grid.append(card);
      }
      empty.hidden = matches.length > 0;
      count.textContent = `${matches.length} dari ${all.length} post ditampilkan.`;
    };
    $('#postSearch').addEventListener('input', render);
    $('#postFilter').addEventListener('change', render);
    render();
  }

  if (page === 'contact') {
    $('#contactForm').addEventListener('submit', event => {
      event.preventDefault();
      const form = event.currentTarget;
      form.classList.add('was-validated');
      if (!form.checkValidity()) { $('#contactStatus').textContent = 'Periksa kolom yang ditandai.'; return; }
      $('#contactStatus').textContent = `Pratinjau siap untuk ${$('#contactName').value.trim()}: “${$('#contactSubject').value}”. Pesan tidak dikirim.`;
    });
  }

  if (page?.startsWith('errors-')) {
    $('.special-error-actions button')?.addEventListener('click', () => {
      if (history.length > 1) history.back();
      else location.href = 'index.html';
    });
  }
})();
