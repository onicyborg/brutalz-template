"""Phase 9 special pages, publication demos, and error states."""

SPECIAL_PAGES = ('subscribe', 'create-post', 'posts', 'contact', 'multilevel')
ERROR_PAGES = ('errors-403', 'errors-404', 'errors-500', 'errors-503')


def subscribe():
    return '''<main class="special-subscribe" id="main">
      <header class="special-top"><a class="brand" href="index.html"><span class="brand-mark bg-yellow">b.</span>BRUTAL.</a><a class="btn btn-sm" href="index.html">Lihat dashboard ↗</a></header>
      <div class="special-subscribe-grid"><section class="subscribe-copy"><span class="eyebrow">NOTES FROM THE BOLD SIDE</span><h1>Ide bagus datang ke inbox.</h1><p>Cerita singkat tentang desain, produk, dan keberanian mencoba hal baru. Buat ruang untuk inspirasi berikutnya.</p>
      <form id="subscribeForm" class="subscribe-form"><label class="form-label" for="subscribeEmail">Alamat email</label><div class="subscribe-input-row"><input class="form-control" id="subscribeEmail" type="email" autocomplete="email" placeholder="kamu@studio.id" required maxlength="120"><button class="btn btn-dark" type="submit">Ikut daftar ↗</button></div><p id="subscribeStatus" class="small mt-3" role="status" aria-live="polite"></p></form>
      <p class="small text-muted">Demo lokal: tidak ada newsletter atau email yang dikirim. Alamat contoh hanya disimpan di browser ini.</p></section>
      <div class="subscribe-art" aria-hidden="true"><svg viewBox="0 0 520 460" xmlns="http://www.w3.org/2000/svg"><rect x="70" y="55" width="355" height="320" rx="18" fill="#232420"/><rect x="55" y="40" width="355" height="320" rx="18" fill="#fffefb" stroke="#232420" stroke-width="6"/><rect x="80" y="66" width="304" height="62" rx="8" fill="#c4a8f5" stroke="#232420" stroke-width="5"/><circle cx="110" cy="97" r="10" fill="#f9de6e" stroke="#232420" stroke-width="4"/><path d="M140 96h197" stroke="#232420" stroke-width="7" stroke-linecap="round"/><path d="M88 190l145 93 144-93" fill="none" stroke="#232420" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><path d="M86 190h292v120H86z" fill="#f9de6e" stroke="#232420" stroke-width="6"/><path d="M88 191l145 93 145-93" fill="#c7e8cc" stroke="#232420" stroke-width="6" stroke-linejoin="round"/><path d="M88 310l102-83m188 83-102-83" stroke="#232420" stroke-width="6"/><path d="M423 197l19 17-19 17-19-17zM26 252l16 14-16 14-16-14z" fill="#ffc7ad" stroke="#232420" stroke-width="5"/><path d="M433 52v48m-24-24h48" stroke="#232420" stroke-width="7" stroke-linecap="round"/></svg><span class="subscribe-sticker">GOOD IDEAS<br>INSIDE ↗</span></div></div>
      <footer class="special-bottom">© 2026 BRUTAL. · Built different.</footer></main>'''


