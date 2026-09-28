#!/usr/bin/env python3
"""Generate readable, standalone HTML pages."""
from pathlib import Path
from html import escape
import json
from component_pages import CATALOG, overview, build_pages, write_flags
from workspace_pages import WORKSPACE_PAGES, build_workspace_pages, write_workspace_assets
from format_html import format_html, verify_semantic

ROOT = Path(__file__).resolve().parent.parent
ICONS = {
    'grid': '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
    'chart': '<path d="M3 3v18h18M7 15l4-5 4 3 5-8"/>',
    'folder': '<path d="M3 7V4h6l3 3h9v13H3z"/>',
    'calendar': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 3v4m10-4v4M3 11h18m-13 4h2m4 0h2m-8 3h2"/>',
    'layers': '<path d="m12 3 10 5-10 5L2 8zm-10 9 10 5 10-5M2 16l10 5 10-5"/>',
    'form': '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8m-8 4h8m-8 4h4"/>',
    'table': '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/>',
    'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21v-2a8 8 0 0 1 16 0v2"/>',
    'users': '<circle cx="9" cy="8" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3m0-16a3 3 0 0 1 0 6m3 4a5 5 0 0 1 3 4v2"/>',
    'lock': '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V6a4 4 0 0 1 8 0v4m-4 5v2"/>',
    'file': '<path d="M5 3h9l5 5v13H5zM14 3v6h5M8 13h8m-8 4h6"/>',
    'book': '<path d="M12 5C9 3 5 3 2 4v16c3-1 7-1 10 1 3-2 7-2 10-1V4c-3-1-7-1-10 1zm0 0v16"/>',
    'settings': '<path d="m10 3-1 3-3 1-3 3 2 3-1 3 3 3 3-1 3 2 3-1 1-3 3-1 1-3-2-3 1-3-3-3-3 1z"/><circle cx="12" cy="12" r="3"/>',
    'search': '<circle cx="10" cy="10" r="6"/><path d="m15 15 6 6"/>',
    'bell': '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 8-3 9h18c0-1-3-2-3-9M9 21h6"/>',
    'plus': '<path d="M12 5v14M5 12h14"/>',
    'arrow': '<path d="M4 12h16m-6-6 6 6-6 6"/>',
    'up': '<path d="m5 15 7-7 7 7M12 8v13"/>',
    'download': '<path d="M12 3v12m-5-5 5 5 5-5M4 15v6h16v-6"/>',
    'wallet': '<path d="M3 7V4h15v3M3 7h18v14H3zm12 5h6v5h-6z"/>',
    'cart': '<path d="M2 3h3l3 12h11l3-9H6M9 19h1m7 0h1"/><circle cx="10" cy="20" r="1"/><circle cx="18" cy="20" r="1"/>',
    'trend': '<path d="m3 17 6-6 4 4 8-10m-6 0h6v6"/>',
    'more': '<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
    'check': '<path d="m4 12 5 5L20 6"/>',
    'menu': '<path d="M3 6h18M3 12h18M3 18h18"/>',
    'logout': '<path d="M9 3H3v18h6m5-15 6 6-6 6m-7-6h13"/>',
    'bolt': '<path d="m13 2-9 12h7l-1 8 10-13h-8z"/>',
    'code': '<path d="m7 6-6 6 6 6m10-12 6 6-6 6M14 3l-4 18"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
    'heart': '<path d="M12 21 3 12C-2 4 8-2 12 6c4-8 14-2 9 6z"/>',
    'close': '<path d="m6 6 12 12M6 18 18 6"/>',
    'eye': '<path d="M2 12c5-9 15-9 20 0-5 9-15 9-20 0z"/><circle cx="12" cy="12" r="3"/>',
}
def icon(name):
    return f'<svg class="icon" aria-hidden="true" viewBox="0 0 24 24">{ICONS.get(name, ICONS["grid"])}</svg>'

NAV = json.loads((ROOT/'assets/js/sidebar-config.js').read_text().split('window.BRUTAL_SIDEBAR =', 1)[1].strip().removesuffix(';'))
def nav_pages(items):
    for item in items:
        if 'children' in item:
            yield from nav_pages(item['children'])
        else:
            yield item
TITLES = {item['page']:item['label'] for section in NAV for item in nav_pages(section['items'])}
TITLES.update({'components':'Komponen UI', 'errors-404':'Halaman tidak ditemukan'})
TITLES.update({'widget-chart':'Widget Grafik','widget-data':'Widget Data'})

def art():
    return '<div class="hero-art" aria-hidden="true"><div class="hero-grid"></div><div class="art-window"><div class="art-title"><i></i><i></i><i></i></div><div class="art-bars"><i></i><i></i><i></i><i></i></div></div><div class="art-star">✦</div><div class="art-sticker">Make it bold. ↗</div></div>'

def heading(title,sub,actions=''):
    return f'<div class="page-heading"><div><h1>{title}</h1><p>{sub}</p></div><div class="page-heading-actions">{actions}</div></div>'

def card(title,body,cls=''):
    return f'<section class="card {cls}"><div class="card-body"><h2>{title}</h2>{body}</div></section>'

