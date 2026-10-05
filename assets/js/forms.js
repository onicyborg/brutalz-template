/* Phase 3 form demos. Each initializer runs only on its own page. */
(() => {
  'use strict';
  const $ = selector => document.querySelector(selector);

  if ($('#advancedForm')) {
    const form = $('#advancedForm');
    const team = $('#advancedTeam');
    const result = $('#advancedResult');
    window.jQuery(team).select2({ placeholder: 'Cari tim…', width: '100%', allowClear: true, language: { noResults: () => 'Tidak ada tim yang cocok.' } });
    window.jQuery('#advancedSkills').select2({ placeholder: 'Pilih keahlian…', width: '100%', language: { noResults: () => 'Tidak ada keahlian yang cocok.' } });
    document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(element => new bootstrap.Tooltip(element));
    const validateTeam = () => {
      const valid = Boolean(team.value);
      $('#advancedTeamError').classList.toggle('d-none', valid);
      window.jQuery(team).next('.select2-container').toggleClass('is-invalid', !valid);
      return valid;
    };
    window.jQuery(team).on('change', () => {
      if (form.classList.contains('was-validated')) validateTeam();
    });
    form.addEventListener('submit', event => {
      event.preventDefault();
      form.classList.add('was-validated');
      const teamValid = validateTeam();
      if (!form.checkValidity() || !teamValid) {
        result.textContent = 'Periksa kolom wajib sebelum melihat ringkasan.';
        const invalid = form.querySelector(':invalid');
        if (invalid === team) window.jQuery(team).select2('open');
        else invalid?.focus();
        return;
      }
      result.textContent = `Brief “${$('#advancedName').value.trim()}” untuk ${team.value} siap. Tidak ada data dikirim.`;
    });
    form.addEventListener('reset', () => {
      setTimeout(() => {
        window.jQuery('#advancedTeam, #advancedSkills').val(null).trigger('change');
        form.classList.remove('was-validated');
        $('#advancedTeamError').classList.add('d-none');
        window.jQuery(team).next('.select2-container').removeClass('is-invalid');
        result.textContent = '';
      }, 0);
    });
  }

  if ($('#editorSnow')) {
    const snow = new Quill('#editorSnow', {
      theme: 'snow',
      modules: { toolbar: [
        [{ header: [1, 2, 3, false] }],
        ['bold', 'italic', 'underline'],
        [{ list: 'ordered' }, { list: 'bullet' }],
        ['link', 'image', 'code-block'],
        ['clean'],
      ] },
    });
    new Quill('#editorBubble', {
      theme: 'bubble',
      modules: { toolbar: ['bold', 'italic', 'link'] },
    });
    document.querySelectorAll('.ql-picker-label').forEach(label => label.setAttribute('aria-label', 'Gaya teks'));
    $('#editorPreview').addEventListener('click', () => {
      const content = snow.getText().trim();
      $('#editorOutput').textContent = content || 'Editor masih kosong.';
      $('#editorStatus').textContent = `${content.length} karakter teks ditampilkan. Konten tidak disimpan.`;
    });
    $('#editorClear').addEventListener('click', () => {
      snow.setText('');
      $('#editorOutput').textContent = 'Editor masih kosong.';
      $('#editorStatus').textContent = 'Editor dikosongkan.';
      snow.focus();
    });
  }

  if ($('#validationForm')) {
    const form = $('#validationForm');
    const result = $('#validationResult');
    const fields = [...form.querySelectorAll('input')];
    const updateField = field => {
      field.classList.toggle('is-valid', field.checkValidity());
      field.classList.toggle('is-invalid', !field.checkValidity());
    };
    fields.forEach(field => {
      field.addEventListener('input', () => updateField(field));
      field.addEventListener('change', () => updateField(field));
    });
    form.addEventListener('submit', event => {
      event.preventDefault();
      fields.forEach(updateField);
      if (!form.checkValidity()) {
        result.textContent = 'Periksa kolom yang ditandai merah.';
        form.querySelector(':invalid')?.focus();
        return;
      }
      result.textContent = `Data ${$('#validationName').value.trim()} valid. Tidak ada data dikirim.`;
    });
    form.addEventListener('reset', () => {
      setTimeout(() => {
        fields.forEach(field => field.classList.remove('is-valid', 'is-invalid'));
        result.textContent = '';
      }, 0);
    });
  }

  if ($('#formWizard')) {
    const wizard = window.jQuery('#formWizard');
    const steps = [
      ['#wizardName', '#wizardPhone'],
      ['#wizardEmail', '#wizardRole'],
      ['#wizardAgree'],
      [],
    ];
    const validateStep = index => {
      const fields = steps[index].map(selector => $(selector));
      fields.forEach(field => {
        field.classList.toggle('is-invalid', !field.checkValidity());
        field.classList.toggle('is-valid', field.checkValidity());
      });
      const firstInvalid = fields.find(field => !field.checkValidity());
      if (firstInvalid) {
        $('#wizardStatus').textContent = 'Lengkapi kolom pada langkah ini sebelum lanjut.';
        firstInvalid.focus();
        return false;
      }
      $('#wizardStatus').textContent = '';
      return true;
    };
    const review = () => {
      [['#reviewName', '#wizardName'], ['#reviewPhone', '#wizardPhone'],
        ['#reviewEmail', '#wizardEmail'], ['#reviewRole', '#wizardRole']]
        .forEach(([output, input]) => { $(output).textContent = $(input).value; });
    };
    wizard.steps({
      headerTag: 'h3', bodyTag: 'section', transitionEffect: 'slideLeft',
      autoFocus: true, enableFinishButton: false,
      labels: { next: 'Lanjut', previous: 'Kembali', finish: 'Selesai' },
      onStepChanging: (_event, current, next) => {
        if (next < current) return true;
        if (!validateStep(current)) return false;
        if (next === 2) review();
        if (next === 3) $('#wizardStatus').textContent = 'Selesai! Tidak ada akun dibuat atau data dikirim.';
        return true;
      },
    });
    wizard[0].querySelectorAll('.actions ul[role="menu"], .actions a[role="menuitem"]').forEach(element => element.removeAttribute('role'));
    steps.flat().forEach(selector => {
      $(selector).addEventListener('input', event => event.target.classList.remove('is-invalid'));
      $(selector).addEventListener('change', event => event.target.classList.remove('is-invalid'));
    });
    $('#wizardRestart').addEventListener('click', () => {
      steps.flat().forEach(selector => {
        const field = $(selector);
        if (field.type === 'checkbox') field.checked = false;
        else field.value = '';
        if (field.tagName === 'SELECT') window.jQuery(field).trigger('change.select2');
        field.classList.remove('is-valid', 'is-invalid');
      });
      wizard.steps('previous');
      wizard.steps('previous');
      wizard.steps('previous');
      $('#wizardStatus').textContent = '';
    });
  }
})();
