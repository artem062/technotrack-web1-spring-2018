from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url
from questions.views import answer_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('core.urls')),
    url(r'^category/', include('categories.urls')),
    url(r'^question/', include('questions.urls')),
    url(r'^answer/(?P<pk>\d+)/$', answer_detail, name='answer_detail'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^debug/', include(debug_toolbar.urls)),
    ] + urlpatterns
