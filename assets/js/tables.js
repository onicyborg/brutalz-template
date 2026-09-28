/* Phase 4 table demos. The workspace project table stays in app.js. */
(() => {
  'use strict';
  const $ = selector => document.querySelector(selector);

  if ($('#advancedTable')) {
    const table = $('#advancedTable');
    const body = table.tBodies[0];
    let column = -1;
    let direction = 1;
    table.tHead.addEventListener('click', event => {
      const button = event.target.closest('[data-sort]');
      if (!button) return;
      const header = button.closest('th');
      const nextColumn = header.cellIndex;
      direction = nextColumn === column ? -direction : 1;
      column = nextColumn;
      const kind = button.dataset.sort;
      const value = row => row.cells[column].dataset.order || row.cells[column].textContent.trim();
      const rows = [...body.rows];
      rows.sort((a, b) => {
        const left = value(a);
        const right = value(b);
        return direction * (kind === 'number'
          ? Number(left) - Number(right)
          : left.localeCompare(right, 'id', { numeric: true }));
      });
      body.append(...rows);
      table.tHead.querySelectorAll('th').forEach(th => th.removeAttribute('aria-sort'));
      header.setAttribute('aria-sort', direction === 1 ? 'ascending' : 'descending');
      $('#advancedSortStatus').textContent = `${button.textContent.trim()} diurutkan ${direction === 1 ? 'naik' : 'turun'}.`;
    });
  }

  const labels = {
    search: 'Cari:', lengthMenu: 'Tampilkan _MENU_ data',
    info: 'Menampilkan _START_–_END_ dari _TOTAL_ data',
    infoEmpty: 'Tidak ada data', infoFiltered: '(disaring dari _MAX_ data)',
    zeroRecords: 'Tidak ada data yang cocok',
    paginate: { first: 'Awal', previous: 'Sebelumnya', next: 'Berikutnya', last: 'Akhir' },
  };
  if ($('#dataTableDemo')) {
    new DataTable('#dataTableDemo', {
      pageLength: 5, order: [[0, 'asc']], language: labels,
      layout: { topStart: 'pageLength', topEnd: 'search', bottomStart: 'info', bottomEnd: 'paging' },
    });
  }

  if ($('#exportTableDemo')) {
    DataTable.Buttons.jszip(JSZip);
    DataTable.Buttons.pdfMake(pdfMake);
    new DataTable('#exportTableDemo', {
      pageLength: 5, order: [[0, 'asc']], language: labels,
      layout: {
        topStart: { buttons: [
          { extend: 'excelHtml5', text: 'Excel', title: 'BRUTAL Proyek Demo', filename: 'brutal-proyek-demo' },
          { extend: 'csvHtml5', text: 'CSV', title: 'BRUTAL Proyek Demo', filename: 'brutal-proyek-demo', bom: true },
          { extend: 'pdfHtml5', text: 'PDF', title: 'BRUTAL Proyek Demo', filename: 'brutal-proyek-demo', orientation: 'landscape' },
          { extend: 'print', text: 'Print', title: 'BRUTAL Proyek Demo' },
        ] },
        topEnd: 'search', bottomStart: 'info', bottomEnd: 'paging',
      },
    });
  }

  if ($('#editableTable')) {
    const table = $('#editableTable');
    const key = 'brutal.editableTable';
    const status = $('#editableStatus');
    const defaults = {};
    table.querySelectorAll('tr[data-record]').forEach(row => {
      defaults[row.dataset.record] = {};
      row.querySelectorAll('[data-field]').forEach(button => {
        defaults[row.dataset.record][button.dataset.field] = button.dataset.value || button.textContent.trim();
      });
    });
    let data = {};
    try {
      const saved = JSON.parse(localStorage.getItem(key) || '{}');
      if (saved && typeof saved === 'object' && !Array.isArray(saved)) data = saved;
    } catch (_) { /* Browser storage may be disabled or contain invalid demo data. */ }
    const allowed = {
      name: value => typeof value === 'string' && value.trim().length > 0 && value.length <= 70,
      category: value => typeof value === 'string' && value.trim().length > 0 && value.length <= 40,
      budget: value => typeof value === 'string' && /^\d{1,9}$/.test(value) && Number(value) > 0,
    };
    const label = (field, value) => field === 'budget' ? `Rp${Number(value).toLocaleString('id-ID')}` : value;
    const render = () => {
      table.querySelectorAll('tr[data-record]').forEach(row => {
        row.querySelectorAll('[data-field]').forEach(button => {
          const field = button.dataset.field;
          const value = data[row.dataset.record]?.[field];
          const safe = allowed[field](value) ? value.trim() : defaults[row.dataset.record][field];
          button.dataset.value = safe;
          button.textContent = label(field, safe);
        });
      });
    };
    const persist = () => {
      try { localStorage.setItem(key, JSON.stringify(data)); }
      catch (_) { status.textContent = 'Perubahan terlihat sementara; penyimpanan browser tidak tersedia.'; }
    };
    render();
    table.addEventListener('click', event => {
      const button = event.target.closest('.editable-cell');
      if (!button || table.querySelector('.editable-input')) return;
      const row = button.closest('tr[data-record]');
      const field = button.dataset.field;
      const original = button.dataset.value;
      const editor = document.createElement('div');
      editor.className = 'editable-controls';
      const input = document.createElement('input');
      input.className = 'form-control form-control-sm editable-input';
      input.type = field === 'budget' ? 'number' : 'text';
      input.min = field === 'budget' ? '1' : '';
      input.maxLength = field === 'name' ? 70 : 40;
      input.value = original;
      input.setAttribute('aria-label', `Ubah ${field} untuk ${row.dataset.record}`);
      const saveButton = document.createElement('button');
      saveButton.type = 'button';
      saveButton.className = 'btn btn-primary btn-sm';
      saveButton.textContent = 'Simpan';
      const cancelButton = document.createElement('button');
      cancelButton.type = 'button';
      cancelButton.className = 'btn btn-sm';
      cancelButton.textContent = 'Batal';
      editor.append(input, saveButton, cancelButton);
      button.replaceWith(editor);
      input.focus();
      input.select();
      let closed = false;
      const close = save => {
        if (closed) return;
        const value = input.value.trim();
        if (save && !allowed[field](value)) {
          input.classList.add('is-invalid');
          status.textContent = field === 'budget'
            ? 'Anggaran harus bilangan bulat positif, maksimal 9 digit.'
            : 'Isi teks tanpa mengosongkan kolom.';
          input.focus();
          return;
        }
        closed = true;
        if (save) {
          data[row.dataset.record] ||= {};
          data[row.dataset.record][field] = value;
          button.dataset.value = value;
          button.textContent = label(field, value);
          status.textContent = `${row.dataset.record} berhasil diperbarui.`;
          persist();
        } else {
          button.dataset.value = original;
          button.textContent = label(field, original);
          status.textContent = 'Perubahan dibatalkan.';
        }
        editor.replaceWith(button);
        button.focus();
      };
      input.addEventListener('keydown', keyEvent => {
        if (keyEvent.key === 'Enter') { keyEvent.preventDefault(); close(true); }
        if (keyEvent.key === 'Escape') { keyEvent.preventDefault(); close(false); }
      });
      saveButton.addEventListener('click', () => close(true));
      cancelButton.addEventListener('click', () => close(false));
      editor.addEventListener('focusout', focusEvent => {
        if (!editor.contains(focusEvent.relatedTarget)) close(false);
      });
    });
    $('#editableReset').addEventListener('click', () => {
      data = {};
      try { localStorage.removeItem(key); } catch (_) { /* Ignore unavailable storage. */ }
      const input = table.querySelector('.editable-input');
      if (input) input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape' }));
      render();
      status.textContent = 'Data contoh dipulihkan.';
    });
  }
})();
