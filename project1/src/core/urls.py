from django.conf.urls import url
from jsonrpc.site import jsonrpc_site
from core.views import page, register, Login, Logout, profile, search
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^search/$', search, name='search'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^profile/$', login_required(profile), name='profile'),
    url(r'^$', page, name='main'),
    url(r'^api/$', jsonrpc_site.dispatch, name='api'),
]
