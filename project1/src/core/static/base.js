$(document).ready(
    function () {
        const centrifugo_url = 'wss://voronov.chickenkiller.com/connection/websocket';

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

        $('.load_now').each(function () {
            $(this).load($(this).data('url'));
        });

        $('.autoload').each(function () {
            $(this).load($(this).data('url'));
        });

        window.setInterval(function () {
                $('.autoload').each(function () {
                    $(this).load($(this).data('url'));
                });
            },
            2000
        );

        $('.editform').each(function () {
            const obj = $(this);
            obj.load(obj.data('url'));
            const centrifuge = new Centrifuge(centrifugo_url);
            centrifuge.setToken(obj.data('token'));
            centrifuge.subscribe(`update_question`, function () {
                if (update) {
                    obj.load(obj.data('url'));
                }
            });
            centrifuge.connect();
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
            const centrifuge = new Centrifuge(centrifugo_url);
            centrifuge.setToken(obj.data('token'));
            centrifuge.subscribe(`add_answer`, function () {
                obj.load(obj.data('url'));
            });
            centrifuge.subscribe(`update_answer`, function () {
                obj.load(obj.data('url'));
            });
            centrifuge.connect();
        });

        $('.like').each(function () {
            const obj = $(this);
            obj.load(obj.data('url'));
            const centrifuge = new Centrifuge(centrifugo_url);
            centrifuge.setToken(obj.data('token'));
            centrifuge.subscribe(`update_question_like_${obj.data('pk')}`, function () {
                obj.load(obj.data('url'));
            });
            centrifuge.connect();
        });

        $('.question_list').each(function () {
            const obj = $(this);
            obj.load(obj.data('url'));
            const centrifuge = new Centrifuge(centrifugo_url);
            centrifuge.setToken(obj.data('token'));
            centrifuge.subscribe(`add_question`, function () {
                obj.load(obj.data('url'));
            });
            centrifuge.subscribe(`update_question`, function () {
                obj.load(obj.data('url'));
            });
            centrifuge.connect();
        });
    }
);
