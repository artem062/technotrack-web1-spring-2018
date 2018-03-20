from django.conf.urls import url
from questions.views import question_detail, questions_list, question_add, answer_add

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', question_detail, name='question_detail'),
    url(r'^$', questions_list, name='questions_list'),
    url(r'^add/(?P<pk>\d+)/$', question_add, name='questions_add'),
    url(r'^add_answer/(?P<pk>\d+)/$', answer_add, name='answer_add'),

]