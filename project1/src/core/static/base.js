$(document).ready(
    function () {
        $('.autoload').each(function () {
            $(this).load($(this).data('url'));
        });

        $('.load_now').each(function () {
            $(this).load($(this).data('url'));
        });

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });

        let update = true;

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
                $(this).load($(this).data('editurl'), function () {
                   $('#id_categories').chosen({rtl: true})
                });
            })
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

        $('.answers').each(function () {
            const obj = $(this);
            obj.load(obj.data('url'));
            const centrifuge = new Centrifuge('http://localhost:8080/connection/sockjs');
            centrifuge.setToken(obj.data('token'));
            centrifuge.subscribe('update_answers', function (message) {
                if (obj.data('pk') === message.data.answers) {
                    obj.load(obj.data('url'));
                }
            });
            centrifuge.connect();
        });
    }
);
