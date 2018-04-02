# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Question, Answer
from categories.models import Category
from django import forms


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


class QuestionAddForm (forms.Form):

    name = forms.CharField(required=True)
    text = forms.CharField(required=False)


def question_add(request, pk=None):

    if request.method == 'GET':
        form = QuestionAddForm()
        context = {
            'category': Category.objects.get(id=pk),
            'question_form': form
        }
        return render(request, 'questions/question_add.html', context)
    elif request.method == 'POST':
        form = QuestionAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_question = Question(name=data['name'], text=data['text'])
            new_question.author = request.user
            new_question.save()
            new_question.categories = Category.objects.get(id=pk),
            new_question.save()
            return redirect('questions:question_detail', pk=new_question.id)
        else:
            context = {
                'category': Category.objects.get(id=pk),
                'question_form': form
            }
            return render(request, 'questions/question_add.html', context)


def question_edit(request, pk=None):

    question = get_object_or_404(Question, id=pk)

    if request.method == 'GET':
        form = QuestionAddForm(initial={'name': question.name, 'text': question.text})
        return render(request, 'questions/question_edit.html', {'question': question, 'question_form': form})
    elif request.method == 'POST':
        form = QuestionAddForm(request.POST, initial={'name': question.name, 'text': question.text})
        if form.is_valid():
            question.name = form.cleaned_data['name']
            question.text = form.cleaned_data['text']
            question.save()
            return redirect('questions:question_detail', pk=question.id)
        else:
            return render(request, 'questions/question_detail.html', {'question': question, 'question_form': form})


def answer_add(request, pk=None):

    context = {
        'question': Question.objects.get(id=pk),
    }
    return render(request, 'questions/answer_add.html', context)