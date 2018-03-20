# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Question, Answer
from categories.models import Category


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


def question_add(request, pk=None):

    context = {
        'category': Category.objects.get(id=pk),
    }

    return render(request, 'questions/question_add.html', context)


def answer_add(request, pk=None):

    context = {
        'question': Question.objects.get(id=pk),
    }
    return render(request, 'questions/answer_add.html', context)