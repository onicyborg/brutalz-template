/* Phase 2 demo behavior. No modal, notification, or file demo sends data to a server. */
(() => {
  'use strict';

  const page = document.body.dataset.page;
  const select = selector => document.querySelector(selector);

  if (page === 'modal') {
    select('#advancedModalForm').addEventListener('submit', event => {
      event.preventDefault();
      const input = select('#modalIdea');
      const idea = input.value.trim();
      if (!idea) {
        input.setCustomValidity('Isi judul ide.');
        input.reportValidity();
        return;
      }
      input.setCustomValidity('');
      select('#modalFormResult').textContent = `Ide “${idea}” disimpan sementara di halaman ini.`;
      event.target.reset();
      bootstrap.Modal.getInstance(select('#modalForm')).hide();
    });
    select('#modalIdea').addEventListener('input', event => event.target.setCustomValidity(''));
    select('#confirmModalDelete').addEventListener('click', () => {
      select('#deleteDemoItem').hidden = true;
      select('#deleteModalResult').textContent = 'Item contoh dihapus sampai halaman dimuat ulang.';
      bootstrap.Modal.getInstance(select('#modalDelete')).hide();
    });
  }

  if (page === 'sweet-alert') {
    const messages = {
      success: {icon:'success', title:'Berhasil!', text:'Ide demo berhasil disimpan.'},
      error: {icon:'error', title:'Ada kendala', text:'Contoh error: perubahan belum dapat disimpan.'},
      warning: {icon:'warning', title:'Perlu perhatian', text:'Periksa kembali sebelum melanjutkan.'},
      info: {icon:'info', title:'Tahukah kamu?', text:'Dialog ini berasal dari SweetAlert2 lokal.'},
      confirm: {icon:'question', title:'Lanjutkan tindakan demo?', text:'Tidak ada data nyata yang akan diubah.', showCancelButton:true, confirmButtonText:'Ya, lanjutkan', cancelButtonText:'Batal'},
      custom: {title:'Checklist kecil', html:'<p>Jaga fokus pada hal yang penting.</p><ul class="text-start"><li>Tujuan jelas</li><li>Umpan balik cepat</li><li>Langkah berikutnya</li></ul>', confirmButtonText:'Siap!'},
      toast: {toast:true, position:'top-end', icon:'success', title:'Progres kecil tetap berarti.', showConfirmButton:false, timer:3000, timerProgressBar:true},
    };
    document.addEventListener('click', async event => {
      const trigger = event.target.closest('[data-swal-demo]');
      if (!trigger) return;
      const kind = trigger.dataset.swalDemo;
      const result = await Swal.fire(messages[kind]);
      if (kind === 'confirm') {
        select('#sweetAlertResult').textContent = result.isConfirmed
          ? 'Tindakan demo dikonfirmasi.' : 'Tindakan demo dibatalkan.';
      }
    });
  }

  if (page === 'toastr') {
    toastr.options = {
      closeButton:true,
      progressBar:true,
      timeOut:4500,
      extendedTimeOut:1000,
      positionClass:'toast-top-right',
      newestOnTop:true,
      preventDuplicates:false,
    };
    const messages = {
      success:['Perubahan demo berhasil disimpan.', 'Berhasil'],
      info:['Ada catatan baru untuk tim kreatif.', 'Informasi'],
      warning:['Periksa kembali detail sebelum lanjut.', 'Peringatan'],
      error:['Contoh kegagalan lokal, tanpa permintaan server.', 'Error'],
    };
    document.addEventListener('click', event => {
      const trigger = event.target.closest('[data-toastr-demo]');
      if (!trigger) return;
      toastr.options.positionClass = select('#toastrPosition').value;
      const [message, title] = messages[trigger.dataset.toastrDemo];
      toastr[trigger.dataset.toastrDemo](message, title);
    });
    select('#toastrPosition').addEventListener('change', () => toastr.remove());
    select('#toastrClear').addEventListener('click', () => toastr.clear());
  }

  if (page === 'empty-state') {
    select('#emptyAdd').addEventListener('click', () => {
      select('#emptyDemo').innerHTML = '<div class="list-group"><div class="list-group-item d-flex justify-content-between align-items-center"><strong>Ide pertama: coba sesuatu yang baru</strong><span class="badge bg-green">Aktif</span></div></div>';
      select('#emptyAdd').hidden = true;
      select('#emptyReset').hidden = false;
    });
    select('#emptyReset').addEventListener('click', () => {
      select('#emptyDemo').innerHTML = '<div class="advanced-empty compact"><span class="empty-symbol" aria-hidden="true">✳</span><h3>Daftar ide masih kosong.</h3><p class="text-muted">Tambahkan contoh untuk melihat keadaan berisi.</p></div>';
      select('#emptyAdd').hidden = false;
      select('#emptyReset').hidden = true;
    });
  }

  if (page === 'multiple-upload') {
    Dropzone.autoDiscover = false;
    const zone = new Dropzone('#uploadDropzone', {
      url:'/upload-disabled',
      autoProcessQueue:false,
      maxFiles:5,
      maxFilesize:5,
      acceptedFiles:'image/*,.pdf',
      addRemoveLinks:true,
      dictRemoveFile:'Hapus file',
      dictInvalidFileType:'Pilih gambar atau PDF.',
      dictFileTooBig:'File terlalu besar (maksimal 5 MB).',
      dictMaxFilesExceeded:'Maksimal 5 file.',
    });
    const summary = select('#uploadSummary');
    const clear = select('#uploadClear');
    function updateSummary() {
      const count = zone.files.filter(file => file.accepted && file.status !== Dropzone.CANCELED).length;
      summary.textContent = count ? `${count} file ditinjau lokal. Tidak ada upload ke server.` : 'Belum ada file dipilih.';
      clear.disabled = zone.files.length === 0;
    }
    zone.on('addedfile', file => queueMicrotask(() => {
      updateSummary();
      if (!file.accepted || !file.previewElement) return;
      const status = document.createElement('span');
      status.className = 'upload-read-status';
      status.textContent = 'Menyiapkan pratinjau 0%';
      file.previewElement.append(status);
      const progress = file.previewElement.querySelector('.dz-upload');
      const reader = new FileReader();
      reader.onprogress = event => {
        if (!event.lengthComputable) return;
        const percent = Math.round(event.loaded / event.total * 100);
        status.textContent = `Menyiapkan pratinjau ${percent}%`;
        if (progress) progress.style.width = `${percent}%`;
      };
      reader.onload = () => {
        status.textContent = 'Pratinjau siap · tidak diunggah';
        if (progress) progress.style.width = '100%';
      };
      reader.onerror = () => { status.textContent = 'File tidak dapat dibaca.'; };
      reader.readAsArrayBuffer(file);
    }));
    zone.on('removedfile', updateSummary);
    zone.on('error', updateSummary);
    clear.addEventListener('click', () => zone.removeAllFiles(true));
  }
})();