def common_ui():
    return f'''<div class="modal fade" id="searchModal" tabindex="-1" aria-labelledby="searchTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="searchTitle">Cari di BRUTAL.</h2><button class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><div class="modal-body"><label class="visually-hidden" for="globalSearch">Cari halaman</label><input id="globalSearch" type="search" class="form-control" placeholder="Cari komponen, form, halaman…" autocomplete="off"><div id="searchResults" class="search-results mt-3"></div></div></div></div></div>
    <div class="modal fade" id="projectModal" tabindex="-1" aria-labelledby="projectTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="projectTitle">Ide besar dimulai di sini.</h2><button class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><form id="projectForm"><div class="modal-body"><p class="text-muted small">Tambahkan proyek ke workspace demo kamu.</p><label class="form-label" for="projectName">Nama proyek</label><input class="form-control mb-3" id="projectName" name="name" placeholder="Contoh: Website studio" required maxlength="70"><label class="form-label" for="projectCategory">Kategori</label><select id="projectCategory" name="category" class="form-select mb-3"><option>Website</option><option>Branding</option><option>Mobile app</option><option>Marketing</option></select><label class="form-label" for="projectDue">Tenggat</label><input id="projectDue" name="due" class="form-control" type="date" required></div><div class="modal-footer"><button type="button" class="btn" data-bs-dismiss="modal">Batal</button><button type="submit" class="btn btn-primary">{icon('plus')} Buat proyek</button></div></form></div></div></div>
    <div class="toast-container position-fixed bottom-0 end-0 p-3"><div id="appToast" class="toast" role="status" aria-live="polite" aria-atomic="true"><div class="d-flex"><div id="toastMessage" class="toast-body"></div><button class="btn-close me-3 m-auto" data-bs-dismiss="toast" aria-label="Tutup"></button></div></div></div>'''

def shell(key, content):
    component_crumb = '<li class="breadcrumb-item"><a href="components.html">Komponen UI</a></li>' if key in {item[0] for item in CATALOG} else ''
    for section in NAV:
        for item in section['items']:
            if 'children' in item and key in WORKSPACE_PAGES and any(child['page'] == key for child in item['children']):
                component_crumb = f'<li class="breadcrumb-item">{escape(item["label"])}</li>'
    return f'''<a class="skip-link" href="#main">Lewati ke konten</a><div id="sidebar-root"></div>
    <div class="app-wrap"><header class="topbar"><div class="d-flex align-items-center gap-3"><button class="btn icon-btn mobile-toggle" id="sidebarToggle" aria-label="Buka navigasi" aria-controls="sidebar" aria-expanded="false">{icon('menu')}</button><nav aria-label="Breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Workspace</a></li>{component_crumb}<li class="breadcrumb-item active" aria-current="page">{escape(TITLES[key])}</li></ol></nav></div><div class="topbar-actions"><button class="search-trigger" data-bs-toggle="modal" data-bs-target="#searchModal" aria-label="Cari halaman">{icon('search')}<span>Cari sesuatu…</span><kbd>Ctrl K</kbd></button><span class="top-divider"></span><div class="dropdown"><button class="btn icon-btn position-relative" data-bs-toggle="dropdown" aria-expanded="false" aria-label="Notifikasi">{icon('bell')}<span class="notification-dot"></span></button><div class="dropdown-menu dropdown-menu-end" style="width:275px"><h2 class="fs-6 px-2 pt-2">Kabar workspace</h2><p class="small px-2 mb-2">Selamat datang! Jelajahi komponen dan mulai proyek pertamamu.</p><a class="dropdown-item" href="docs.html">Baca panduan {icon('arrow')}</a></div></div><div class="dropdown"><button class="avatar bg-purple" data-bs-toggle="dropdown" aria-label="Menu akun" aria-expanded="false">AD</button><div class="dropdown-menu dropdown-menu-end"><a class="dropdown-item" href="profile.html">Profil & pengaturan</a><a class="dropdown-item" href="auth-login.html">Lihat halaman login</a></div></div></div></header><main class="main-content" id="main" tabindex="-1">{content}</main><footer class="app-footer"><span>© 2026 BRUTAL. <span class="ms-1">Built different. Built with Bootstrap.</span></span><div><span class="me-3">Demo workspace</span><a href="docs.html">Dokumentasi ↗</a></div></footer></div>{common_ui()}'''

def page(key,content,standalone=False):
    body = ('<a class="skip-link" href="#main">Lewati ke konten</a><div id="sidebar-root"></div><button type="button" id="sidebarToggle" class="btn icon-btn standalone-toggle" aria-label="Buka navigasi" aria-controls="sidebar" aria-expanded="false">'+icon('menu')+'</button>'+content+common_ui()) if standalone else shell(key,content)
    workspace_style = '<link rel="stylesheet" href="assets/css/workspace.css">' if key in WORKSPACE_PAGES else ''
    workspace_script = '<script src="assets/js/workspace.js"></script>' if key in WORKSPACE_PAGES else ''
    return f'''<!doctype html>
<html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="BRUTAL. — Template admin Neubrutalism berbasis Bootstrap 5.3.8. Komponen, form, tabel, dan halaman siap dikembangkan."><title>{escape(TITLES[key])} — BRUTAL.</title><link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="bootstrap-5.3.8/dist/css/bootstrap.min.css"><link rel="stylesheet" href="assets/css/theme.css">{workspace_style}</head><body data-page="{key}"{' class="standalone-page"' if standalone else ''}>{body}<script src="bootstrap-5.3.8/dist/js/bootstrap.bundle.min.js"></script><script src="assets/js/sidebar-config.js"></script><script src="assets/js/sidebar-icons.js"></script><script src="assets/js/sidebar.js"></script><script src="assets/js/app.js"></script>{workspace_script}</body></html>'''

def new_project_button():
    return f'<button class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#projectModal">{icon("plus")} Proyek baru</button>'

