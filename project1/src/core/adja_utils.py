# coding: utf-8
import time
from django.conf import settings
import jwt


# In django.VERSION >= (1, 10) user.is_authenticated is not callable anymore
def _is_authenticated(user):
    if callable(user.is_authenticated):
        return user.is_authenticated()
    return user.is_authenticated


def get_connection_parameters(user, info=''):
    timestamp = time.time()
    if _is_authenticated(user):
        user_pk = "0"
    else:
        user_pk = user.pk
    token = jwt.encode({
        "sub": str(user_pk),
    }, settings.CENTRIFUGE_SECRET, algorithm="HS256").decode()
    return {
        'sockjs_endpoint': settings.CENTRIFUGE_ADDRESS + '/connection',
        'ws_endpoint': settings.CENTRIFUGE_ADDRESS + '/connection/websocket',
        'user': user_pk,
        'timestamp': timestamp,
        'token': token,
        'info': info
    }
