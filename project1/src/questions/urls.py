from django.conf.urls import url
from questions.views import question_detail, questions_list, QuestionEdit, QuestionAdd, answer_add, answer_detail
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', question_detail, name='question_detail'),
    url(r'^$', questions_list, name='questions_list'),
    url(r'^add/(?P<pk>\d+)/$', login_required(QuestionAdd.as_view()), name='question_add'),
    url(r'^edit/(?P<pk>\d+)/$', QuestionEdit.as_view(), name='question_edit'),
    url(r'^add_answer/(?P<pk>\d+)/$', answer_add, name='answer_add'),
    url(r'^answer/(?P<pk>\d+)/$', answer_detail, name='answer_detail'),
]