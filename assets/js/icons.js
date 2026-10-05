/* Search and copy controls shared by the local icon showcases. */
(() => {
  const search = document.getElementById('iconSearch');
  if (!search) return;
  const items = [...document.querySelectorAll('.icon-item')];
  const count = document.getElementById('iconCount');
  const empty = document.getElementById('iconEmpty');
  const status = document.getElementById('iconCopyStatus');

  function filterIcons() {
    const query = search.value.trim().toLocaleLowerCase('id');
    let visible = 0;
    items.forEach((item) => {
      const matched = item.dataset.iconName.includes(query);
      item.hidden = !matched;
      if (matched) visible += 1;
    });
    count.textContent = `${visible} dari ${items.length} ikon tampil`;
    empty.classList.toggle('d-none', visible !== 0);
  }

  async function copyText(value) {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(value);
      return;
    }
    const field = document.createElement('textarea');
    field.value = value;
    field.style.position = 'fixed';
    field.style.opacity = '0';
    document.body.appendChild(field);
    field.select();
    const copied = document.execCommand('copy');
    field.remove();
    if (!copied) throw new Error('copy failed');
  }

  search.addEventListener('input', filterIcons);
  document.addEventListener('click', async (event) => {
    const button = event.target.closest('.icon-copy');
    if (!button) return;
    const previous = button.textContent;
    try {
      const value = button.dataset.copyKey
        ? window.BRUTAL_FEATHER_SVG?.[button.dataset.copyKey]
        : button.dataset.copy;
      if (!value) throw new Error('icon source missing');
      await copyText(value);
      button.textContent = 'Tersalin!';
      status.textContent = `Kode ${button.closest('.icon-item').querySelector('h3').textContent} tersalin.`;
    } catch (_) {
      button.textContent = 'Gagal salin';
      status.textContent = 'Clipboard tidak tersedia. Pilih kode pada kartu untuk menyalin manual.';
    }
    window.setTimeout(() => { button.textContent = previous; }, 1800);
  });
  filterIcons();
})();
