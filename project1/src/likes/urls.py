from django.conf.urls import include, url
from likes.views import question_like
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^question_like/(?P<pk>\d+)/$', question_like, name='question_like'),
]

