# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Question, Answer


def questions_list(request):

    context = {
        'questions': Question.objects.all()
    }
    return render(request, 'questions/questions_list.html', context)


def question_detail(request, pk=None):

    question = Question.objects.get(id=pk)
    context = {
        'question': question,
        'answers': question.answers.all().filter(is_archive=False)
    }
    return render(request, 'questions/question_detail.html', context)


def answer_detail(request, pk=None):

    answer = Answer.objects.get(id=pk)
    context = {
        'answer': answer,
        'question': answer.question
    }
    return render(request, 'questions/answer_page.html', context)
