"""Individual Bootstrap component demos and their sidebar catalog."""
from html import escape

CATALOG = [
    ('alert', 'Alert', 'Pesan kontekstual, ikon, judul, dan dismissible alerts.'),
    ('badge', 'Badge', 'Label status, pill, penghitung, dan notifikasi.'),
    ('breadcrumb', 'Breadcrumb', 'Jejak navigasi dengan divider, ikon, dan warna.'),
    ('buttons', 'Buttons', 'Warna, outline, ukuran, state, ikon, dan button group.'),
    ('collapse', 'Collapse', 'Panel sederhana, multiple targets, dan accordion.'),
    ('dropdown', 'Dropdown', 'Menu sederhana, split button, arah, dan header.'),
    ('checkbox-and-radio', 'Checkbox & Radios', 'Pilihan tunggal dan jamak, switch, warna, dan toggle.'),
    ('list-group', 'List Group', 'Daftar dasar, tautan, badge, dan panel interaktif.'),
    ('media-object', 'Media Object', 'Avatar dan konten, nesting, daftar, serta alignment.'),
    ('navbar', 'Navbar', 'Brand, navigasi responsif, pencarian, dan teks.'),
    ('pagination', 'Pagination', 'Navigasi halaman, state, ikon, ukuran, dan alignment.'),
    ('popover', 'Popover', 'Informasi tambahan dalam popover yang interaktif.'),
    ('progress', 'Progress', 'Progres dengan label, warna, tinggi, dan animasi.'),
    ('tooltip', 'Tooltip', 'Bantuan singkat untuk tombol, tautan, dan teks.'),
    ('flags', 'Flag', 'Bendera SVG lokal dengan variasi ukuran dan pencarian.'),
    ('typography', 'Typography', 'Heading, display, warna teks, kutipan, dan daftar.'),
]
VARIANTS = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark']


def demo(title, description, markup, wide=False):
    readable_markup = markup.replace('><', '>\n<')
    return f'''<section class="card component-demo{' demo-wide' if wide else ''}"><div class="card-body"><h2>{title}</h2><p class="small text-muted mb-4">{description}</p><div class="component-preview">{markup}</div><details class="demo-source"><summary>Lihat markup</summary><pre class="code mt-3 mb-0"><code>{escape(readable_markup)}</code></pre></details></div></section>'''


def row(markup):
    return f'<div class="demo-row">{markup}</div>'


def button(label, variant='primary', attrs=''):
    return f'<button type="button" class="btn btn-{variant}" {attrs}>{label}</button>'


def overview(heading, icon):
    links = ''.join(f'<a class="card component-link" href="{path}.html"><div class="card-body"><span class="eyebrow text-muted">COMPONENT {i:02}</span><h2 class="mt-3">{escape(title)} <span aria-hidden="true">↗</span></h2><p class="small text-muted mb-0">{desc}</p></div></a>' for i, (path, title, desc) in enumerate(CATALOG, 1))
    extra = demo('Workspace utilities', 'Modal dan toast tetap tersedia untuk interaksi lintas halaman.', row(button('Buka modal',attrs='data-bs-toggle="modal" data-bs-target="#projectModal"')+button('Tampilkan toast','warning','data-toast="Halo! Notifikasi workspace siap dipakai."')))
    return heading('Komponen, penuh karakter.', 'Pilih salah satu dari 16 komponen. Setiap halaman punya variasi dan markup siap pakai.', '<a class="btn" href="docs.html#components">'+icon('code')+' Panduan penggunaan</a>')+f'<div class="component-catalog">{links}</div><div class="mt-4">{extra}</div>'


def alert_page(icon):
    basic = ''.join(f'<div class="alert alert-{v}" role="alert">Ini pesan <strong>{v}</strong> untuk workspace kamu.</div>' for v in VARIANTS)
    icons = ''.join(f'<div class="alert alert-{v} d-flex align-items-center gap-3" role="alert">{icon(i)}<span>{text}</span></div>' for v,i,text in [('success','check','Perubahan berhasil disimpan.'),('warning','bolt','Masih ada tugas yang belum selesai.'),('danger','close','Proyek gagal diperbarui. Coba lagi.'),('info','mail','Ada pesan baru untuk tim kamu.')])
    title = '<div class="alert alert-success" role="alert"><h3 class="alert-heading">Semua siap untuk diluncurkan!</h3><p>Seluruh komponen sudah diperiksa oleh tim.</p><hr><p class="mb-0 small">Lanjutkan ke <a class="alert-link" href="projects.html">halaman proyek</a> untuk melihat progresnya.</p></div>'
    dismiss = '<div class="alert alert-warning alert-dismissible fade show" role="alert"><strong>Simpan idemu.</strong> Ada perubahan yang belum disimpan.<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Tutup contoh alert"></button></div><p class="small text-muted mb-0">Muat ulang halaman untuk menampilkan pesan ini kembali.</p>'
    return demo('Default','Delapan warna kontekstual Bootstrap.',basic)+demo('Dengan ikon','Ikon SVG lokal membantu memperjelas jenis pesan.',icons)+demo('Judul & tautan','Pesan panjang dengan heading, divider, dan tautan.',title)+demo('Dismissible','Tutup pesan dengan tombol di sisi kanan.',dismiss)


