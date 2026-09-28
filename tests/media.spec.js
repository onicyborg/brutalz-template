const { test, expect } = require('@playwright/test');

const mediaPages = ['light-gallery', 'gallery1', 'carousel', 'owl-carousel', 'timeline'];

test('all five media pages are linked from the sidebar', async ({ page }) => {
  await page.goto('/light-gallery.html');
  for (const name of mediaPages) {
    await expect(page.locator(`#sidebar a[href="${name}.html"]`)).toHaveCount(1);
  }
});

test('GLightbox opens local artwork and closes by keyboard', async ({ page }) => {
  await page.goto('/light-gallery.html');
  await expect(page.locator('.light-gallery-item')).toHaveCount(6);
  await page.locator('.light-gallery-item').first().click();
  await expect(page.locator('.glightbox-container')).toBeVisible();
  await expect(page.locator('.gslide.current img')).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(page.locator('.glightbox-container')).toBeHidden();
});

test('CSS masonry gallery and three timeline variants show their artwork', async ({ page }) => {
  await page.goto('/gallery1.html');
  await expect(page.locator('.masonry-item')).toHaveCount(6);
  await expect(page.locator('.masonry-item img')).toHaveCount(6);
  await page.goto('/timeline.html');
  await expect(page.locator('.media-timeline')).toHaveCount(3);
  await expect(page.locator('.media-timeline-zigzag li')).toHaveCount(4);
  await expect(page.locator('.media-timeline-content img')).toHaveCount(2);
});

test('Bootstrap carousel controls move all three showcase variants', async ({ page }) => {
  await page.goto('/carousel.html');
  for (const id of ['mediaHeroCarousel', 'mediaMultiCarousel', 'mediaCaptionCarousel']) {
    const carousel = page.locator(`#${id}`);
    const first = await carousel.locator('.carousel-item.active').textContent();
    await carousel.getByRole('button', { name: 'Slide berikutnya' }).click();
    await expect(carousel.locator('.carousel-item.active')).not.toHaveText(first);
  }
});

test('Owl Carousel initializes responsive, autoplay and thumbnail navigation', async ({ page }) => {
  await page.goto('/owl-carousel.html');
  for (const id of ['owlBasic', 'owlAutoplay', 'owlThumbs']) {
    await expect(page.locator(`#${id}`)).toHaveClass(/owl-loaded/);
  }
  const toggle = page.locator('#owlAutoplayToggle');
  await toggle.click();
  await expect(toggle).toHaveAttribute('aria-pressed', 'true');
  await page.getByRole('button', { name: 'Tampilkan Mono Journal' }).click();
  await expect(page.getByRole('button', { name: 'Tampilkan Mono Journal' })).toHaveAttribute('aria-pressed', 'true');
  await expect(page.locator('#owlThumbs .owl-item.active h3')).toHaveText('Mono Journal');
});