def stats():
    data = [('Total pendapatan','Rp48,5 jt','+18,6%','bulan ini','wallet','purple'),('Proyek aktif','24','+4 proyek','bulan ini','folder','green'),('Total pelanggan','1.284','+12,8%','bulan ini','users','orange'),('Tingkat konversi','4,82%','+2,1%','bulan ini','trend','yellow')]
    return '<div class="stats-grid">'+''.join(f'<section class="card stat-card bg-{color}"><div class="stat-top"><span class="stat-label">{label}</span><span class="stat-icon">{icon(ico)}</span></div><div class="stat-value">{value}</div><div class="stat-meta"><strong>↗ {change}</strong><span>{time}</span></div></section>' for label,value,change,time,ico,color in data)+'</div>'

def revenue_chart():
    grid = ''.join(f'<line x1="40" y1="{y}" x2="560" y2="{y}" class="chart-grid"/><text x="0" y="{y+4}" class="chart-label">{n} jt</text>' for y,n in [(30,20),(78,15),(126,10),(174,5)])
    labels = ''.join(f'<text x="{x}" y="227" text-anchor="middle" class="chart-label">{m}</text>' for x,m in zip([40,144,248,352,456,560],['Apr','Mei','Jun','Jul','Agu','Sep']))
    return f'<svg class="revenue-chart" viewBox="0 0 580 240" role="img" aria-labelledby="revenueChartTitle"><title id="revenueChartTitle">Pendapatan contoh April–September: 8, 11, 9, 16, 14, 20 juta rupiah. Target: 5, 8, 7, 11, 9, 14 juta.</title>{grid}<path id="chartArea" d="M40 145 144 116 248 134 352 68 456 87 560 30V205H40Z" fill="#c4a8f555"/><path id="chartTarget" d="M40 174 144 145 248 155 352 116 456 135 560 87" fill="none" stroke="#9ebba3" stroke-width="2.5" stroke-dasharray="5 5"/><path id="chartLine" d="M40 145 144 116 248 134 352 68 456 87 560 30" fill="none" stroke="#232420" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><g id="chartDots">'+''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="#c4a8f5" stroke="#232420" stroke-width="2"/>' for x,y in [(40,145),(144,116),(248,134),(352,68),(456,87),(560,30)])+f'</g>{labels}</svg>'

def chart_panel():
    return f'<section class="card"><div class="card-body"><div class="panel-heading"><div><h2>Arus pendapatan</h2><p>Sedikit progres, setiap hari.</p></div><select class="form-select form-select-sm w-auto" id="chartPeriod" aria-label="Periode grafik"><option value="current">6 bulan terakhir</option><option value="previous">6 bulan sebelumnya</option></select></div><div class="d-flex justify-content-between align-items-center flex-wrap gap-2"><div><span class="chart-summary" id="chartTotal">Rp78.000.000</span> <span class="badge bg-green" id="chartGrowth">↗ 23,8%</span></div><div class="chart-legend"><span><i class="legend-dot bg-purple"></i>Pendapatan</span><span><i class="legend-dot bg-green"></i>Target</span></div></div>{revenue_chart()}</div></section>'

def source_panel():
    return '<section class="card"><div class="card-body"><div class="panel-heading"><div><h2>Dari mana mereka datang?</h2><p>Sumber kunjungan bulan ini</p></div></div><div class="donut" role="img" aria-label="Kunjungan: organik 48 persen, langsung 32 persen, referral 20 persen"><div class="donut-hole"><strong>8.542</strong><small>Total pengunjung</small></div></div>'+''.join(f'<div class="source-row"><i class="legend-dot bg-{c}"></i>{s}<strong>{n}%</strong></div>' for s,n,c in [('Pencarian organik',48,'purple'),('Kunjungan langsung',32,'green'),('Referral & sosial',20,'yellow')])+'</div></section>'

def projects_table(full=False):
    return f'''<section class="card"><div class="card-body pb-0"><div class="panel-heading"><div><h2>{'Semua proyek' if full else 'Proyek terbaru'}</h2><p>Ide yang sedang jadi kenyataan.</p></div>{'<button class="btn btn-sm" id="exportTable">'+icon('download')+' CSV</button>' if full else '<a class="small fw-bold text-dark text-decoration-none" href="tables.html">Lihat semua ↗</a>'}</div>{'<div class="d-flex flex-wrap gap-3 mb-3"><input class="form-control flex-grow-1" style="min-width:160px;flex-basis:200px" type="search" id="tableSearch" placeholder="Cari nama atau kategori…" aria-label="Cari proyek"><select id="tableStatus" class="form-select w-auto" aria-label="Filter status"><option value="">Semua status</option><option>Berjalan</option><option>Selesai</option><option>Review</option><option>Rencana</option></select><select id="tableSort" class="form-select w-auto" aria-label="Urutkan proyek"><option value="newest">Terbaru</option><option value="name">Nama A–Z</option><option value="due">Tenggat terdekat</option></select></div>' if full else ''}</div><div class="table-responsive"><table class="table table-hover"><caption class="visually-hidden">Daftar proyek workspace demo</caption><thead><tr><th scope="col">Nama proyek</th><th scope="col">Tim</th><th scope="col">Status</th><th scope="col">Tenggat</th></tr></thead><tbody id="projectRows" data-limit="{'5' if full else '4'}"></tbody></table></div>{'<div class="card-footer d-flex justify-content-between align-items-center"><small id="tableCount" aria-live="polite"></small><nav aria-label="Halaman tabel"><ul class="pagination mb-0" id="tablePagination"></ul></nav></div>' if full else ''}</section>'''

