jQuery(document).ready(function($) {
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
                });
        });
    }

    if ($('.ingredients-list .form-row').length === 1) {
        $('.ingredients-list .form-row .fa-trash').hide();
    }

    $('.ingredients-create').on('click', function(event) {
        event.preventDefault();

        var $cloned = $(this)
            .siblings('.ingredients-list')
            .find('.form-row:last')
            .clone();

        $cloned.find('input').each(function(index, el) {
            var currentName = $(el)
                .attr('name')
                .split('-');

            currentName[1] = parseInt(currentName[1]) + 1;

            $(el).attr('name', currentName.join('-'));
        });

        $cloned.appendTo($(this).siblings('.ingredients-list'));

        if ($('.ingredients-list .form-row').length > 1) {
            $('.ingredients-list .form-row .fa-trash').show();
        }

        $cloned.find('.fa-trash').on('click', trashIconOnClick);
    });

    $('.fa-trash')
        .parent()
        .on('click', trashIconOnClick);
});
