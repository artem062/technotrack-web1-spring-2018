# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .models import Question, Answer
from django import forms
from django.views.generic import UpdateView, CreateView


class QuestionsListForm (forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'по имени'),
        ('-name', 'по имени в обратном'),
        ('id', 'по ID'),
        ('author', 'по автору')
    ), required=False, label='Сортировать')
    search = forms.CharField(required=False, label='Поиск')


def questions_list(request):

    questions = Question.objects.all()
    form = QuestionsListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            questions = questions.order_by(data['sort'])
        if data['search']:
            questions = questions.filter(name__icontains=data['search'])
    context = {
        'questions': questions,
        'question_form': form
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
        'answers': question.answers.all().filter(is_archive=False).order_by('created'),
    }
    if request.method == 'GET':
        form = AnswerForm(initial={'author': request.user, 'question': question})
        context['form'] = form
        return render(request, 'questions/question_detail.html', context)
    elif request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            answer = Answer(author=request.user, question_id=question.pk, name=data['name'])
            answer.save()
            return redirect('questions:question_detail', pk=question.pk)
        else:
            context['form'] = form
            return render(request, 'questions/question_detail.html', context)


def answer_detail(request, pk=None):

    answer = get_object_or_404(Answer, id=pk)
    context = {
        'answer': answer,
        'question': answer.question
    }
    return render(request, 'questions/answer_edit.html', context)


class QuestionAdd(CreateView):

    model = Question
    fields = 'name', 'text', 'categories'
    context_object_name = 'question'
    template_name = 'questions/question_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionAdd, self).form_valid(form)

    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.object.pk})


class QuestionEdit(UpdateView):

    model = Question
    fields = 'name', 'text', 'categories'
    context_object_name = 'question'
    template_name = 'questions/question_edit.html'

    def get_queryset(self):
        queryset = super(QuestionEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.object.pk})


class AnswerEdit(UpdateView):

    model = Answer
    fields = 'name',
    context_object_name = 'answer'
    template_name = 'questions/answer_edit.html'

    def get_queryset(self):
        queryset = super(AnswerEdit, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_success_url(self):
        return reverse('questions:question_detail', kwargs={'pk': self.object.question.id})