def badge_page(icon):
    headings = ''.join(f'<div class="h{i} mb-3">Heading {i} <span class="badge text-bg-primary">Baru</span></div>' for i in range(2,7))
    variants = row(''.join(f'<span class="badge text-bg-{v}">{v.title()}</span>' for v in VARIANTS))+row(''.join(f'<span class="badge rounded-pill text-bg-{v}">{v.title()}</span>' for v in VARIANTS))
    buttons = row(button('Inbox <span class="badge text-bg-light">8<span class="visually-hidden"> pesan belum dibaca</span></span>',attrs='data-toast="Kamu punya 8 pesan demo."')+button('Tugas <span class="badge text-bg-dark">12</span>','warning','data-toast="Ada 12 tugas demo."'))
    position = '<div class="p-3">'+button('Notifikasi <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill text-bg-danger">9+<span class="visually-hidden"> notifikasi belum dibaca</span></span>','primary','style="position:relative" data-toast="Ini contoh badge notifikasi."')+'</div>'
    links = row(''.join(f'<a href="{link}.html" class="badge text-bg-{v} text-decoration-none">{text} ↗</a>' for link,v,text in [('projects','success','Proyek'),('forms','warning','Form'),('docs','info','Dokumentasi')]))
    return demo('Heading','Label ringkas di samping judul.',headings)+demo('Warna & pill','Badge bersudut dan rounded-pill.',variants)+demo('Di dalam tombol','Counter yang punya konteks untuk pembaca layar.',buttons)+demo('Posisi notifikasi','Badge ditempatkan di sudut tombol.',position)+demo('Badge sebagai tautan','Tautan ringkas ke halaman lain.',links)


def crumb(items, label, attrs=''):
    return f'<nav aria-label="{label}" {attrs}><ol class="breadcrumb mb-0">'+''.join(f'<li class="breadcrumb-item{" active" if not href else ""}"'+(' aria-current="page"' if not href else '')+f'>{f"<a href={href}>{text}</a>" if href else text}</li>' for text,href in items)+'</ol></nav>'


def breadcrumb_page(icon):
    path=[('Workspace','index.html'),('Komponen UI','components.html'),('Breadcrumb',None)]
    basic = '<div class="d-grid gap-4">'+crumb([('Home',None)],'Satu tingkat')+crumb([('Home','index.html'),('Komponen',None)],'Dua tingkat')+crumb(path,'Tiga tingkat')+'</div>'
    icons = crumb([(icon('grid')+'<span class="visually-hidden">Workspace</span>','index.html'),('Komponen UI','components.html'),('Breadcrumb',None)],'Breadcrumb dengan ikon')
    bg = ''.join(f'<div class="breadcrumb-surface bg-{color} mb-3">{crumb(path,"Breadcrumb "+color)}</div>' for color in ['purple','yellow','green'])
    divider = crumb(path,'Divider panah','style="--bs-breadcrumb-divider: \'→\';"')
    return demo('Default','Satu, dua, dan tiga tingkat navigasi.',basic)+demo('Dengan ikon','Ikon Home tetap memiliki label aksesibel.',icons)+demo('Background','Surface pastel untuk menonjolkan jalur navigasi.',bg)+demo('Custom divider','Gunakan CSS variable Bootstrap untuk mengganti pemisah.',divider)


def buttons_page(icon):
    basic = row(''.join(button(v.title(),v,f'data-toast="Tombol {v} diklik."') for v in VARIANTS))
    outline = row(''.join(button(v.title(),'outline-'+v,f'data-toast="Outline {v} diklik."') for v in VARIANTS if v != 'light'))
    sizes = row(''.join(f'<button type="button" class="btn btn-primary {size}" data-toast="Ukuran {label}.">{label}</button>' for size,label in [('btn-lg','Large'),('','Default'),('btn-sm','Small')]))
    states = row(button('Toggle aktif',attrs='data-bs-toggle="button" aria-pressed="false"')+button('Disabled','primary','disabled')+button('Disabled outline','outline-primary','disabled'))
    icons = row(button(icon('plus')+' Proyek',attrs='data-bs-toggle="modal" data-bs-target="#projectModal"')+button(icon('download')+' Unduh','warning','data-toast="Contoh tombol unduh diklik."')+button(icon('heart'),'danger','aria-label="Suka" data-bs-toggle="button" aria-pressed="false"')+button(icon('settings'),'info','aria-label="Pengaturan contoh" data-toast="Contoh pengaturan."'))
    group = '<div class="btn-group mb-4" role="group" aria-label="Aksi editor">'+''.join(button(label,'outline-primary',f'data-toast="{label} dipilih."') for label in ['Salin','Tempel','Simpan'])+'</div><div><div class="btn-group-vertical" role="group" aria-label="Aksi vertikal">'+''.join(button(label,'primary',f'data-toast="{label} dipilih."') for label in ['Atas','Tengah','Bawah'])+'</div></div>'
    return demo('Basic','Semua varian warna Bootstrap.',basic)+demo('Outline','Border tegas dengan warna saat hover.',outline)+demo('Ukuran','Large, default, dan small.',sizes)+demo('State & toggle','Toggle menyimpan state aria-pressed. Disabled tidak dapat diklik.',states)+demo('Tombol ikon','Dengan label atau ikon saja.',icons)+demo('Button group','Grup horizontal dan vertikal.',group)