def dashboard():
    intro = heading('Sedikit ide. Dampak besar. ✳','Selamat datang kembali, Alex. Yuk, buat sesuatu yang hebat hari ini.',f'<button class="btn" id="exportDashboard">{icon("download")} Ekspor</button>{new_project_button()}')
    hero = f'<section class="card hero"><div class="hero-copy"><span class="eyebrow">YOUR WORKSPACE, BUT BOLDER.</span><h2>Kerja rapi.<br>Hasil luar biasa.</h2><p>Semua proyek, angka, dan ide besarmu.<br>Satu tempat untuk terus bergerak maju.</p><a class="btn btn-dark" href="projects.html">Jelajahi workspace {icon("arrow")}</a></div>{art()}</section>'
    tasks = '<section class="card"><div class="card-body"><div class="panel-heading"><div><h2>Fokus hari ini</h2><p>Satu per satu, beres.</p></div><span class="badge bg-yellow" id="taskCount">0/0</span></div><div id="taskList"></div><form id="taskForm" class="task-form"><input id="taskInput" class="form-control" placeholder="Tambah hal yang ingin dibereskan…" aria-label="Tugas baru" required maxlength="90"><button class="btn btn-primary" aria-label="Tambah tugas">'+icon('plus')+'</button></form></div></section>'
    return intro+hero+stats()+f'<div class="dashboard-grid">{chart_panel()}{source_panel()}</div><div class="dashboard-grid">{projects_table()}{tasks}</div>'

def components():
    return overview(heading, icon)


def forms():
    form = '''<form id="demoForm" class="needs-validation" novalidate><div class="row g-3"><div class="col-md-6"><label class="form-label" for="firstName">Nama depan</label><input id="firstName" name="firstName" class="form-control" placeholder="Alex" required><div class="invalid-feedback">Isi nama depan kamu.</div></div><div class="col-md-6"><label class="form-label" for="lastName">Nama belakang</label><input id="lastName" class="form-control" name="lastName" placeholder="Darma" required><div class="invalid-feedback">Isi nama belakang kamu.</div></div><div class="col-12"><label class="form-label" for="demoEmail">Alamat email</label><input id="demoEmail" type="email" name="email" class="form-control" placeholder="alex@studio.id" required><div class="invalid-feedback">Gunakan alamat email yang valid.</div></div><div class="col-md-6"><label class="form-label" for="role">Peran</label><select class="form-select" id="role" required><option value="">Pilih peran…</option><option>Designer</option><option>Developer</option><option>Project manager</option></select><div class="invalid-feedback">Pilih salah satu peran.</div></div><div class="col-md-6"><label class="form-label" for="startDate">Mulai bergabung</label><input class="form-control" type="date" id="startDate" required><div class="invalid-feedback">Tentukan tanggal mulai.</div></div><div class="col-12"><label class="form-label" for="bio">Sedikit tentang kamu</label><textarea class="form-control" id="bio" rows="3" placeholder="Ide, keahlian, atau hal yang kamu sukai…" maxlength="300"></textarea></div><div class="col-12"><div class="form-check"><input class="form-check-input" type="checkbox" id="consent" required><label class="form-check-label small" for="consent">Saya paham ini adalah form demonstrasi.</label><div class="invalid-feedback">Centang persetujuan untuk melanjutkan.</div></div></div><div class="col-12 d-flex gap-3"><button class="btn btn-primary" type="submit">Simpan data demo</button><button class="btn" type="reset">Reset</button></div></div><p id="formResult" class="small mt-3 mb-0" role="status"></p></form>'''
    inputs = '''<label for="website" class="form-label">Input group</label><div class="input-group mb-3"><span class="input-group-text">https://</span><input id="website" class="form-control" placeholder="studio.id"></div><div class="form-floating mb-3"><input type="email" class="form-control" id="floatingEmail" placeholder="Email"><label for="floatingEmail">Floating label</label></div><label for="disabledInput" class="form-label">Disabled</label><input id="disabledInput" class="form-control" placeholder="Tidak dapat diedit" disabled><label for="readonlyInput" class="form-label mt-3">Read only</label><input id="readonlyInput" class="form-control" value="BRUTAL-2026" readonly>'''
    choices = '''<div class="form-check mb-2"><input class="form-check-input" type="checkbox" id="checkDemo" checked><label class="form-check-label" for="checkDemo">Terima pembaruan produk</label></div><div class="form-check form-switch mb-4"><input class="form-check-input" type="checkbox" role="switch" id="switchDemo" checked><label class="form-check-label" for="switchDemo">Notifikasi desktop</label></div><fieldset><legend class="form-label">Prioritas proyek</legend><div class="demo-row"><div class="form-check"><input class="form-check-input" type="radio" id="normal" name="priority" checked><label class="form-check-label" for="normal">Normal</label></div><div class="form-check"><input class="form-check-input" type="radio" id="high" name="priority"><label class="form-check-label" for="high">Tinggi</label></div></div></fieldset><label for="budget" class="form-label">Budget demo: <output id="budgetOutput">50</output> juta</label><input class="form-range" type="range" min="10" max="100" value="50" id="budget"><label class="form-label mt-3" for="fileUpload">Lampiran (preview nama file)</label><input class="form-control" id="fileUpload" type="file" multiple><p class="small text-muted mt-2" id="fileNames" aria-live="polite">File tidak diunggah ke server.</p>'''
    return heading('Form yang enak diisi.','Input yang jelas, validasi yang membantu. Semua dengan Bootstrap native.')+f'<div class="row g-4"><div class="col-lg-7">{card("Kenalan dulu, yuk.",form)}</div><div class="col-lg-5 d-grid gap-4">{card("Input variations",inputs)}{card("Pilihan & kontrol",choices)}</div></div>'

