jQuery(document).ready(function($) {
    $('select[name="categories"]').select2();
    new SimpleMDE({ element: $('#id_cooking_method')[0], forceSync: true });
    new SimpleMDE({ element: $('#id_description')[0], forceSync: true });

    $('.ingredients-list input[data-type="TOTAL_FORMS"]').val(
        $('.ingredients-list .form-row').length,
    );

    $('.ingredients-list input[data-type="INITIAL_FORMS"]').val(
        $('.ingredients-list .form-row').length,
    );

    validateIngredients();

    function validateIngredients() {
        var isValid =
            $('.ingredients-list input[type="text"][name*="name"]')
                .removeClass('is-invalid')
                .filter(function() {
                    return !this.value;
                })
                .addClass('is-invalid').length === 0;

        $('.ingredients-create').attr('disabled', !isValid);
        $('form button[type="submit"]').attr('disabled', !isValid);
    }

    function trashIconOnClick(event) {
        event.preventDefault();

        $(this)
            .parents('.form-row')
            .remove();

        if ($('.ingredients-list .form-row').length === 1) {
            $('.ingredients-list .form-row .fa-trash').hide();
        }

        $('.ingredients-list .form-row').each(function(rowIndex, rowElement) {
            $(rowElement)
                .find('input')
                .each(function(inputIndex, inputElement) {
                    var currentName = $(inputElement)
                        .attr('name')
                        .split('-');

                    currentName[1] = rowIndex;

                    $(inputElement).attr('name', currentName.join('-'));
                    $(inputElement).attr('id', 'id_' + currentName.join('-'));
                });
        });

        var $totalForms = $('.ingredients-list input[data-type="TOTAL_FORMS"]');
        $totalForms.val(parseInt($totalForms.val()) - 1);

        validateIngredients();
    }

    if ($('.ingredients-list .form-row').length === 1) {
        $('.ingredients-list .form-row .fa-trash').hide();
    }

    $('.ingredients-list input[type="text"]').on('change', function(event) {
        event.preventDefault();
        validateIngredients();
    });

    $('.ingredients-create').on('click', function(event) {
        event.preventDefault();

        var $cloned = $(this)
            .siblings('.ingredients-list')
            .find('.form-row:last')
            .clone()
            .find('input')
            .each(function(index, el) {
                $(el).val('');

                var currentName = $(el)
                    .attr('name')
                    .split('-');

                currentName[1] = parseInt(currentName[1]) + 1;

                $(el).attr('name', currentName.join('-'));
                $(el).attr('id', 'id_' + currentName.join('-'));
            })
            .end()
            .appendTo($(this).siblings('.ingredients-list'))
            .find('.fa-trash')
            .on('click', trashIconOnClick);

        if ($('.ingredients-list .form-row').length > 1) {
            $('.ingredients-list .form-row .fa-trash').show();
        }

        var $totalForms = $('.ingredients-list input[data-type="TOTAL_FORMS"]');
        $totalForms.val(parseInt($totalForms.val()) + 1);

        validateIngredients();

        $('.ingredients-list input[type="text"]').on('change', function(event) {
            event.preventDefault();
            validateIngredients();
        });
    });

    $('.fa-trash')
        .parent()
        .on('click', trashIconOnClick);
});