def collapse_page(icon):
    simple = row(button('Buka / tutup panel',attrs='data-bs-toggle="collapse" data-bs-target="#simplePanel" aria-expanded="false" aria-controls="simplePanel"'))+'<div class="collapse" id="simplePanel"><div class="demo-inset bg-green">Ide yang baik butuh ruang. Panel ini memakai Collapse Bootstrap.</div></div>'
    multi = row(button('Panel pertama','primary','data-bs-toggle="collapse" data-bs-target="#multiOne" aria-expanded="false" aria-controls="multiOne"')+button('Panel kedua','warning','data-bs-toggle="collapse" data-bs-target="#multiTwo" aria-expanded="false" aria-controls="multiTwo"')+button('Keduanya','dark','data-bs-toggle="collapse" data-bs-target=".multi-demo" aria-expanded="false" aria-controls="multiOne multiTwo"'))+'<div class="row g-3"><div class="col-sm-6"><div class="collapse multi-demo" id="multiOne"><div class="demo-inset bg-purple">Ruang untuk ide pertama.</div></div></div><div class="col-sm-6"><div class="collapse multi-demo" id="multiTwo"><div class="demo-inset bg-yellow">Ruang untuk ide kedua.</div></div></div></div>'
    accordion='<div class="accordion" id="componentAccordion">'+''.join(f'<div class="accordion-item"><h3 class="accordion-header"><button class="accordion-button{" collapsed" if i else ""}" type="button" data-bs-toggle="collapse" data-bs-target="#accordionPanel{i}" aria-expanded="{"false" if i else "true"}" aria-controls="accordionPanel{i}">{q}</button></h3><div id="accordionPanel{i}" class="accordion-collapse collapse{" show" if not i else ""}" data-bs-parent="#componentAccordion"><div class="accordion-body">{a}</div></div></div>' for i,(q,a) in enumerate([('Apa itu BRUTAL.?','Template Bootstrap dengan karakter Neubrutalism.'),('Bisakah warnanya diganti?','Ya. Ubah token --neo-* pada stylesheet tema.'),('Apakah memerlukan internet?','Tidak. Seluruh aset demo tersedia lokal.')]))+'</div>'
    return demo('Simple','Satu tombol untuk satu panel.',simple)+demo('Multiple targets','Kontrol panel secara terpisah atau bersamaan.',multi)+demo('Accordion','Satu panel terbuka pada satu waktu.',accordion,True)


def menu_markup(extra=''):
    return f'<ul class="dropdown-menu {extra}"><li><h3 class="dropdown-header">Workspace</h3></li><li><a class="dropdown-item" href="projects.html">Proyek</a></li><li><a class="dropdown-item" href="profile.html">Profil</a></li><li><hr class="dropdown-divider"></li><li><button class="dropdown-item" type="button" data-toast="Aksi menu dipilih.">Aksi demo</button></li><li><button class="dropdown-item" type="button" disabled>Arsip (disabled)</button></li></ul>'


def dropdown_page(icon):
    def dropdown(label, variant='primary', direction='', size=''):
        return f'<div class="dropdown {direction}"><button class="btn btn-{variant} dropdown-toggle {size}" type="button" data-bs-toggle="dropdown" aria-expanded="false">{label}</button>{menu_markup()}</div>'
    simple = row(dropdown('Pilih aksi')+dropdown('Pilihan lain','warning'))
    split = '<div class="btn-group">'+button('Simpan','success','data-toast="Contoh perubahan disimpan."')+'<button type="button" class="btn btn-success dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false"><span class="visually-hidden">Opsi penyimpanan</span></button>'+menu_markup()+'</div>'
    directions = row(dropdown('Ke atas','primary','dropup')+dropdown('Ke kanan','info','dropend')+dropdown('Ke kiri','warning','dropstart'))
    sizes = row(dropdown('Large','primary',size='btn-lg')+dropdown('Small','primary',size='btn-sm'))
    icons = '<div class="dropdown">'+button(icon('settings')+' Pengaturan',attrs='data-bs-toggle="dropdown" aria-expanded="false"')+'<ul class="dropdown-menu"><li><a class="dropdown-item" href="profile.html">'+icon('user')+' Profil</a></li><li><a class="dropdown-item" href="docs.html">'+icon('book')+' Dokumentasi</a></li></ul></div>'
    header = '<div class="d-flex justify-content-end"><div class="dropdown">'+button('Menu rata kanan','dark','data-bs-toggle="dropdown" aria-expanded="false"')+menu_markup('dropdown-menu-end')+'</div></div>'
    return demo('Simple','Menu kontekstual dengan tautan dan aksi.',simple)+demo('Split button','Aksi utama dan menu tambahan.',split)+demo('Direction','Popper menyesuaikan posisi dengan ruang yang tersedia.',directions)+demo('Size','Ukuran pemicu mengikuti ukuran button.',sizes)+demo('Dengan ikon','Ikon memberi konteks pada item menu.',icons)+demo('Header & alignment','Header, divider, item disabled, dan rata kanan.',header)