def projects():
    return heading('Dari ide ke selesai.','Pindahkan status pekerjaan dan jaga semuanya tetap bergerak.',new_project_button())+'<div class="alert alert-info small">'+icon('folder')+' Workspace demo disimpan di browser ini. Ubah status lewat pilihan di setiap kartu.</div><div class="kanban-board" id="kanbanBoard"></div>'

def calendar():
    return heading('Beri ruang untuk rencana.','Jadwal yang jelas untuk hari yang lebih tenang.','<button class="btn btn-dark" data-bs-toggle="modal" data-bs-target="#eventModal">'+icon('plus')+' Agenda baru</button>')+'''<section class="card"><div class="card-body"><div class="d-flex justify-content-between align-items-center gap-2"><h2 class="mb-0" id="calendarTitle"></h2><div class="d-flex gap-2"><button class="btn btn-sm" id="prevMonth" aria-label="Bulan sebelumnya">←</button><button class="btn btn-sm" id="todayMonth">Hari ini</button><button class="btn btn-sm" id="nextMonth" aria-label="Bulan berikutnya">→</button></div></div></div><div class="calendar-grid" id="calendarGrid"></div></section><div class="d-flex gap-4 mt-4 small"><span><i class="legend-dot bg-purple"></i>Agenda workspace</span><span class="text-muted">Klik agenda untuk melihat detail.</span></div><div class="modal fade" id="eventModal" tabindex="-1" aria-labelledby="eventTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="eventTitle">Rencanakan sesuatu.</h2><button class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><form id="eventForm"><div class="modal-body"><label for="eventName" class="form-label">Nama agenda</label><input id="eventName" name="name" class="form-control mb-3" maxlength="60" required><label for="eventDate" class="form-label">Tanggal</label><input type="date" id="eventDate" name="date" class="form-control mb-3" required><label for="eventTime" class="form-label">Waktu</label><input type="time" id="eventTime" name="time" class="form-control" required value="09:00"></div><div class="modal-footer"><button class="btn btn-primary">Simpan agenda</button></div></form></div></div></div>'''

def profile():
    return heading('Ruangmu, caramu.','Buat workspace terasa sedikit lebih personal.')+'''<div class="row g-4"><div class="col-lg-4"><section class="card"><div class="profile-cover"></div><div class="card-body"><span class="avatar profile-avatar bg-yellow">AD</span><h2 class="mt-3" id="profileDisplayName">Alex Darma</h2><p class="text-muted" id="profileDisplayRole">Product designer & creative thinker</p><span class="badge bg-green">Available for big ideas</span><hr><p class="small">Membangun produk digital dengan sedikit keberanian dan banyak rasa ingin tahu.</p><div class="d-flex gap-4"><div><strong class="fs-4">24</strong><div class="small text-muted">Proyek demo</div></div><div><strong class="fs-4">12</strong><div class="small text-muted">Kolaborator</div></div></div></div></section></div><div class="col-lg-8"><section class="card mb-4"><div class="card-body"><h2 class="mb-4">Detail profil</h2><form id="profileForm"><label class="form-label" for="profileName">Nama lengkap</label><input id="profileName" name="name" class="form-control mb-3" value="Alex Darma" required maxlength="70"><label class="form-label" for="profileEmail">Email</label><input id="profileEmail" name="email" type="email" class="form-control mb-3" value="alex@example.com" required><label class="form-label" for="profileRole">Headline</label><input id="profileRole" name="role" class="form-control mb-4" value="Product designer & creative thinker" maxlength="120"><button class="btn btn-primary">Simpan profil</button><p class="small text-muted mt-3 mb-0">Data profil demo tersimpan di browser ini.</p></form></div></section><section class="card"><div class="card-body"><h2 class="mb-4">Preferensi tampilan</h2><div class="form-check form-switch"><input class="form-check-input" type="checkbox" role="switch" id="compactMode"><label class="form-check-label" for="compactMode">Tampilan lebih ringkas</label></div><hr><h3>Mulai dari awal</h3><p class="text-muted small">Hapus proyek, tugas, agenda, chat, email, profil, dan preferensi demo BRUTAL. di browser ini.</p><button class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#resetModal">Reset data demo</button></div></section></div></div><div class="modal fade" id="resetModal" tabindex="-1" aria-labelledby="resetTitle" aria-hidden="true"><div class="modal-dialog modal-dialog-centered"><div class="modal-content"><div class="modal-header"><h2 class="modal-title" id="resetTitle">Reset workspace demo?</h2><button class="btn-close" data-bs-dismiss="modal" aria-label="Tutup"></button></div><div class="modal-body">Data demo buatanmu di browser ini akan dihapus dan contoh awal dipulihkan.</div><div class="modal-footer"><button class="btn" data-bs-dismiss="modal">Batal</button><button class="btn btn-danger" id="resetData">Ya, reset demo</button></div></div></div></div>'''

