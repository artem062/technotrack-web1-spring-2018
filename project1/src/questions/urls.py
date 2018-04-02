from django.conf.urls import url
from questions.views import question_detail, questions_list, question_edit, question_add, answer_add, answer_detail

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', question_detail, name='question_detail'),
    url(r'^$', questions_list, name='questions_list'),
    url(r'^add/(?P<pk>\d+)/$', question_add, name='question_add'),
    url(r'^edit/(?P<pk>\d+)/$', question_edit, name='question_edit'),
    url(r'^add_answer/(?P<pk>\d+)/$', answer_add, name='answer_add'),
    url(r'^answer/(?P<pk>\d+)/$', answer_detail, name='answer_detail'),
]