def check_control(id_, label, kind='checkbox', attrs='', cls=''):
    return f'<div class="form-check {cls}"><input class="form-check-input" type="{kind}" id="{id_}" {attrs}><label class="form-check-label" for="{id_}">{label}</label></div>'


def checks_page(icon):
    basic='<div class="d-grid gap-3">'+check_control('checkDefault','Default')+check_control('checkSelected','Terpilih',attrs='checked')+check_control('checkMixed','Sebagian dipilih',attrs='data-indeterminate')+check_control('checkDisabled','Disabled',attrs='disabled')+'</div>'
    radios='<fieldset><legend class="form-label">Prioritas pekerjaan</legend><div class="d-grid gap-3">'+check_control('radioNormal','Normal','radio','name="priorityDemo" checked')+check_control('radioHigh','Tinggi','radio','name="priorityDemo"')+check_control('radioDisabled','Disabled','radio','name="priorityDemo" disabled')+'</div></fieldset>'
    switches='<div class="d-grid gap-3">'+check_control('switchEmail','Notifikasi email',attrs='role="switch" checked',cls='form-switch')+check_control('switchPush','Notifikasi desktop',attrs='role="switch"',cls='form-switch')+check_control('switchLocked','Tidak tersedia',attrs='role="switch" disabled',cls='form-switch')+'</div>'
    colors='<div class="d-grid gap-3">'+''.join(check_control('color-'+v, v.title(), attrs='checked',cls='check-'+v) for v in ['primary','success','warning','danger'])+'</div>'
    inline='<fieldset><legend class="form-label">Keahlian</legend>'+''.join(check_control('skill'+str(i),label,cls='form-check-inline') for i,label in enumerate(['Design','Frontend','Backend']))+'</fieldset><hr><fieldset><legend class="form-label">Ukuran tim</legend>'+''.join(check_control('team'+str(i),label,'radio','name="teamSize"'+(' checked' if i==0 else ''),cls='form-check-inline') for i,label in enumerate(['Solo','2–5','6+']))+'</fieldset>'
    toggles='<div class="demo-row"><input class="btn-check" type="checkbox" id="favoriteToggle" autocomplete="off"><label class="btn btn-outline-primary" for="favoriteToggle">'+icon('heart')+' Favorit</label><input class="btn-check" type="checkbox" id="publishToggle" autocomplete="off" checked><label class="btn btn-outline-primary" for="publishToggle">'+icon('check')+' Publik</label></div><div class="btn-group" role="group" aria-label="Mode tampilan">'+''.join(f'<input class="btn-check" type="radio" name="viewMode" id="view{i}" autocomplete="off" {"checked" if i==0 else ""}><label class="btn btn-outline-primary" for="view{i}">{label}</label>' for i,label in enumerate(['Grid','List']))+'</div>'
    return demo('Basic checkbox','Default, checked, indeterminate, dan disabled.',basic)+demo('Radio buttons','Pilihan dalam satu grup bersifat eksklusif.',radios)+demo('Switch','Kontrol on/off memakai checkbox native.',switches)+demo('Color checkbox','Warna kontekstual dengan indikator checked.',colors)+demo('Inline controls','Grup input ringkas yang bisa membungkus di mobile.',inline)+demo('Toggle buttons & icons','Label tombol terhubung ke input native.',toggles)


def list_page(icon):
    basic='<ul class="list-group"><li class="list-group-item active" aria-current="true">Desain sistem</li><li class="list-group-item">Pengembangan frontend</li><li class="list-group-item">Dokumentasi</li><li class="list-group-item disabled" aria-disabled="true">Arsip terkunci</li></ul>'
    flush='<ul class="list-group list-group-flush">'+''.join(f'<li class="list-group-item">{t}</li>' for t in ['Riset pengguna','Eksplorasi visual','Prototype','Evaluasi'])+'</ul>'
    badges='<ul class="list-group">'+''.join(f'<li class="list-group-item d-flex justify-content-between align-items-center">{t}<span class="badge text-bg-{v} rounded-pill">{n}</span></li>' for t,v,n in [('Ide baru','primary',12),('Dalam pengerjaan','warning',4),('Selesai','success',8)])+'</ul>'
    links='<div class="list-group">'+''.join(f'<a class="list-group-item list-group-item-action" href="{p}.html">{icon(i)} <span class="ms-2">{t}</span></a>' for p,i,t in [('projects','folder','Buka proyek'),('calendar','calendar','Lihat kalender'),('profile','user','Atur profil')])+'</div>'
    tabs='<div class="list-group mb-3" role="tablist" aria-label="Panel workspace">'+''.join(f'<button type="button" class="list-group-item list-group-item-action{" active" if i==0 else ""}" id="listTab{i}" data-bs-toggle="list" data-bs-target="#listPane{i}" role="tab" aria-controls="listPane{i}" aria-selected="{"true" if i==0 else "false"}">{t}</button>' for i,t in enumerate(['Ringkasan','Aktivitas','Pengaturan']))+'</div><div class="tab-content demo-inset">'+''.join(f'<div class="tab-pane fade{" show active" if i==0 else ""}" id="listPane{i}" role="tabpanel" aria-labelledby="listTab{i}" tabindex="0">{t}</div>' for i,t in enumerate(['Semua ide workspace dalam satu tempat.','Nina memperbarui desain landing page.','Preferensi tampilan bisa diubah lewat halaman profil.']))+'</div>'
    custom='<div class="list-group"><a href="projects.html" class="list-group-item list-group-item-action"><div class="d-flex justify-content-between gap-2"><h3>Website studio</h3><small>Hari ini</small></div><p class="mb-1 small">Desain baru sudah siap ditinjau tim.</p><small class="text-muted">Alex Darma · Website</small></a><a href="calendar.html" class="list-group-item list-group-item-action"><h3>Creative sync</h3><p class="small mb-0">Lihat agenda pertemuan berikutnya.</p></a></div>'
    contextual='<ul class="list-group">'+''.join(f'<li class="list-group-item list-group-item-{v}">Item {v}</li>' for v in VARIANTS)+'</ul>'
    return ''.join([demo('Basic, active & disabled','Status item dalam satu daftar.',basic),demo('Flush','Tanpa border luar untuk konten dalam kartu.',flush),demo('Badge counters','Jumlah item selalu terlihat.',badges),demo('Tautan & ikon','Seluruh baris dapat diklik.',links),demo('JavaScript behavior','Pilih item untuk mengganti isi panel.',tabs),demo('Custom content','Gabungkan judul, metadata, dan deskripsi.',custom),demo('Contextual classes','Warna kontekstual untuk setiap item.',contextual)])