def invoice():
    return heading('Detail yang bikin profesional.','Contoh invoice, siap dicetak atau disimpan sebagai PDF.','<button class="btn btn-primary" id="printInvoice">'+icon('download')+' Cetak invoice</button>')+'''<section class="card invoice-card"><div class="card-body p-md-5"><div class="d-flex justify-content-between flex-wrap gap-4 mb-5"><div><div class="brand mb-3"><span class="brand-mark">b.</span>BRUTAL. Studio</div><p class="small text-muted">Jl. Kreatif No. 24, Bandung<br>studio@example.com</p></div><div class="text-md-end"><span class="eyebrow">INVOICE DEMO</span><h2 class="fs-3 mt-2">INV-2026-024</h2><span class="badge bg-green">Lunas</span></div></div><div class="row mb-5"><div class="col-6"><div class="eyebrow text-muted mb-2">DITAGIHKAN KEPADA</div><strong>Acme Creative Co.</strong><p class="small text-muted">Tim Keuangan<br>finance@example.com</p></div><div class="col-6 text-end"><div class="small mb-2"><span class="text-muted">Tanggal terbit</span><br><strong>20 September 2026</strong></div><div class="small"><span class="text-muted">Jatuh tempo</span><br><strong>27 September 2026</strong></div></div></div><div class="table-responsive"><table class="table"><thead><tr><th scope="col">Deskripsi</th><th scope="col">Qty</th><th scope="col">Harga</th><th scope="col" class="text-end">Total</th></tr></thead><tbody><tr><td><strong>Brand identity</strong><div class="table-sub">Logo, color palette, brand guidelines</div></td><td>1</td><td>Rp8.000.000</td><td class="text-end">Rp8.000.000</td></tr><tr><td><strong>Website design</strong><div class="table-sub">5 halaman, responsive design</div></td><td>1</td><td>Rp12.000.000</td><td class="text-end">Rp12.000.000</td></tr><tr><td><strong>Social media kit</strong><div class="table-sub">Template konten siap pakai</div></td><td>4</td><td>Rp500.000</td><td class="text-end">Rp2.000.000</td></tr></tbody></table></div><div class="row mt-4"><div class="col-md-6"><div class="alert alert-info small">Terima kasih sudah mempercayakan ide besarmu kepada kami. Sampai di proyek berikutnya! ✳</div></div><div class="col-md-5 ms-auto"><div class="d-flex justify-content-between mb-3 small"><span>Subtotal</span><strong>Rp22.000.000</strong></div><div class="d-flex justify-content-between mb-3 small"><span>Diskon kolaborasi</span><strong>−Rp2.000.000</strong></div><div class="d-flex justify-content-between border-top border-2 pt-3 fw-bold fs-5"><span>Total</span><span>Rp20.000.000</span></div></div></div><p class="small text-muted mt-5 mb-0">Dokumen demonstrasi · Bukan tagihan aktual · Tidak memproses pembayaran.</p></div></section>'''

def pricing():
    plans = [('Starter','Untuk ide yang baru mulai.','0','', ['1 workspace','3 proyek aktif','Komponen dasar','Dukungan komunitas'],'Mulai sederhana'),('Studio','Untuk tim dengan ide besar.','149','purple',['5 workspace','Proyek tak terbatas','Semua komponen','Dukungan prioritas'],'Pilih Studio'),('Collective','Untuk kolaborasi tanpa batas.','399','', ['Workspace tak terbatas','Manajemen anggota','Laporan lanjutan','Dukungan khusus'],'Pilih Collective')]
    cards = ''
    for name,desc,price,bg,features,cta in plans:
        cards += f'<section class="card {"pricing-featured" if bg else ""}"><div class="card-body {"bg-purple" if bg else ""}"><div class="d-flex align-items-center justify-content-between"><h2 class="fs-4 mb-0">{name}</h2>{"<span class=\"badge bg-yellow\">FAVORIT</span>" if bg else ""}</div><p class="small mt-2 mb-0">{desc}</p><div class="price">Rp{price}<small>{" ribu / bulan" if price != "0" else " / selamanya"}</small></div><ul class="feature-list">'+''.join(f'<li>{icon("check")}{f}</li>' for f in features)+f'</ul><button class="btn {"btn-dark" if bg else "btn-primary"} w-100" data-toast="Paket {name} dipilih. Ini contoh UI; tidak ada transaksi.">{cta} {icon("arrow")}</button></div></section>'
    return heading('Ide besar. Pilihan sederhana.','Contoh halaman harga untuk produk digital atau layananmu.')+'<div class="text-center my-5"><span class="badge bg-yellow mb-3">BUILT FOR YOUR NEXT BIG THING</span><h2 class="display-6 fw-bold">Ada ruang untuk setiap ambisi.</h2><p class="text-muted">Mulai kecil. Berkembang dengan caramu.</p></div><div class="pricing-grid">'+cards+'</div><p class="text-center text-muted small mt-4">Paket dan harga ilustratif. Tombol mendemonstrasikan UI tanpa memproses pembayaran.</p>'

