from django.conf.urls import include, url
from core.views import page, register, Login, Logout

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^$', page, name='main'),
]