def media_page(icon):
    def media(name, text, initials='AD', align='start', reverse=False, child=''):
        return f'<div class="d-flex align-items-{align} gap-3{" flex-row-reverse" if reverse else ""}"><span class="avatar media-avatar bg-purple">{initials}</span><div class="flex-grow-1"><h3>{name}</h3><p class="small text-muted mb-0">{text}</p>{child}</div></div>'
    basic=media('Alex Darma','Ide yang sederhana bisa menjadi awal dari produk yang luar biasa.')
    listing='<ul class="list-unstyled mb-0">'+''.join('<li class="py-3'+(' border-top' if i else '')+'">'+media(n,t,initials)+'</li>' for i,(n,t,initials) in enumerate([('Alex Darma','Mengunggah konsep visual baru.','AD'),('Nina Sari','Menambahkan feedback untuk tim.','NS'),('Rio Kurnia','Menyelesaikan komponen navigasi.','RK')]))+'</ul>'
    nested=media('Alex Darma','Bagaimana kalau kita pakai palet lilac?',child='<div class="mt-4">'+media('Nina Sari','Setuju! Kontrasnya cocok dengan border gelap.','NS')+'</div>')
    order=media('Konten dulu, avatar kemudian.','Gunakan flex-row-reverse untuk mengubah urutan visual.',reverse=True)
    aligns='<div class="d-grid gap-4">'+''.join(media('Align '+a,'Avatar mengikuti posisi '+a+'. Konten panjang akan membungkus dan tetap terbaca pada layar kecil.','AD',a) for a in ['start','center','end'])+'</div>'
    return demo('Simple','Pola media object dibangun dengan flex utilities Bootstrap 5.',basic)+demo('List','Aktivitas atau komentar dalam bentuk daftar.',listing)+demo('Nesting','Balasan bersarang di dalam konten utama.',nested)+demo('Order','Ubah posisi avatar tanpa kelas media Bootstrap 4.',order)+demo('Vertical alignment','Align start, center, dan end.',aligns,True)


def navbar_page(icon):
    brand='<nav class="navbar demo-navbar bg-purple" aria-label="Contoh navbar brand"><div class="container-fluid"><a class="navbar-brand fw-bold" href="index.html">BRUTAL.</a><span class="navbar-text small">Creative workspace</span></div></nav>'
    responsive='<nav class="navbar navbar-expand-lg demo-navbar bg-yellow" aria-label="Contoh navbar responsif"><div class="container-fluid"><a class="navbar-brand fw-bold" href="index.html">Studio.</a><button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#demoNavbarMenu" aria-controls="demoNavbarMenu" aria-expanded="false" aria-label="Buka menu contoh navbar"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="demoNavbarMenu"><ul class="navbar-nav ms-auto"><li class="nav-item"><a class="nav-link active" href="navbar.html" aria-current="page">Home</a></li><li class="nav-item"><a class="nav-link" href="projects.html">Proyek</a></li><li class="nav-item dropdown"><button class="nav-link dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">Lainnya</button>'+menu_markup()+'</li><li class="nav-item"><span class="nav-link disabled" aria-disabled="true">Arsip</span></li></ul></div></div></nav>'
    form='<nav class="navbar demo-navbar bg-green" aria-label="Contoh navbar pencarian"><div class="container-fluid gap-3"><a class="navbar-brand fw-bold" href="index.html">Find your idea.</a><form class="d-flex gap-2 navbar-demo-search" role="search"><input class="form-control" type="search" aria-label="Cari di navbar contoh" placeholder="Cari ide…" required><button class="btn btn-dark" type="submit">Cari</button></form></div></nav><p id="navbarSearchResult" class="small mt-3 mb-0" role="status"></p>'
    text='<nav class="navbar demo-navbar" aria-label="Contoh navbar teks"><div class="container-fluid gap-3"><span class="navbar-text">Masuk sebagai <strong>Alex Darma</strong></span><a class="btn btn-sm btn-primary" href="profile.html">Lihat profil ↗</a></div></nav>'
    return demo('Brand','Identitas dan teks pendamping dalam navbar.',brand,True)+demo('Items & responsive collapse','Menu berubah menjadi toggler pada layar kecil.',responsive,True)+demo('Form pencarian','Form demo memberi feedback tanpa berpindah halaman.',form,True)+demo('Teks & aksi','Navbar juga dapat berisi informasi akun.',text,True)


