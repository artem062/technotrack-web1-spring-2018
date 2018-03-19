from django.conf.urls import include, url
from core.views import page, login, logout, register

urlpatterns = [
    url(r'^register$', register, name='register'),
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^$', page),
]