def post_form(heading):
    return heading('Tulis sesuatu yang layak dibaca.', 'Buat artikel contoh dengan Quill, lalu lihat hasilnya di daftar post.') + '''
      <div class="row g-4"><div class="col-xl-8"><section class="card"><div class="card-body"><form id="createPostForm" novalidate>
      <div class="row g-3"><div class="col-12"><label class="form-label" for="postTitle">Judul post</label><input class="form-control" id="postTitle" required minlength="5" maxlength="100" placeholder="Contoh: Ide besar dimulai dari halaman kosong"><div class="invalid-feedback">Isi judul minimal 5 karakter.</div></div>
      <div class="col-md-6"><label class="form-label" for="postCategory">Kategori</label><select class="form-select" id="postCategory" required><option value="">Pilih kategori</option><option>Desain</option><option>Produk</option><option>Studio</option><option>Inspirasi</option></select><div class="invalid-feedback">Pilih kategori.</div></div>
      <div class="col-md-6"><label class="form-label" for="postTags">Tags</label><input class="form-control" id="postTags" maxlength="100" placeholder="desain, ide, proses"><div class="form-text">Pisahkan dengan koma; maksimal 5 tag.</div></div>
      <div class="col-12"><label class="form-label" for="postCover">Cover image</label><input class="form-control" id="postCover" type="file" accept="image/png,image/jpeg,image/webp,image/gif"><div class="form-text">PNG, JPG, WebP, atau GIF; maksimal 500 KB. Gambar tersimpan lokal untuk demo.</div><p id="postCoverStatus" class="small mt-2" role="status"></p><img id="postCoverPreview" class="post-cover-preview" alt="Pratinjau cover" hidden></div>
      <div class="col-12"><label class="form-label" id="postEditorLabel">Isi post</label><div id="postEditor" class="post-editor"><p>Mulai ceritamu di sini…</p></div><p id="postEditorError" class="small text-danger mt-2" role="status"></p></div></div>
      <div class="form-check form-switch mt-4"><input class="form-check-input" id="postPublished" type="checkbox" checked><label class="form-check-label" for="postPublished">Publikasikan sekarang</label></div>
      <div class="d-flex flex-wrap gap-2 mt-4"><button class="btn btn-primary" type="submit">Simpan post ↗</button><a class="btn" href="posts.html">Lihat daftar post</a></div><p id="createPostStatus" class="small mt-3" role="status" aria-live="polite"></p></form></div></section></div>
      <div class="col-xl-4"><section class="card bg-yellow"><div class="card-body"><span class="badge bg-white mb-3">EDITORIAL DESK</span><h2>Konten yang terasa hidup.</h2><p>Gunakan judul yang jelas, satu ide utama, dan cover yang mendukung cerita.</p><p class="small mb-0">Post disimpan di browser ini saja. Tombol publikasi mengubah status demo; tidak ada situs atau feed publik yang diperbarui.</p></div></section></div></div>'''


def posts(heading):
    return heading('Cerita dari studio.', 'Cari, saring, dan baca ringkasan post contoh yang tersimpan di browser ini.', '<a class="btn btn-primary" href="create-post.html">+ Buat post</a>') + '''
      <section class="card mb-4"><div class="card-body"><div class="post-toolbar"><div><label class="form-label" for="postSearch">Cari post</label><input class="form-control" id="postSearch" type="search" placeholder="Cari judul, isi, atau tag"></div><div><label class="form-label" for="postFilter">Kategori</label><select class="form-select" id="postFilter"><option value="">Semua kategori</option><option>Desain</option><option>Produk</option><option>Studio</option><option>Inspirasi</option></select></div></div><p id="postCount" class="small text-muted mt-3 mb-0" role="status"></p></div></section>
      <div id="postGrid" class="post-grid"></div><div id="postEmpty" class="card post-empty" hidden><div class="card-body text-center py-5"><span class="post-empty-icon" aria-hidden="true">✳</span><h2>Belum ada cerita di sini.</h2><p>Coba kata kunci lain atau buat post baru.</p><a class="btn btn-primary" href="create-post.html">Tulis post pertama</a></div></div>'''


def contact(heading):
    return heading('Mari mulai percakapan.', 'Punya ide, pertanyaan, atau ingin berkolaborasi? Kirim pesan contoh di bawah.') + '''
      <div class="row g-4"><div class="col-lg-7"><section class="card"><div class="card-body"><h2>Tinggalkan pesan.</h2><p class="small text-muted">Form ini mendemonstrasikan validasi dan umpan balik lokal.</p><form id="contactForm" novalidate><div class="row g-3"><div class="col-md-6"><label class="form-label" for="contactName">Nama lengkap</label><input class="form-control" id="contactName" autocomplete="name" required minlength="2" maxlength="70"><div class="invalid-feedback">Isi nama minimal 2 karakter.</div></div><div class="col-md-6"><label class="form-label" for="contactEmail">Email</label><input class="form-control" id="contactEmail" type="email" autocomplete="email" required><div class="invalid-feedback">Masukkan email yang valid.</div></div><div class="col-12"><label class="form-label" for="contactSubject">Topik</label><select class="form-select" id="contactSubject" required><option value="">Pilih topik</option><option>Proyek baru</option><option>Kolaborasi</option><option>Pertanyaan umum</option></select><div class="invalid-feedback">Pilih topik.</div></div><div class="col-12"><label class="form-label" for="contactMessage">Pesan</label><textarea class="form-control" id="contactMessage" rows="6" required minlength="10" maxlength="1000" placeholder="Ceritakan idemu…"></textarea><div class="invalid-feedback">Tulis minimal 10 karakter.</div></div></div><button class="btn btn-primary mt-4" type="submit">Pratinjau pesan ↗</button><p id="contactStatus" class="small mt-3 mb-0" role="status" aria-live="polite"></p></form></div></section></div>
      <div class="col-lg-5"><section class="card bg-purple"><div class="card-body"><span class="badge bg-yellow mb-3">BRUTAL. STUDIO</span><h2>Temukan kami.</h2><dl class="contact-details"><dt>Alamat contoh</dt><dd>Jl. Ide Baru No. 8<br>Jakarta, Indonesia</dd><dt>Telepon contoh</dt><dd>+62 21 5550 2026</dd><dt>Email contoh</dt><dd>halo@example.com</dd><dt>Sosial</dt><dd><span class="contact-social">Instagram</span><span class="contact-social">Behance</span><span class="contact-social">LinkedIn</span></dd></dl><p class="small mb-0">Informasi kontak ini hanya ilustrasi template. Pesan tidak dikirim ke server.</p></div></section></div></div>'''


