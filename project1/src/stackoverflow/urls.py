from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls', namespace='core')),
    url(r'^category/', include('categories.urls', namespace='categories')),
    url(r'^question/', include('questions.urls', namespace='questions')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^debug/', include(debug_toolbar.urls)),
    ] + urlpatterns
