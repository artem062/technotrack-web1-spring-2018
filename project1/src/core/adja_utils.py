import time
from django.conf import settings
import jwt


def get_connection_parameters(user, info=''):
    timestamp = int(time.time())
    user_pk = str(user.pk) if user.is_authenticated() else ""
    token = jwt.encode({
        "sub": str(user.pk),
        "exp": timestamp + settings.CENTRIFUGE_TIMEOUT * 60,
    }, settings.CENTRIFUGE_SECRET, algorithm="HS256").decode()

    return {
        'sockjs_endpoint': settings.CENTRIFUGE_ADDRESS + '/connection',
        'ws_endpoint': settings.CENTRIFUGE_ADDRESS + '/connection/websocket',
        'user': user_pk,
        'timestamp': timestamp,
        'token': token,
        'info': info
    }
