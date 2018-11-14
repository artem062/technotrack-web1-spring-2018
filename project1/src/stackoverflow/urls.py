from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^category/', include('categories.urls', namespace='categories')),
    url(r'^question/', include('questions.urls', namespace='questions')),
    url(r'^likes/', include('likes.urls', namespace='likes')),
    url('', include('social_django.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^debug/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += staticfiles_urlpatterns()