def pagination_markup(id_, size='', align='', arrows=False):
    return f'<div data-pagination-demo id="{id_}"><nav aria-label="Contoh pagination {id_}"><ul class="pagination {size} {align} flex-wrap gap-1"><li class="page-item disabled"><button class="page-link" type="button" data-page-step="-1" aria-label="Sebelumnya" disabled>{"←" if arrows else "Prev"}</button></li>'+''.join(f'<li class="page-item{" active" if n==1 else ""}"><button class="page-link" type="button" data-demo-page="{n}" aria-label="Halaman {n}" {"aria-current=page" if n==1 else ""}>{n}</button></li>' for n in range(1,4))+f'<li class="page-item"><button class="page-link" type="button" data-page-step="1" aria-label="Berikutnya">{"→" if arrows else "Next"}</button></li></ul></nav><p class="small text-muted mb-0" data-page-result aria-live="polite">Halaman 1 · Menampilkan item 1–5 dari 15.</p></div>'


def pagination_page(icon):
    return demo('Default & state','Halaman aktif dan tombol sebelumnya/berikutnya diperbarui saat diklik.',pagination_markup('basicPages'))+demo('Icon navigation','Panah memiliki label untuk pembaca layar.',pagination_markup('iconPages',arrows=True))+demo('Sizing','Ukuran kecil dan besar memakai kelas Bootstrap.',pagination_markup('smallPages','pagination-sm')+'<hr>'+pagination_markup('largePages','pagination-lg',arrows=True))+demo('Alignment','Navigasi rata tengah dan rata kanan.',pagination_markup('centerPages',align='justify-content-center')+'<hr>'+pagination_markup('endPages',align='justify-content-end'))


def popover_page(icon):
    directions=row(''.join(button(label,attrs=f'data-bs-toggle="popover" data-bs-placement="{pos}" data-bs-title="Sedikit konteks" data-bs-content="Popover pada sisi {label.lower()}. Klik lagi untuk menutup."') for pos,label in [('top','Atas'),('right','Kanan'),('bottom','Bawah'),('left','Kiri')]))
    dismiss=button('Klik lalu klik di luar','warning','data-bs-toggle="popover" data-bs-trigger="focus" data-bs-title="Dismiss on focus out" data-bs-content="Popover ini menutup ketika fokus berpindah."')
    disabled='<span class="d-inline-block" tabindex="0" role="button" aria-label="Info tombol disabled" data-bs-toggle="popover" data-bs-trigger="hover focus" data-bs-content="Fitur ini belum tersedia untuk workspace kamu."><button type="button" class="btn btn-primary" style="pointer-events:none" disabled>Tombol disabled</button></span>'
    link='<p class="mb-0">Butuh penjelasan tentang <button type="button" class="inline-info" data-bs-toggle="popover" data-bs-trigger="focus" data-bs-title="Workspace" data-bs-content="Satu tempat untuk proyek, tugas, dan anggota tim.">workspace</button>? Klik istilah tersebut untuk melihat konteks.</p>'
    return demo('Directions','Klik tombol. Posisi menyesuaikan ruang layar.',directions)+demo('Dismissible','Gunakan trigger focus untuk menutup ketika keluar dari tombol.',dismiss)+demo('Disabled trigger','Wrapper yang bisa menerima fokus membungkus tombol disabled.',disabled)+demo('Di dalam teks','Popover untuk penjelasan istilah tanpa meninggalkan halaman.',link)


def progress_bar(value, color='purple', label=False, height=12, extra=''):
    return f'<div class="progress mb-3" role="progressbar" aria-label="Progres {value} persen" aria-valuenow="{value}" aria-valuemin="0" aria-valuemax="100" style="height:{height}px"><div class="progress-bar bg-{color} {extra}" style="width:{value}%">{str(value)+"%" if label else ""}</div></div>'


