# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Question, Answer
from django import forms
from django.views.generic import UpdateView, CreateView


def questions_list(request):

    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'questions/questions_list.html', context)


def question_detail(request, pk=None):

    question = get_object_or_404(Question, id=pk)
    context = {
        'question': question,
        'answers': question.answers.all().filter(is_archive=False)
    }
    return render(request, 'questions/question_detail.html', context)


def answer_detail(request, pk=None):

    answer = get_object_or_404(Answer, id=pk)
    context = {
        'answer': answer,
        'question': answer.question
    }
    return render(request, 'questions/answer_page.html', context)


class QuestionAdd(CreateView):

    model = Question
    fields = 'name', 'text'
    context_object_name = 'question'
    template_name = 'questions/question_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionAdd, self).form_valid(form)

    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.object.pk})


class QuestionEdit(UpdateView):

    model = Question
    fields = 'name', 'text'
    context_object_name = 'question'
    template_name = 'questions/question_edit.html'

    def get_queryset(self):
        queryset = super(QuestionEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.object.pk})


def answer_add(request, pk=None):

    context = {
        'question': Question.objects.get(id=pk),
    }
    return render(request, 'questions/answer_add.html', context)