def auth(key):
    login = key == 'auth-login'
    register = key == 'auth-register'
    title,sub = ('Halo, kamu lagi.','Masuk dan lanjutkan ide besarmu.') if login else ('Ide besar dimulai di sini.','Buat ruang untuk semua kemungkinan.') if register else ('Lupa? Tidak apa-apa.','Masukkan email untuk mencoba alur reset password.')
    inputs = '<label class="form-label" for="authName">Nama lengkap</label><input class="form-control" id="authName" autocomplete="name" placeholder="Alex Darma" required maxlength="70">' if register else ''
    inputs += '<label class="form-label" for="authEmail">Email</label><input class="form-control" type="email" id="authEmail" autocomplete="email" placeholder="kamu@studio.id" required>'
    if login or register:
        inputs += f'<label class="form-label" for="authPassword">Password</label><div class="input-group"><input class="form-control" type="password" id="authPassword" autocomplete="{"new-password" if register else "current-password"}" placeholder="Minimal 8 karakter" minlength="8" required><button class="btn" type="button" id="togglePassword" aria-label="Tampilkan password" aria-pressed="false">{icon("eye")}</button></div>'
    if login:
        inputs += '<div class="text-end mt-3"><a class="small text-dark" href="auth-forgot-password.html">Lupa password?</a></div>'
    if register:
        inputs += '<div class="form-check mt-3"><input class="form-check-input" id="authConsent" type="checkbox" required><label class="form-check-label small" for="authConsent">Saya memahami ini hanya demo antarmuka.</label></div>'
    cta = 'Masuk ke workspace' if login else 'Buat akun demo' if register else 'Coba reset password'
    bottom = '<p class="small text-center mt-4">Baru di sini? <a href="auth-register.html" class="fw-bold text-dark">Buat akun</a></p>' if login else '<p class="small text-center mt-4"><a href="auth-login.html" class="text-dark">← Kembali ke login</a></p>'
    return f'<div class="auth-layout"><section class="auth-art"><a class="brand" href="index.html"><span class="brand-mark bg-yellow">b.</span>BRUTAL.</a><div><span class="eyebrow">YOUR NEXT BIG THING STARTS HERE.</span><div class="auth-display mt-3">Stay curious.<br>Build bold.</div>{art()}</div><p class="small mb-0">Sedikit keberanian. Banyak kemungkinan. © 2026 BRUTAL.</p></section><main class="auth-content" id="main"><div class="auth-form"><a class="text-dark small text-decoration-none" href="index.html">← Kembali ke dashboard</a><span class="badge bg-yellow d-table mt-5 mb-3">LET’S MAKE THINGS HAPPEN</span><h1>{title}</h1><p class="text-muted mb-4">{sub}</p><form id="authForm">{inputs}<button class="btn btn-primary w-100 mt-4" type="submit">{cta} {icon("arrow")}</button><p id="authResult" class="small mt-3" role="status"></p></form>{bottom}<p class="auth-note">Demo antarmuka. Tidak ada autentikasi server, pembuatan akun, atau email yang dikirim. Gunakan data contoh; password tidak disimpan.</p></div></main></div>'

def docs():
    return heading('Mulai dari sini. Buat jadi milikmu.','Panduan singkat membangun dengan BRUTAL. dan Bootstrap 5.3.8.')+'''<div class="row g-4"><div class="col-lg-8"><section class="card mb-4"><div class="card-body"><span class="badge bg-green mb-3">LOCAL FIRST · NO BUILD REQUIRED</span><h2 class="fs-4">Hello, builder.</h2><p>BRUTAL. adalah template admin HTML statis dengan tema Neubrutalism. Grid, utilities, dan interaksi dasar memakai Bootstrap asli. Lapisan tema memberi garis tegas, pastel, dan bayangan solid.</p><div class="code">npm run dev
# Buka http://localhost:4173
# Atau buka index.html langsung di browser.</div><p class="small text-muted mt-3 mb-0">Python 3 diperlukan untuk server lokal dan generator. Tidak ada dependensi runtime CDN atau jQuery.</p></div></section><section class="card mb-4"><div class="card-body"><h2>Struktur proyek</h2><pre class="code mb-0">index.html                  Dashboard
components.html             Indeks 16 halaman komponen
alert.html / buttons.html   Contoh komponen terpisah
forms.html / tables.html     Form & tabel interaktif
assets/css/theme.css        Token, override Bootstrap, layout
assets/js/app.js            Interaksi demo & localStorage
assets/img/favicon.svg      Identitas lokal
bootstrap-5.3.8/dist/        Bootstrap vendor asli
scripts/build.py            Generator halaman & shell
assets/js/sidebar-config.js Satu konfigurasi navigasi
assets/js/sidebar.js        Renderer & drawer bersama
blank.html                  Titik awal halaman baru</pre></div></section><section class="card mb-4" id="components"><div class="card-body"><h2>Bootstrap dulu, tema setelahnya.</h2><p class="small">Urutan stylesheet penting. Semua kelas Bootstrap tetap tersedia.</p><pre class="code">&lt;link rel="stylesheet" href="bootstrap-5.3.8/dist/css/bootstrap.min.css"&gt;
&lt;link rel="stylesheet" href="assets/css/theme.css"&gt;
&lt;button class="btn btn-primary"&gt;Mulai membangun&lt;/button&gt;
&lt;script src="bootstrap-5.3.8/dist/js/bootstrap.bundle.min.js"&gt;&lt;/script&gt;
&lt;div id="sidebar-root"&gt;&lt;/div&gt;
&lt;script src="assets/js/sidebar-config.js"&gt;&lt;/script&gt;
&lt;script src="assets/js/sidebar-icons.js"&gt;&lt;/script&gt;
&lt;script src="assets/js/sidebar.js"&gt;&lt;/script&gt;
&lt;script src="assets/js/app.js"&gt;&lt;/script&gt;</pre><p class="small mb-0">Gunakan <code>.bg-purple</code>, <code>.bg-yellow</code>, <code>.bg-green</code>, <code>.bg-orange</code>, atau <code>.bg-blue</code> untuk warna pastel. Grid menggunakan <code>.row</code> dan <code>.col-*</code>.</p></div></section><section class="card mb-4"><div class="card-body"><h2>Ganti warna, pertahankan karakter.</h2><p class="small">Edit token di awal <code>assets/css/theme.css</code>. Source Bootstrap vendor tetap utuh sehingga lebih mudah diperbarui.</p><pre class="code">:root {
  --neo-purple: #c4a8f5;
  --neo-yellow: #f9de6e;
  --neo-ink: #232420;
  --neo-paper: #f5f4ef;
  --neo-shadow: 4px 4px 0 var(--neo-ink);
}</pre></div></section><section class="card"><div class="card-body"><h2>Menambah halaman</h2><ol class="small ps-3"><li class="mb-2">Salin <code>blank.html</code> ke nama halamanmu.</li><li class="mb-2">Ubah judul, breadcrumb, <code>data-page</code>, dan isi elemen <code>&lt;main&gt;</code>. Daftarkan halaman di <code>assets/js/sidebar-config.js</code>; sidebar dan pencarian otomatis mengikuti konfigurasi ini.</li><li class="mb-2">Untuk perubahan topbar/footer dan konten hasil generate, edit <code>scripts/build.py</code>, lalu jalankan <code>npm run build</code>.</li><li>Hubungkan form dan data ke backend pilihanmu.</li></ol><div class="alert alert-warning small mb-0">Generator menimpa HTML hasil generate. Simpan perubahan permanen di generator, atau gunakan salinan HTML dengan nama baru.</div></div></section></div><div class="col-lg-4"><section class="card mb-4 bg-yellow"><div class="card-body"><h2>Isi starter ini</h2><ul class="small ps-3 mb-0"><li>Dashboard, widget grafik & data</li><li>Chat, portfolio, blog & mailbox demo</li><li>16 halaman komponen Bootstrap</li><li>Form dan validasi</li><li>Tabel: cari, filter, urutkan, CSV</li><li>Kanban proyek & kalender</li><li>Profil dan preferensi</li><li>Login, register, reset password</li><li>Invoice, pricing, blank, 404</li></ul></div></section><section class="card mb-4"><div class="card-body"><h2>Interaksi & data</h2><p class="small">Proyek, tugas, agenda, profil, dan preferensi disimpan dengan prefix <code>brutal.</code> di localStorage. Data hanya berada di browser, dan berbeda antar origin.</p><p class="small mb-0">Angka statistik adalah ilustrasi tetap. Grafik SVG mendukung pergantian periode. Login/register hanya simulasi; tidak ada sesi autentikasi atau transaksi.</p></div></section><section class="card"><div class="card-body"><h2>Cakupan & pengembangan</h2><p class="small">Terinspirasi cakupan admin Otika, disusun ulang untuk Bootstrap 5. Starter ini bukan salinan satu per satu seluruh plugin Otika.</p><p class="small">Chat dan email tersedia sebagai simulasi lokal. Pengiriman nyata, peta, rich text editor, dan upload server belum diintegrasikan. Tambahkan library hanya ketika fitur tersebut diperlukan; pin versi dan muat per halaman.</p><a class="btn btn-sm" href="errors-404.html">Preview halaman 404 ↗</a></div></section></div></div>'''