def progress_page(icon):
    basic=''.join(progress_bar(v) for v in [0,25,50,75,100])
    labels=''.join(progress_bar(v,c,True,26) for v,c in [(25,'purple'),(50,'green'),(75,'yellow'),(100,'blue')])
    heights=''.join(f'<p class="demo-label">{h}px</p>'+progress_bar(65,height=h) for h in [6,12,24,36])
    colors=''.join(progress_bar(v,c) for v,c in [(20,'purple'),(40,'green'),(60,'yellow'),(80,'orange'),(100,'blue')])
    striped=progress_bar(65,'purple',True,26,'progress-bar-striped')+progress_bar(80,'green',True,26,'progress-bar-striped progress-bar-animated')+button('Jeda animasi','outline-primary','id="progressAnimation" aria-pressed="false"')
    stacked='<div class="progress-stacked" style="height:26px">'+''.join(f'<div class="progress" role="progressbar" aria-label="{t}" aria-valuenow="{n}" aria-valuemin="0" aria-valuemax="100" style="width:{n}%"><div class="progress-bar bg-{c}">{n}%</div></div>' for n,c,t in [(35,'purple','Design'),(25,'green','Development'),(20,'yellow','Review')])+'</div><p class="small mt-3 mb-0">Design 35% · Development 25% · Review 20%</p>'
    return demo('Simple','Lebar progres dari 0 sampai 100 persen.',basic)+demo('Label','Label dengan tinggi yang cukup agar mudah dibaca.',labels)+demo('Height','Tinggi disesuaikan dengan kebutuhan layout.',heights)+demo('Background','Warna pastel untuk beberapa metrik.',colors)+demo('Striped & animated','Animasi bisa dijeda dan mengikuti preferensi reduced motion.',striped)+demo('Multiple bars','Gabungkan beberapa fase dalam satu track.',stacked)


def tooltip_page(icon):
    directions=row(''.join(button(label,attrs=f'data-bs-toggle="tooltip" data-bs-placement="{pos}" data-bs-title="Tooltip di {label.lower()}"') for pos,label in [('top','Atas'),('right','Kanan'),('bottom','Bawah'),('left','Kiri')]))
    disabled='<span class="d-inline-block" tabindex="0" role="button" aria-label="Bantuan untuk tombol disabled" data-bs-toggle="tooltip" data-bs-title="Tombol ini belum tersedia"><button type="button" class="btn btn-primary" style="pointer-events:none" disabled>Disabled</button></span>'
    link='<a href="docs.html" data-bs-toggle="tooltip" data-bs-title="Buka panduan penggunaan BRUTAL.">Baca dokumentasi ↗</a>'
    paragraph='<p>Bangun <button type="button" class="inline-info" data-bs-toggle="tooltip" data-bs-title="Kumpulan komponen visual yang konsisten">design system</button> yang mudah dipakai ulang. Gunakan <button type="button" class="inline-info" data-bs-toggle="tooltip" data-bs-title="Nilai warna, border, dan shadow dalam CSS variables">design token</button> untuk menjaga identitas produk.</p>'
    return demo('Directions','Arahkan pointer atau fokuskan tombol dengan keyboard.',directions)+demo('Disabled tooltip','Wrapper memberikan akses hover dan keyboard.',disabled)+demo('Link','Bantuan singkat untuk tujuan tautan.',link)+demo('Paragraph','Informasi tambahan pada istilah di dalam paragraf.',paragraph)


FLAGS = [('id','Indonesia'),('pl','Polandia'),('nl','Belanda'),('fr','Prancis'),('de','Jerman'),('it','Italia'),('jp','Jepang'),('ua','Ukraina'),('at','Austria'),('be','Belgia'),('ie','Irlandia'),('bd','Bangladesh')]


def write_flags(root):
    """Original SVG geometric flags, intrinsic national proportions preserved."""
    folder=root/'assets/img/flags'; folder.mkdir(parents=True,exist_ok=True)
    specs={'id':(3,2,['#e70011','#fff'],False),'pl':(8,5,['#fff','#dc143c'],False),'nl':(3,2,['#ae1c28','#fff','#21468b'],False),'fr':(3,2,['#002654','#fff','#ed2939'],True),'de':(5,3,['#000','#d00','#ffce00'],False),'it':(3,2,['#009246','#fff','#ce2b37'],True),'ua':(3,2,['#0057b7','#ffdd00'],False),'at':(3,2,['#ed2939','#fff','#ed2939'],False),'be':(15,13,['#000','#fdda24','#ef3340'],True),'ie':(2,1,['#169b62','#fff','#ff883e'],True)}
    for code,_ in FLAGS:
        if code in specs:
            w,h,colors,vertical=specs[code];w*=100;h*=100
            shapes=''.join(f'<rect x="{i*w/len(colors) if vertical else 0}" y="{0 if vertical else i*h/len(colors)}" width="{w/len(colors) if vertical else w}" height="{h if vertical else h/len(colors)}" fill="{c}"/>' for i,c in enumerate(colors))
        elif code=='jp':
            w,h=300,200;shapes='<path fill="#fff" d="M0 0h300v200H0z"/><circle cx="150" cy="100" r="60" fill="#bc002d"/>'
        else:
            w,h=500,300;shapes='<path fill="#006a4e" d="M0 0h500v300H0z"/><circle cx="225" cy="150" r="100" fill="#f42a41"/>'
        (folder/f'{code}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{shapes}</svg>',encoding='utf-8')


