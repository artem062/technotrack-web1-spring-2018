from django.conf.urls import url
from questions.views import question_detail, questions_list, QuestionEdit, \
    QuestionAdd, answer_detail, AnswerEdit, answers_list, question_file, question_list_base
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', question_detail, name='question_detail'),
    url(r'^$', questions_list, name='questions_list'),
    url(r'^base$', question_list_base, name='questions_list_base'),
    url(r'^add/$', login_required(QuestionAdd.as_view()), name='question_add'),
    url(r'^edit/(?P<pk>\d+)/$', QuestionEdit.as_view(), name='question_edit'),
    url(r'^answer/(?P<pk>\d+)/$', answer_detail, name='answer_detail'),
    url(r'^file/(?P<pk>\d+)/$', question_file, name='question_file'),
    url(r'^answer/edit/(?P<pk>\d+)/$', AnswerEdit.as_view(), name='answer_edit'),
    url(r'^answers_list/(?P<pk>\d+)/$', answers_list, name='answers_list'),
]
