/* Phase 8 maps: browser-only Google key and locally bundled world map. */
(() => {
  'use strict';

  const page = document.body.dataset.page;
  const status = document.getElementById('mapStatus');
  const result = document.getElementById('mapResult');
  const indonesia = { lat: -2.5, lng: 118 };
  const jakarta = { lat: -6.2088, lng: 106.8456 };
  const cities = [
    { name: 'Jakarta', lat: -6.2088, lng: 106.8456 },
    { name: 'Bandung', lat: -6.9175, lng: 107.6191 },
    { name: 'Yogyakarta', lat: -7.7956, lng: 110.3695 },
    { name: 'Surabaya', lat: -7.2575, lng: 112.7521 },
    { name: 'Denpasar', lat: -8.6705, lng: 115.2126 },
  ];

  function say(message, isError = false) {
    if (!status) return;
    status.textContent = message;
    status.classList.toggle('is-error', isError);
  }

  function loadGoogle(key) {
    if (window.google?.maps?.importLibrary) return Promise.resolve();
    if (window.brutalMapsLoad) return window.brutalMapsLoad;

    window.brutalMapsLoad = new Promise((resolve, reject) => {
      const callback = '__brutalMapsReady';
      const script = document.createElement('script');
      let timer;
      const fail = () => {
        clearTimeout(timer);
        delete window[callback];
        script.remove();
        window.brutalMapsLoad = null;
        reject(new Error('Google Maps gagal dimuat. Periksa key, billing, batasan domain, dan koneksi.'));
      };
      window[callback] = () => {
        clearTimeout(timer);
        delete window[callback];
        resolve();
      };
      window.gm_authFailure = fail;
      script.onerror = fail;
      timer = setTimeout(fail, 15000);
      script.src = `https://maps.googleapis.com/maps/api/js?key=${encodeURIComponent(key)}&v=weekly&loading=async&language=id&callback=${callback}`;
      script.async = true;
      document.head.append(script);
    });
    return window.brutalMapsLoad;
  }

  async function marker(map, position, title, draggable = false) {
    const { AdvancedMarkerElement } = await google.maps.importLibrary('marker');
    return new AdvancedMarkerElement({ map, position, title, gmpDraggable: draggable });
  }

  async function drawRoute(map, withWaypoint = false, alternatives = false) {
    const { Route } = await google.maps.importLibrary('routes');
    const request = {
      origin: 'Jakarta, Indonesia',
      destination: withWaypoint ? 'Semarang, Indonesia' : 'Bandung, Indonesia',
      travelMode: 'DRIVING',
      fields: ['path', 'viewport', 'distanceMeters', 'durationMillis', 'routeLabels'],
    };
    if (withWaypoint) request.intermediates = [{ location: 'Cirebon, Indonesia' }];
    if (alternatives) request.computeAlternativeRoutes = true;
    const response = await Route.computeRoutes(request);
    if (!response.routes?.length) throw new Error('Rute tidak ditemukan untuk lokasi ini.');
    const colors = ['#7951ae', '#238f69', '#eb8749', '#466bce'];
    response.routes.forEach((route, index) => {
      route.createPolylines({
        polylineOptions: { map, strokeColor: colors[index % colors.length], strokeOpacity: index ? 0.75 : 1, strokeWeight: index ? 5 : 7 },
        colorScheme: map.get('colorScheme'),
      });
    });
    const main = response.routes[0];
    if (main.viewport) map.fitBounds(main.viewport, 50);
    await main.createWaypointAdvancedMarkers({ map });
    const distance = main.distanceMeters ? `${(main.distanceMeters / 1000).toFixed(0)} km` : 'jarak tersedia di peta';
    say(`${response.routes.length} rute ditemukan · ${distance}.`);
  }

  async function initGoogle() {
    const { Map, InfoWindow } = await google.maps.importLibrary('maps');
    const element = document.getElementById('googleMap');
    const map = new Map(element, {
      center: page === 'gmaps-simple' ? indonesia : jakarta,
      zoom: page === 'gmaps-simple' ? 5 : 11,
      mapId: 'DEMO_MAP_ID',
      mapTypeControl: false,
      streetViewControl: false,
    });
    document.getElementById('mapPlaceholder').hidden = true;

    if (page === 'gmaps-marker') {
      const pin = await marker(map, jakarta, 'Jakarta');
      const info = new InfoWindow({ content: '<strong>Jakarta</strong><br>Ibu kota Indonesia dan titik awal cerita ini.' });
      pin.addListener('click', () => info.open({ anchor: pin, map }));
    }
    if (page === 'gmaps-multiple-marker') {
      const bounds = new google.maps.LatLngBounds();
      const info = new InfoWindow();
      for (const city of cities) {
        const pin = await marker(map, { lat: city.lat, lng: city.lng }, city.name);
        pin.addListener('click', () => {
          info.setContent(`<strong>${city.name}</strong>`);
          info.open({ anchor: pin, map });
        });
        bounds.extend({ lat: city.lat, lng: city.lng });
      }
      map.fitBounds(bounds, 55);
    }
    if (page === 'gmaps-route') await drawRoute(map);
    if (page === 'gmaps-advanced-route') {
      let activePolylines = [];
      let activeMarkers = [];
      const render = async (mode) => {
        activePolylines.forEach(line => line.setMap(null));
        activeMarkers.forEach(pin => { pin.map = null; });
        const { Route } = await google.maps.importLibrary('routes');
        const request = {
          origin: 'Jakarta, Indonesia',
          destination: mode === 'via' ? 'Semarang, Indonesia' : 'Bandung, Indonesia',
          travelMode: 'DRIVING',
          fields: ['path', 'viewport', 'distanceMeters', 'routeLabels'],
        };
        if (mode === 'via') request.intermediates = [{ location: 'Cirebon, Indonesia' }];
        else request.computeAlternativeRoutes = true;
        const { routes } = await Route.computeRoutes(request);
        if (!routes?.length) throw new Error('Rute tidak ditemukan.');
        activePolylines = routes.flatMap((route, index) => route.createPolylines({
          polylineOptions: { map, strokeColor: ['#7951ae', '#238f69', '#eb8749', '#466bce'][index % 4], strokeWeight: 6, strokeOpacity: index ? 0.7 : 1 },
          colorScheme: map.get('colorScheme'),
        }));
        activeMarkers = await routes[0].createWaypointAdvancedMarkers({ map });
        if (routes[0].viewport) map.fitBounds(routes[0].viewport, 50);
        say(mode === 'via' ? 'Rute Jakarta → Cirebon → Semarang.' : `${routes.length} pilihan rute Jakarta → Bandung.`);
      };
      document.querySelectorAll('[data-map-route]').forEach(button => button.addEventListener('click', async () => {
        document.querySelectorAll('[data-map-route]').forEach(item => item.classList.toggle('btn-primary', item === button));
        try { await render(button.dataset.mapRoute); } catch (error) { say(error.message, true); }
      }));
      await render('via');
    }
    if (page === 'gmaps-draggable-marker') {
      const pin = await marker(map, jakarta, 'Geser marker Jakarta', true);
      const update = () => {
        const point = pin.position;
        const lat = typeof point.lat === 'function' ? point.lat() : point.lat;
        const lng = typeof point.lng === 'function' ? point.lng() : point.lng;
        result.textContent = `Koordinat: ${Number(lat).toFixed(5)}, ${Number(lng).toFixed(5)}`;
      };
      pin.addEventListener('gmp-drag', update);
      pin.addEventListener('gmp-dragend', update);
    }
    if (page === 'gmaps-geocoding') {
      const { Geocoder } = await google.maps.importLibrary('geocoding');
      const geocoder = new Geocoder();
      const pin = await marker(map, jakarta, 'Hasil pencarian');
      document.getElementById('mapSearchForm').addEventListener('submit', async event => {
        event.preventDefault();
        const address = document.getElementById('mapAddress').value.trim();
        if (!address) return;
        result.textContent = 'Mencari alamat…';
        try {
          const { results } = await geocoder.geocode({ address });
          if (!results?.length) throw new Error('Alamat tidak ditemukan.');
          const place = results[0];
          pin.position = place.geometry.location;
          map.setCenter(place.geometry.location);
          map.setZoom(14);
          result.textContent = place.formatted_address;
        } catch (error) {
          result.textContent = error.message?.includes('REQUEST_DENIED')
            ? 'Pencarian ditolak. Aktifkan Geocoding API dan izinkan situs ini pada pembatasan API key.'
            : error.message || 'Pencarian gagal.';
        }
      });
    }
    if (page === 'gmaps-geolocation') {
      let pin;
      document.getElementById('mapLocate').addEventListener('click', () => {
        if (!navigator.geolocation) { result.textContent = 'Browser tidak mendukung lokasi.'; return; }
        result.textContent = 'Meminta izin lokasi…';
        navigator.geolocation.getCurrentPosition(async position => {
          const point = { lat: position.coords.latitude, lng: position.coords.longitude };
          if (pin) pin.position = point;
          else pin = await marker(map, point, 'Lokasi saya');
          map.setCenter(point);
          map.setZoom(15);
          result.textContent = `Lokasi: ${point.lat.toFixed(5)}, ${point.lng.toFixed(5)}`;
        }, () => { result.textContent = 'Lokasi tidak tersedia. Periksa izin browser dan gunakan HTTPS atau localhost.'; },
        { enableHighAccuracy: true, timeout: 10000 });
      });
    }
    if (!status.classList.contains('is-error') && !['gmaps-route', 'gmaps-advanced-route'].includes(page)) say('Peta berhasil dimuat. Selamat menjelajah!');
  }

  function initVector() {
    const selected = document.getElementById('vectorSelection');
    if (!window.jsVectorMap) { selected.textContent = 'Peta vektor gagal dimuat.'; return; }
    new jsVectorMap({
      selector: '#vectorMap', map: 'world', zoomButtons: true,
      backgroundColor: '#fffefb',
      regionStyle: { initial: { fill: '#f9de6e', stroke: '#232420', strokeWidth: 0.55 }, hover: { fill: '#c4a8f5' }, selected: { fill: '#c4a8f5' } },
      markerStyle: { initial: { fill: '#238f69', stroke: '#232420', strokeWidth: 2, r: 6 }, hover: { fill: '#c7e8cc' } },
      markers: [{ name: 'Jakarta', coords: [-6.2088, 106.8456] }, { name: 'London', coords: [51.5072, -0.1276] }, { name: 'New York', coords: [40.7128, -74.006] }],
      selectedRegions: ['ID'],
      onRegionClick(event, code) {
        const name = this.regions[code]?.config?.name || code;
        selected.textContent = `Negara dipilih: ${name} (${code})`;
      },
      onMarkerClick(event, index) {
        selected.textContent = `Kota dipilih: ${['Jakarta', 'London', 'New York'][index]}`;
      },
    });
  }

  if (page === 'vector-map') { initVector(); return; }
  if (!page?.startsWith('gmaps-')) return;
  const form = document.getElementById('mapKeyForm');
  const input = document.getElementById('mapApiKey');
  const saved = localStorage.getItem('brutal.mapsApiKey');
  let initialized = false;
  async function activate(key) {
    if (initialized) return;
    say('Memuat Google Maps…');
    try {
      await loadGoogle(key);
      localStorage.setItem('brutal.mapsApiKey', key);
      await initGoogle();
      initialized = true;
      input.value = '';
    } catch (error) { say(error.message || 'Peta gagal dimuat.', true); }
  }
  form.addEventListener('submit', event => {
    event.preventDefault();
    const key = input.value.trim();
    if (key) activate(key);
  });
  document.getElementById('mapForgetKey').addEventListener('click', () => {
    localStorage.removeItem('brutal.mapsApiKey');
    input.value = '';
    say('Key tersimpan dihapus dari browser ini.');
  });
  if (saved) activate(saved);
})();