def flags_page(icon):
    gallery='<label class="form-label" for="flagSearch">Cari negara atau kode</label><input class="form-control mb-4" id="flagSearch" type="search" placeholder="Contoh: Indonesia atau id"><div class="flag-grid">'+''.join(f'<div class="flag-tile" data-flag-name="{name.lower()} {code}"><img src="assets/img/flags/{code}.svg" class="flag-img" alt="Bendera {name}" width="60" height="40"><strong>{name}</strong><code>{code.upper()}</code></div>' for code,name in FLAGS)+'</div><p id="flagCount" class="small text-muted mt-3 mb-0" aria-live="polite">12 bendera</p>'
    sizes=row(''.join(f'<img src="assets/img/flags/id.svg" class="flag-img" style="width:{size}px;height:auto" alt="Bendera Indonesia ukuran {size} piksel" width="{size}" height="{int(size*2/3)}">' for size in [24,40,64,96]))
    context='<div class="list-group">'+''.join(f'<div class="list-group-item d-flex align-items-center gap-3"><img class="flag-img flag-inline" src="assets/img/flags/{code}.svg" alt=""><span>{name}</span><span class="badge text-bg-light ms-auto">{code.upper()}</span></div>' for code,name in FLAGS[:3])+'</div>'
    return demo('Flag gallery','12 contoh SVG lokal dengan proporsi asli, tanpa font emoji atau CDN.',gallery,True)+demo('Sizing','SVG tetap tajam pada berbagai ukuran.',sizes)+demo('Dalam daftar','Nama negara memberi konteks; gambar dekoratif memakai alt kosong.',context)


def typography_page(icon):
    headings=''.join(f'<div class="h{i} mb-3">Heading {i}</div>' for i in range(1,7))
    display=''.join(f'<div class="display-{i} fw-bold">Display {i}</div>' for i in [4,5,6])
    inline='<p><mark>Sorot ide penting.</mark></p><p><del>Konsep lama.</del> <ins>Konsep yang diperbarui.</ins></p><p><strong>Teks tebal</strong> dan <em>penekanan halus</em>.</p><p><small>Catatan pendamping berukuran kecil.</small></p><p><abbr title="User Interface">UI</abbr> dan <abbr title="User Experience">UX</abbr> bekerja bersama.</p><p class="mb-0">Gunakan <code>.fw-bold</code> atau tekan <kbd>Ctrl</kbd> + <kbd>K</kbd>.</p>'
    colors=''.join(f'<p class="text-{v}">Teks {v} untuk konteks yang berbeda.</p>' for v in ['primary','secondary','success','danger','warning','info','body','muted'])
    quote='<figure class="mb-0"><blockquote class="blockquote"><p>Ide besar dimulai dari keberanian untuk mencoba.</p></blockquote><figcaption class="blockquote-footer mt-3">Tim studio, dalam <cite title="Creative notes">Creative notes</cite></figcaption></figure>'
    lists='<div class="row g-3"><div class="col-sm-6"><h3>Unordered</h3><ul><li>Riset</li><li>Desain<ul><li>Wireframe</li><li>Prototype</li></ul></li><li>Evaluasi</li></ul></div><div class="col-sm-6"><h3>Ordered</h3><ol><li>Pahami kebutuhan</li><li>Bangun solusi</li><li>Uji dan iterasi</li></ol></div></div><dl class="row small mb-0"><dt class="col-sm-4">Design token</dt><dd class="col-sm-8">Nilai dasar yang dipakai ulang di seluruh antarmuka.</dd><dt class="col-sm-4">Component</dt><dd class="col-sm-8">Bagian UI yang dapat dikomposisikan.</dd></dl>'
    paragraph='<p class="lead">Sedikit ide. Dampak besar.</p><p>Tipografi membantu pengguna menemukan informasi yang penting. Gunakan hierarki yang jelas, ukuran yang nyaman, dan panjang baris yang wajar.</p><p class="text-start">Rata kiri.</p><p class="text-center">Rata tengah.</p><p class="text-end">Rata kanan.</p><p class="text-uppercase small fw-bold mb-0">Ruang untuk ide berikutnya.</p>'
    return demo('Headings','Skala h1–h6 ditampilkan memakai kelas heading.',headings)+demo('Display','Judul besar untuk pesan yang menonjol.',display)+demo('Inline text & abbreviations','Markup semantik untuk penekanan dan istilah.',inline)+demo('Text colors','Warna kontekstual Bootstrap.',colors)+demo('Blockquote','Kutipan dengan atribusi sumber.',quote)+demo('Lists & descriptions','Daftar unordered, ordered, nested, dan definisi.',lists)+demo('Paragraph & alignment','Lead paragraph, body text, dan alignment.',paragraph,True)


BUILDERS = [alert_page,badge_page,breadcrumb_page,buttons_page,collapse_page,dropdown_page,checks_page,list_page,media_page,navbar_page,pagination_page,popover_page,progress_page,tooltip_page,flags_page,typography_page]


def build_pages(heading, icon):
    pages={}
    for (key,title,description),builder in zip(CATALOG,BUILDERS):
        pages[key]=heading(escape(title),description,'<a class="btn" href="components.html">'+icon('layers')+' Semua komponen</a>')+'<div class="demo-grid component-demos">'+builder(icon)+'</div>'
    return pages
