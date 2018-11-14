# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Question, Answer
from likes.models import QuestionLike
from django import forms
from django.views.generic import UpdateView, CreateView
from django.http import JsonResponse
from jsonrpc import jsonrpc_method
from django.core.serializers import serialize
# from adjacent.utils import get_connection_parameters
# from adjacent.client import Client


class QuestionsListForm (forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'по имени'),
        ('-name', 'по имени в обратном'),
        ('id', 'по ID'),
        ('author', 'по автору')
    ), required=False, label='Сортировать')
    search = forms.CharField(required=False, label='Поиск')


def questions_list(request):

    questions = Question.objects.count_answers().filter(is_archive=False).select_related('author')
    form = QuestionsListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            questions = questions.order_by(data['sort'])
        if data['search']:
            questions = questions.filter(name__icontains=data['search'])
    context = {
        'questions': questions.count_answers,
        'question_form': form,
        # 'token': get_connection_parameters(request.user)['token'],
    }
    return render(request, 'questions/questions_list.html', context)


# @jsonrpc_method('api.questions_list')
# def questions_list(request):
#
#     questions = Question.objects.count_answers().filter(is_archive=False).select_related('author')
#     form = QuestionsListForm(request.GET)
#     if form.is_valid():
#         data = form.cleaned_data
#         if data['sort']:
#             questions = questions.order_by(data['sort'])
#         if data['search']:
#             questions = questions.filter(name__icontains=data['search'])
#     return JsonResponse({
#         'questions': serialize('json', questions),
#         # 'question_form': form
#     })


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = 'name',


def question_detail(request, pk=None):

    question = get_object_or_404(Question.objects.count_answers(), id=pk)
    context = {
        'question': question,
        # 'token': get_connection_parameters(request.user)['token'],
    }
    if request.method == 'GET':
        form = AnswerForm(initial={'author': request.user, 'question': question})
        context['form'] = form
        return render(request, 'questions/question_detail.html', context)
    elif request.method == 'POST' and request.user.id is not None:
        form = AnswerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            answer = Answer(author=request.user, question_id=question.pk, name=data['name'])
            answer.save()
            # client = Client()
            # client.publish("update_answers_{}".format(question.pk), {})
            # client.send()
            return redirect('questions:question_detail', pk=question.pk)
        else:
            context['form'] = form
            return render(request, 'questions/question_detail.html', context)


# @jsonrpc_method('api.question_detail')
# def question_detail(request, pk=None):
#
#     question = get_object_or_404(Question.objects.count_answers(), id=pk)
#     likes = QuestionLike.objects.filter(question=question)
#     context = {
#         'question': question,
#         'likes': likes.count(),
#     }
#     if request.user.id is not None and likes.filter(author=request.user).exists():
#         context['is_liked'] = True
#     else:
#         context['is_liked'] = False
#     if request.method == 'GET':
#         form = AnswerForm(initial={'author': request.user, 'question': question})
#         context['form'] = form
#     elif request.method == 'POST':
#         form = AnswerForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             answer = Answer(author=request.user, question_id=question.pk, name=data['name'])
#             answer.save()
#             return redirect('questions:question_detail', pk=question.pk)
#         else:
#             context['form'] = form
#     return JsonResponse({
#         'question': serialize('json', Question.objects.all().filter(id=pk)),
#         'likes': context['likes'],
#         'is_liked': context['is_liked']
#     })


def answer_detail(request, pk=None):

    answer = get_object_or_404(Answer, id=pk)
    context = {
        'answer': answer,
        'question': answer.question
    }
    return render(request, 'questions/answer_edit.html', context)


# @jsonrpc_method('api.answer_detail')
# def answer_detail(request, pk=None):
#
#     answer = get_object_or_404(Answer, id=pk)
#     return JsonResponse({
#         'answer': serialize('json', Answer.objects.all().filter(id=pk)),
#         'question': serialize('json', answer.question),
#     })


def question_file(request, pk=None):

    question = get_object_or_404(Question, id=pk)
    context = {
        'question': question,
    }
    return render(request, 'pieces/question_file.html', context)


# @jsonrpc_method('api.question_file')
# def question_file(request, pk=None):
#
#     question = get_object_or_404(Question, id=pk)
#     return JsonResponse({
#         'question': serialize('json', Question.objects.all().filter(id=pk))
#     })


def question_list_base(request):

    questions = Question.objects.all().filter(is_archive=False).select_related('author')
    context = {
        'questions': questions,
        # 'is_liked': QuestionLike.objects.filter(author=request.user),
        # 'token': get_connection_parameters(request.user)['token'],
    }
    return render(request, 'pieces/questions_list.html', context)


# @jsonrpc_method('api.question_list_base')
# def question_list_base(request):
#
#     questions = Question.objects.all().filter(is_archive=False).select_related('author')
#     context = {
#         'questions': serialize('json', questions),
#         'is_liked': serialize('json', QuestionLike.objects.filter(author=request.user))
#     }
#     return JsonResponse(context)


def answers_list(request, pk=None):

    context = {
        'answers': Answer.objects.all().filter(question_id=pk, is_archive=False).order_by('created'),
        # 'token': get_connection_parameters(request.user)['token'],
    }
    return render(request, 'pieces/answers_list.html', context)


# @jsonrpc_method('api.answers_list')
# def answers_list(request, pk=None):
#
#     return JsonResponse({
#         'answers': serialize('json',
#                              Answer.objects.all().filter(question_id=pk, is_archive=False).order_by('created')),
#     })


class QuestionAdd(CreateView):

    model = Question
    fields = 'name', 'text', 'categories'
    context_object_name = 'question'
    template_name = 'questions/question_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionAdd, self).form_valid(form)

    def get_success_url(self):
        # client = Client()
        # client.publish("update_questions_list", {})
        # client.send()
        return reverse('questions:question_detail', kwargs={'pk': self.object.pk})


class QuestionEdit(UpdateView):

    model = Question
    fields = 'name', 'text', 'categories'
    context_object_name = 'question'
    template_name = 'pieces/question_edit.html'

    def get_queryset(self):
        queryset = super(QuestionEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        # client = Client()
        # client.publish("update_questions_list", {})
        # client.publish("update_question_{}".format(self.object.pk), {})
        # client.send()
        return reverse('questions:question_detail', kwargs={'pk': self.object.pk})


class AnswerEdit(UpdateView):

    model = Answer
    fields = 'name', 'is_archive',
    context_object_name = 'answer'
    template_name = 'questions/answer_edit.html'

    def get_queryset(self):
        queryset = super(AnswerEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        # client = Client()
        # client.publish("update_answers_{}".format(self.object.question.pk), {})
        # client.send()
        return reverse('questions:question_detail', kwargs={'pk': self.object.question.id})

