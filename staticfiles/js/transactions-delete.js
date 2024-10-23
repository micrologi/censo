'use strict';

document.addEventListener('DOMContentLoaded', function (e) {
  (function () {
    const deleteButtons = document.querySelectorAll('.delete-transaction');
    deleteButtons.forEach(deleteButton => {
      deleteButton.addEventListener('click', function (e) {
        e.preventDefault();
        Swal.fire({
          title: 'Deletar Registro?',
          html: `<p class="text-danger">Confirma a deleção deste registro?</p>`,
          icon: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Sim, deletar!',
          cancelButtonText: 'Não, cancelar.',
          customClass: {
            confirmButton: 'btn btn-primary waves-effect waves-light',
            cancelButton: 'btn btn-outline-secondary  waves-effect waves-light'
          }
        }).then(result => {
          if (result.isConfirmed) {
            window.location.href = this.getAttribute('href'); //redirect to herf
          }
        });
      });
    });
  })();
});
