$(document).ready(
    function () {
        $('.autoload').each(function () {
            $(this).load($(this).data('url'));
        });

        var update = true;

        window.setInterval(function () {
                $('.autoload').each(function () {
                    $(this).load($(this).data('url'));
                });
                if (update) {
                    $('.editform').each(function () {
                        $(this).load($(this).data('url'));
                    });
                }
            },
            2000
        );

        $('.editform').each(function () {
            $(this).load($(this).data('url'));
        });

        $(document).on('submit', '.ajaxform', function () {
            $.post(
                $(this).data('url'),
                $(this).serialize()
            );
            if ($(this).data('clear')) {
                $(this.name).val('')
            }
            return false
        });

        $(document).on('submit', '.edited', function () {
             $.post(
                $(this).data('url'),
                $(this).serialize()
            );
             update = false;
            $('.editform').each(function () {
                $(this).load($(this).data('editurl'));
            });
            return false
        });

        $(document).on('submit', '.saveform', function () {
            $.post(
                $(this).data('url'),
                $(this).serialize()
            );
            update = true;
            return false
        });


        $('#categories').chosen({rtl: true})
    }
);