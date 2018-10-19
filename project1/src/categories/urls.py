from django.conf.urls import url
from .views import category_detail, category_list

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', category_detail, name='category_detail'),
    url(r'$', category_list, name='categories_list'),
]
