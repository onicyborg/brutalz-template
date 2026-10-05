/* Phase 7: local GLightbox and Owl Carousel initializers. */
(() => {
  if (document.body.dataset.page === 'light-gallery' && window.GLightbox) {
    window.GLightbox({ selector: '.glightbox', loop: true, touchNavigation: true });
  }

  if (document.body.dataset.page !== 'owl-carousel' || !window.jQuery?.fn.owlCarousel) return;
  const $ = window.jQuery;
  function labelNavigation() {
    for (const [selector, label] of [['.owl-prev', 'Slide sebelumnya'], ['.owl-next', 'Slide berikutnya']]) {
      document.querySelectorAll(selector).forEach(button => {
        button.setAttribute('aria-label', label);
        button.disabled = button.classList.contains('disabled');
      });
    }
  }
  $('.owl-carousel').on('initialized.owl.carousel refreshed.owl.carousel translated.owl.carousel', labelNavigation);
  const navigation = { nav: true, navText: ['chevron-left', 'chevron-right'].map(name => `<svg class="icon" aria-hidden="true" viewBox="0 0 24 24">${window.BRUTAL_ICONS[name]}</svg>`), dots: true, margin: 16, smartSpeed: 350 };
  $('#owlBasic').owlCarousel({ ...navigation, loop: false, responsive: { 0: { items: 1 }, 600: { items: 2 }, 1050: { items: 3 } } });
  const auto = $('#owlAutoplay').owlCarousel({ ...navigation, loop: true, items: 1, autoplay: true, autoplayTimeout: 3200, autoplayHoverPause: true });
  const toggle = document.getElementById('owlAutoplayToggle');
  toggle.addEventListener('click', () => {
    const paused = toggle.getAttribute('aria-pressed') === 'true';
    auto.trigger(paused ? 'play.owl.autoplay' : 'stop.owl.autoplay', [3200]);
    toggle.setAttribute('aria-pressed', String(!paused));
    toggle.textContent = paused ? 'Jeda autoplay' : 'Lanjut autoplay';
  });

  const thumbs = $('#owlThumbs').owlCarousel({ ...navigation, loop: false, items: 1, dots: false });
  labelNavigation();
  const buttons = [...document.querySelectorAll('[data-owl-thumb]')];
  function setActive(index) {
    buttons.forEach((button, position) => {
      button.classList.toggle('active', position === index);
      button.setAttribute('aria-pressed', String(position === index));
    });
  }
  thumbs.on('changed.owl.carousel', (event) => setActive(event.item.index));
  buttons.forEach((button) => button.addEventListener('click', () => {
    const index = Number(button.dataset.owlThumb);
    thumbs.trigger('to.owl.carousel', [index, 350]);
    setActive(index);
  }));
})();