def multilevel(heading):
    return heading('Menu bertingkat, tetap mudah diikuti.', 'Halaman ini berada pada tingkat terdalam menu Multilevel di sidebar.') + '''
      <section class="card"><div class="card-body"><span class="badge bg-yellow mb-3">LEVEL 3</span><h2>Tiga tingkat. Satu tujuan.</h2><p>Di sidebar, buka <strong>Multilevel → Level 1 → Level 2 → Level 3</strong>. Menu aktif dan semua induknya otomatis terbuka saat halaman ini dipilih.</p><div class="multilevel-path"><span>Multilevel</span><b>›</b><span>Level 1</span><b>›</b><span>Level 2</span><b>›</b><strong>Level 3</strong></div><p class="small text-muted mt-4 mb-0">Gunakan Tab dan Enter untuk membuka atau menutup setiap tingkat dari keyboard.</p></div></section>'''


def error_page(code):
    content = {
        '403': ('Akses ditolak.', 'Pintu ini belum terbuka untukmu. Kembali ke ruang kerja atau lihat halaman lain.', 'bg-orange'),
        '404': ('Halaman tidak ditemukan.', 'Tautan yang kamu cari mungkin sudah pindah. Yuk, kembali ke awal.', 'bg-yellow'),
        '500': ('Ada kendala di server.', 'Sesuatu terhenti di belakang layar. Coba kembali beberapa saat lagi.', 'bg-purple'),
        '503': ('Sedang dirawat.', 'Kami sedang merapikan ruang ini. Silakan mampir lagi nanti.', 'bg-green'),
    }[code]
    title, description, color = content
    return f'''<main id="main" class="special-error"><a class="brand" href="index.html"><span class="brand-mark {color}">b.</span>BRUTAL.</a>
      <div class="special-error-content"><svg class="error-art" viewBox="0 0 260 190" role="img" aria-label="Ilustrasi halaman {code}" xmlns="http://www.w3.org/2000/svg"><rect x="40" y="23" width="180" height="145" rx="9" fill="#232420"/><rect x="26" y="10" width="180" height="145" rx="9" fill="#fffefb" stroke="#232420" stroke-width="5"/><path d="M27 48h179" stroke="#232420" stroke-width="5"/><circle cx="49" cy="29" r="6" fill="#ffc7ad" stroke="#232420" stroke-width="3"/><circle cx="70" cy="29" r="6" fill="#f9de6e" stroke="#232420" stroke-width="3"/><path d="M88 83h54m-54 24h79" stroke="#232420" stroke-width="7" stroke-linecap="round"/><path d="m157 101 36 36m0-36-36 36" stroke="#7951ae" stroke-width="10" stroke-linecap="round"/><path d="M230 27v36m-18-18h36" stroke="#232420" stroke-width="6" stroke-linecap="round"/></svg><span class="badge {color}">ERROR {code}</span><div class="error-code">{code}</div><h1>{title}</h1><p>{description}</p><div class="special-error-actions"><a class="btn btn-primary" href="index.html">Kembali ke dashboard ↗</a><button class="btn" type="button" onclick="history.back()">Halaman sebelumnya</button></div></div>
      <p class="small text-muted">© 2026 BRUTAL. · Halaman status demonstrasi.</p></main>'''


def build_special_pages(heading):
    return {
        'subscribe': subscribe(),
        'create-post': post_form(heading),
        'posts': posts(heading),
        'contact': contact(heading),
        'multilevel': multilevel(heading),
    }