def main():
    pages = {
        'index':dashboard(), 'components':components(), 'forms':forms(),
        'tables':heading('Data rapi. Keputusan tepat.','Cari, filter, dan ekspor proyek dari workspace demo.',new_project_button())+projects_table(True),
        'charts':heading('Angka yang punya cerita.','Widget statistik dan grafik SVG lokal. Data ilustratif, tanpa library tambahan.')+stats()+f'<div class="dashboard-grid">{chart_panel()}{source_panel()}</div>'+card('Aktivitas workspace','<div class="mt-4">'+''.join(f'<div class="timeline-item"><h3>{t}</h3><p class="small text-muted mb-0">{d}</p></div>' for t,d in [('Website studio masuk tahap review','Hari ini, 09.30 · oleh Alex Darma'),('Brand identity diselesaikan','Kemarin, 16.45 · oleh Nina Sari'),('Proyek baru ditambahkan','25 September, 10.00 · oleh Rio Kurnia')])+'</div>'),
        'projects':projects(), 'calendar':calendar(), 'profile':profile(), 'invoice':invoice(), 'pricing':pricing(), 'docs':docs(),
        'blank':heading('Sesuatu yang besar dimulai di sini.','Halaman kosong, penuh kemungkinan.')+card('Kanvas berikutnya milikmu.','<div class="text-center py-5"><span class="brand-mark bg-yellow mx-auto mb-4" style="width:60px;height:60px;font-size:40px">✳</span><h2 class="fs-3">Satu ide sudah cukup.</h2><p class="text-muted mb-4">Mulai dengan komponen yang ada, lalu buat jadi sesuatu yang baru.</p><a class="btn btn-primary" href="components.html">Jelajahi komponen '+icon('arrow')+'</a></div>')
    }
    pages.update(build_pages(heading, icon))
    pages.update(build_workspace_pages(heading, icon, stats))
    write_workspace_assets(ROOT)
    (ROOT/'assets/js/sidebar-icons.js').write_text('// Generated from ICONS in scripts/build.py.\nwindow.BRUTAL_ICONS = '+json.dumps(ICONS)+';\n',encoding='utf-8')
    write_flags(ROOT)
    def write_page(key, content, standalone=False):
        source = page(key, content, standalone)
        formatted = format_html(source)
        valid, reason = verify_semantic(source, formatted)
        if not valid:
            raise ValueError(f'HTML formatting changed {key}.html: {reason}')
        (ROOT/f'{key}.html').write_text(formatted,encoding='utf-8')

    for key,content in pages.items():
        write_page(key, content)
    for key in ['auth-login','auth-register','auth-forgot-password']:
        write_page(key, auth(key), True)
    error = '<main class="min-vh-100 d-flex align-items-center justify-content-center p-4 text-center" id="main"><div><span class="badge bg-yellow mb-4">A LITTLE LOST, STILL BOLD.</span><div class="error-code">404</div><h1 class="mt-4">Oops. Ide ini belum ada.</h1><p class="text-muted mb-4">Halaman yang kamu cari mungkin sudah pindah.<br>Yuk, kembali ke tempat semua ide dimulai.</p><a class="btn btn-primary" href="index.html">Kembali ke dashboard '+icon('arrow')+'</a></div></main>'
    write_page('errors-404', error, True)
    print(f'Built {len(pages)+4} static pages.')

if __name__ == '__main__':
    main()
