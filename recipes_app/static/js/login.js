$(function() {
    $('.openSigninModal').click(function(event) {
        event.preventDefault();
        $('#signinModal').modal('show');
    });

    $('#signinModal button[type="submit"]').on('click', function(event) {
        event.preventDefault();
        var username = $('#signinModal #id_username').val();
        var password = $('#signinModal #id_password').val();

        $.ajax({
            url: '/login/',
            method: 'POST',
            data: {
                username: username,
                password: password,
            },
        }).done(function(data) {
            if (data.ok) {
                window.location.reload();
            } else {
                Swal.fire('Error!', 'Invalid credentials', 'warning');
            }
        });
    });
});
