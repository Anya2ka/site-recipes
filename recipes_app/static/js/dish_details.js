jQuery(document).ready(function($) {
    $('.remove-item').on('click', function(event) {
        event.preventDefault();
        Swal.fire({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Yes, delete it!',
        }).then(result => {
            if (result.value) {
                $.ajax({
                    url: window.location.pathname,
                    method: 'DELETE',
                    statusCode: {
                        404: function() {
                            Swal.fire('Error!', 'Dish not found', 'error');
                        },
                    },
                }).done(function(data) {
                    Swal.fire('Deleted!', data.message, 'success').then(() => {
                        window.location.href = '/';
                    });
                });
            }
        });
    });
});
