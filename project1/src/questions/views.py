# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Question, Answer
from likes.models import QuestionLike
from django import forms
from django.views.generic import UpdateView, CreateView
from django.http import JsonResponse
from django.core.serializers import serialize
from core.adja_utils import get_connection_parameters
from core.models import User
from adjacent.client import Client
from django.views.decorators.csrf import csrf_exempt
import json


class QuestionsListForm (forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'по имени'),
        ('-name', 'по имени в обратном'),
        ('id', 'по ID'),
        ('author', 'по автору')
    ), required=False, label='Сортировать')
    search = forms.CharField(required=False, label='Поиск')


def questions_list(request):

    questions = Question.objects.count_answers().filter(is_archive=False)
    # form = QuestionsListForm(request.GET)
    # if form.is_valid(): TODO sorting in question_list
    #     data = form.cleaned_data
    #     if data['sort']:
    #         questions = questions.order_by(data['sort'])
    #     if data['search']:
    #         questions = questions.filter(name__icontains=data['search'])
    context = {
        'questions': questions.count_answers,
        # 'question_form': form,
        'token': get_connection_parameters(request.user)['token'],
    }
    return render(request, 'questions/questions_list.html', context)


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = 'name',


def question_detail(request, pk=None):

    question = get_object_or_404(Question, id=pk)
    context = {
        'question': question,
        'token': get_connection_parameters(request.user)['token'],
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
            client = Client()
            client.publish("add_answer", {
                'question_id': question.pk,
                'name': data['name']
            })
            client.send()
            return redirect('questions:question_detail', pk=question.pk)
        else:
            context['form'] = form
            return render(request, 'questions/question_detail.html', context)


def answer_detail(request, pk=None):

    answer = get_object_or_404(Answer, id=pk)
    context = {
        'answer': answer,
        'question': answer.question.values('id', 'name')
    }
    return render(request, 'questions/answer_edit.html', context)


def js_answer_detail(request, pk=None):

    return JsonResponse({
        'answers': serialize('json', Answer.objects.filter(question_id=pk).order_by('created'))
    })


def question_file(request, pk=None):

    question = get_object_or_404(Question, id=pk)
    context = {
        'question': question,
    }
    return render(request, 'pieces/question_file.html', context)


def question_list_base(request):
    questions = Question.objects.filter(is_archive=False).select_related('author')
    context = {
        'questions': questions,
    }
    return render(request, 'pieces/questions_list.html', context)


def js_question_list_base(request):
    questions = Question.objects.all().filter(is_archive=False)
    context = {
       'questions': serialize('json', questions),
    }
    return JsonResponse(context)


def answers_list(request, pk=None):

    context = {
        'answers': Answer.objects.all().filter(question_id=pk, is_archive=False).order_by('created').select_related('author'),
        'token': get_connection_parameters(request.user)['token'],
    }
    return render(request, 'pieces/answers_list.html', context)


class QuestionAdd(CreateView):

    model = Question
    fields = 'name', 'text', 'categories'
    context_object_name = 'question'
    template_name = 'questions/question_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionAdd, self).form_valid(form)

    def get_success_url(self):
        client = Client()
        client.publish("add_question", {
            'id': self.object.pk,
            'name': self.object.name,
            'text': self.object.text,
        })
        client.send()
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
        client = Client()
        client.publish("update_question", {
            'id': self.object.pk,
            'name': self.object.name,
            'text': self.object.text,
        })
        client.send()
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
        client = Client()
        client.publish("update_answer", {
            'question_id': self.object.question.pk,
            'name': self.object.name
        })
        client.send()
        return reverse('questions:question_detail', kwargs={'pk': self.object.question.id})


@csrf_exempt
def js_add_question(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['token']
        name = data['topic']
        text = data['text']

        quest = Question(name=name, text=text, author=get_object_or_404(User, username=username))
        quest.save()

        return JsonResponse({'id': quest.pk, 'status': 'Получено'})


@csrf_exempt
def js_add_answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['token']
        quest = data['question_id']
        text = data['text']

        answer = Answer(name=text, author=get_object_or_404(User, username=username), question_id=quest)
        answer.save()

        return JsonResponse({'status': 'Получено'})
