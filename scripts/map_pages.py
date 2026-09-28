"""Phase 8 map showcases. Google credentials are entered at runtime."""

MAP_PAGES = (
    'gmaps-simple', 'gmaps-marker', 'gmaps-multiple-marker', 'gmaps-route',
    'gmaps-advanced-route', 'gmaps-draggable-marker', 'gmaps-geocoding',
    'gmaps-geolocation', 'vector-map',
)

GOOGLE_DEMOS = {
    'gmaps-simple': ('Peta Indonesia, mulai dari sini.', 'Peta dasar dengan pusat Jakarta dan kontrol navigasi Google Maps.', ''),
    'gmaps-marker': ('Satu pin, satu cerita.', 'Klik marker Jakarta untuk membuka info window.', ''),
    'gmaps-multiple-marker': ('Beberapa kota, satu peta.', 'Marker Jakarta, Bandung, Yogyakarta, Surabaya, dan Bali dibuat dari data array.', ''),
    'gmaps-route': ('Dari Jakarta ke Bandung.', 'Rute berkendara A ke B menggunakan Routes Library.', ''),
    'gmaps-advanced-route': ('Pilih jalurmu sendiri.', 'Bandingkan rute via Cirebon dengan pilihan rute alternatif tanpa perhentian.',
        '<div class="map-controls" role="group" aria-label="Jenis rute">'
        '<button type="button" class="btn btn-primary" data-map-route="via">Via Cirebon</button>'
        '<button type="button" class="btn" data-map-route="alternatives">Rute alternatif</button></div>'),
    'gmaps-draggable-marker': ('Geser titik, baca koordinat.', 'Tarik marker atau gunakan keyboard; koordinat akan diperbarui.',
        '<p class="map-result" id="mapResult" aria-live="polite">Koordinat awal: -6.2088, 106.8456</p>'),
    'gmaps-geocoding': ('Temukan alamat di peta.', 'Cari alamat dan pindahkan marker ke hasilnya.',
        '<form class="map-controls" id="mapSearchForm"><label class="visually-hidden" for="mapAddress">Alamat</label>'
        '<input class="form-control" id="mapAddress" type="search" placeholder="Contoh: Monas, Jakarta" required>'
        '<button class="btn btn-primary" type="submit">Cari alamat</button></form>'
        '<p class="map-result" id="mapResult" aria-live="polite">Masukkan alamat setelah peta dimuat.</p>'),
    'gmaps-geolocation': ('Lihat lokasi kamu.', 'Izinkan lokasi pada browser untuk menampilkan titik kamu saat ini.',
        '<div class="map-controls"><button class="btn btn-primary" id="mapLocate" type="button">Lokasi saya</button></div>'
        '<p class="map-result" id="mapResult" aria-live="polite">Lokasi belum diminta.</p>'),
}


def google_page(key, heading):
    title, intro, controls = GOOGLE_DEMOS[key]
    setup = (
        '<section class="card map-setup"><div class="card-body"><h2>Hubungkan Google Maps</h2>'
        '<p>Aktifkan billing serta <strong>Maps JavaScript API</strong> di Google Cloud. Untuk demo rute, aktifkan juga '
        '<strong>Routes API</strong>; untuk pencarian alamat, aktifkan <strong>Geocoding API</strong>. '
        'Gunakan API key browser yang dibatasi ke domain situsmu.</p>'
        '<form id="mapKeyForm" class="map-key-form"><label class="form-label" for="mapApiKey">Google Maps API key</label>'
        '<div class="map-key-row"><input id="mapApiKey" class="form-control" type="password" autocomplete="off" '
        'placeholder="Tempel API key di browser ini" required><button class="btn btn-primary" type="submit">Muat peta</button></div>'
        '<p class="small text-muted mb-0 mt-2">Key disimpan hanya di browser ini agar tersedia di halaman Maps lain. '
        'Jangan masukkan key yang belum dibatasi.</p></form>'
        '<button type="button" class="btn btn-sm mt-3" id="mapForgetKey">Hapus key tersimpan</button>'
        '<p id="mapStatus" class="map-status" role="status" aria-live="polite">Masukkan API key untuk mengaktifkan peta.</p>'
        '</div></section>'
    )
    map_area = (
        '<section class="card map-card"><div class="card-body"><div class="panel-heading"><div><h2>Preview peta</h2>'
        '<p>Jelajahi demo setelah API key terhubung.</p></div><span class="badge bg-purple">Google Maps</span></div>'
        '<div class="map-stage"><div id="googleMap" class="google-map" role="region" aria-label="Peta interaktif"></div>'
        '<div id="mapPlaceholder" class="map-placeholder"><span class="map-pin-art" aria-hidden="true">⌖</span>'
        '<strong>Peta siap dijelajahi.</strong><span>Masukkan API key di panel atas untuk memuat peta.</span></div></div>'
        + controls + '</div></section>'
    )
    return heading(title, intro) + '<div class="map-layout">' + setup + map_area + '</div>'


def vector_page(heading):
    return (heading('Dunia dalam satu kanvas.', 'Peta vektor dunia interaktif dengan region berwarna, marker kota, dan zoom lokal.')
        + '<div class="map-summary"><span class="badge bg-yellow">Tanpa API key</span>'
        '<p>Gerakkan pointer atau fokus ke negara untuk melihat namanya. Klik region untuk memperbarui panel pilihan.</p></div>'
        '<section class="card map-card"><div class="card-body"><div class="panel-heading"><div><h2>Jelajahi dunia</h2>'
        '<p>jsVectorMap dengan data peta dunia lokal.</p></div><span class="badge bg-green">Interactive</span></div>'
        '<div id="vectorMap" class="vector-map" role="region" aria-label="Peta vektor dunia"></div>'
        '<p id="vectorSelection" class="map-result" role="status" aria-live="polite">Klik negara untuk melihat detail.</p>'
        '<div class="map-legend"><span><i class="legend-dot legend-purple"></i> Negara pilihan</span>'
        '<span><i class="legend-dot legend-yellow"></i> Negara lain</span>'
        '<span><i class="legend-dot legend-green"></i> Kota contoh</span></div></div></section>')


def build_map_pages(heading):
    pages = {key: google_page(key, heading) for key in GOOGLE_DEMOS}
    pages['vector-map'] = vector_page(heading)
    return pages
