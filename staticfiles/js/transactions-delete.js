'use strict';

document.addEventListener('DOMContentLoaded', function (e) {
  (function () {
    const deleteButtons = document.querySelectorAll('.delete-transaction');
    deleteButtons.forEach(deleteButton => {
      deleteButton.addEventListener('click', function (e) {
        e.preventDefault();
        Swal.fire({
          title: 'Delete Transaction?',
          html: `<p class="text-danger">Are you sure you want to delete transaction of ?</p>`,
          icon: 'warning',
          showCancelButton: true,
          confirmButtonText: 'Delete',
          cancelButtonText: 'Cancel',
          customClass: {
            confirmButton: 'btn btn-primary waves-effect waves-light',
            cancelButton: 'btn btn-outline-secondary  waves-effect waves-light'
          }
        }).then(result => {
          if (result.isConfirmed) {
            window.location.href = this.getAttribute('href'); //redirect to herf
          } else {
            Swal.fire({
              title: 'Cancelled',
              html: `<p>Did not delete Transaction!</p>`,
              icon: 'error',
              confirmButtonText: 'Ok',
              customClass: {
                confirmButton: 'btn btn-success  waves-effect waves-light'
              }
            });
          }
        });
      });
    });
  })();
});
