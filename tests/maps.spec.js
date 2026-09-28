const { test, expect } = require('@playwright/test');

test('Google Maps shows setup before any remote request', async ({ page }) => {
  const remote = [];
  page.on('request', request => {
    if (request.url().includes('maps.googleapis.com')) remote.push(request.url());
  });
  await page.goto('/gmaps-simple.html');
  await expect(page.locator('#mapPlaceholder')).toBeVisible();
  await expect(page.locator('#mapApiKey')).toBeVisible();
  expect(remote).toHaveLength(0);
});

test('world vector map renders offline and responds to region clicks', async ({ page }) => {
  await page.goto('/vector-map.html');
  await expect(page.locator('#vectorMap svg')).toBeVisible();
  const indonesia = page.locator('#vectorMap [data-code="ID"]');
  await expect(indonesia).toHaveCount(1);
  await indonesia.evaluate(element => element.dispatchEvent(new MouseEvent('click', { bubbles: true })));
  await expect(page.locator('#vectorSelection')).toContainText('ID');
});

async function mockGoogle(page) {
  await page.addInitScript(() => {
    localStorage.setItem('brutal.mapsApiKey', 'test-only-key');
    window.mapCalls = { routes: [], markers: [], geocodes: [] };
    class Map {
      constructor(element, options) { this.element = element; this.options = options; }
      fitBounds() {}
      setCenter(point) { this.center = point; }
      setZoom(zoom) { this.zoom = zoom; }
      get() { return 'LIGHT'; }
    }
    class AdvancedMarkerElement {
      constructor(options) { Object.assign(this, options); window.mapCalls.markers.push(this); }
      addListener() {}
      addEventListener(name, callback) { this[name] = callback; }
    }
    class Route {
      static async computeRoutes(request) {
        window.mapCalls.routes.push(request);
        const route = {
          viewport: {}, distanceMeters: 150000,
          createPolylines: () => [{ setMap() {} }],
          createWaypointAdvancedMarkers: async () => [],
        };
        return { routes: request.computeAlternativeRoutes ? [route, route] : [route] };
      }
    }
    class Geocoder {
      async geocode(options) {
        window.mapCalls.geocodes.push(options.address);
        return { results: [{ formatted_address: 'Monas, Jakarta', geometry: { location: { lat: -6.17, lng: 106.83 } } }] };
      }
    }
    window.google = { maps: {
      Map, InfoWindow: class {}, AdvancedMarkerElement, LatLngBounds: class { extend() {} },
      importLibrary: async name => ({ maps: { Map, InfoWindow: class {} }, marker: { AdvancedMarkerElement }, routes: { Route }, geocoding: { Geocoder } })[name],
    } };
  });
}

test('markers, route modes, geocoding, and draggable coordinates work', async ({ page }) => {
  await mockGoogle(page);
  await page.goto('/gmaps-multiple-marker.html');
  await expect(page.locator('#mapPlaceholder')).toBeHidden();
  expect(await page.evaluate(() => window.mapCalls.markers.length)).toBe(5);

  await page.goto('/gmaps-advanced-route.html');
  await expect(page.locator('#mapStatus')).toContainText('Cirebon');
  await page.locator('[data-map-route="alternatives"]').click();
  await expect(page.locator('#mapStatus')).toContainText('2 pilihan rute');
  const requests = await page.evaluate(() => window.mapCalls.routes);
  expect(requests[0].intermediates).toHaveLength(1);
  expect(requests[1].computeAlternativeRoutes).toBe(true);
  expect(requests[1].intermediates).toBeUndefined();

  await page.goto('/gmaps-geocoding.html');
  await page.locator('#mapAddress').fill('Monas');
  await page.locator('#mapSearchForm button').click();
  await expect(page.locator('#mapResult')).toHaveText('Monas, Jakarta');

  await page.goto('/gmaps-draggable-marker.html');
  await page.evaluate(() => {
    const pin = window.mapCalls.markers[0];
    pin.position = { lat: -6.5, lng: 107.25 };
    pin['gmp-drag']();
  });
  await expect(page.locator('#mapResult')).toContainText('-6.50000, 107.25000');
});

test('geolocation centers map on browser location and key can be removed', async ({ page, context }) => {
  await mockGoogle(page);
  await context.grantPermissions(['geolocation']);
  await context.setGeolocation({ latitude: -6.2, longitude: 106.8 });
  await page.goto('/gmaps-geolocation.html');
  await page.locator('#mapLocate').click();
  await expect(page.locator('#mapResult')).toContainText('-6.20000, 106.80000');
  await page.locator('#mapForgetKey').click();
  expect(await page.evaluate(() => localStorage.getItem('brutal.mapsApiKey'))).toBeNull();
});
