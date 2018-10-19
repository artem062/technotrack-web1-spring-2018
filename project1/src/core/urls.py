from django.conf.urls import include, url
from jsonrpc import jsonrpc_site
from core.views import page, register, Login, Logout, profile, search, upload_file
from django.contrib.auth.decorators import login_required
from oauthlib.uri_validate import path

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^search/$', search, name='search'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^profile/$', login_required(profile), name='profile'),
    url(r'^$', page, name='main'),
    url(r'^api/$', jsonrpc_site.dispatch, name='api'),
]
