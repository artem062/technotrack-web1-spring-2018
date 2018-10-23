# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Category, Question, Answer, CategoryLike, QuestionLike, AnswerLike
from django.views.generic import CreateView
from django.views import View
from django import forms
from django.db import models
from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404, HttpResponse, redirect

# Create your views here.


class QuestionLikeForm(forms.ModelForm):

    class Meta:
        model = QuestionLike
        fields = 'author', 'question'


def question_like(request, pk=None):

    question = get_object_or_404(Question, id=pk)
    likes = QuestionLike.objects.filter(question=question)
    context = {
        'question': question,
        'likes': likes.count(),
    }
    if request.user.id is not None and likes.filter(author=request.user).exists():
        context['is_liked'] = True
    else:
        context['is_liked'] = False
    if request.method == 'GET':
        form = QuestionLikeForm(initial={'author': request.user, 'question': question})
        context['form'] = form
        return render(request, 'question_like.html', context)
    elif request.method == 'POST' and request.user.id is not None:
        form = QuestionLikeForm(request.POST)
        if form.is_valid():
            thislike = QuestionLike.objects.filter(question=question, author=request.user)
            questionSet = Question.objects.filter(id=pk)
            if thislike.exists():
                questionSet.update(likes_count=models.F('likes_count') - 1)
                thislike.delete()
            else:
                questionSet.update(likes_count=models.F('likes_count') + 1)
                QuestionLike(author=request.user, question_id=question.pk).save()
            return redirect('likes:question_like', pk=question.pk)
        else:
            context['form'] = form
            return render(request, 'question_like.html', context)


# def question_like_json(request, pk=None):
#
#     question = get_object_or_404(Question, id=pk)
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
#         form = QuestionLikeForm(initial={'author': request.user, 'question': question})
#         context['form'] = form
#         return JsonResponse(context)
#     elif request.method == 'POST' and request.user.id is not None:
#         form = QuestionLikeForm(request.POST)
#         if form.is_valid():
#             thislike = QuestionLike.objects.filter(question=question, author=request.user)
#             questionSet = Question.objects.filter(id=pk)
#             if thislike.exists():
#                 questionSet.update(likes_count=models.F('likes_count') - 1)
#                 thislike.delete()
#             else:
#                 questionSet.update(likes_count=models.F('likes_count') + 1)
#                 QuestionLike(author=request.user, question_id=question.pk).save()
#             return redirect('likes:question_like', pk=question.pk)
#         else:
#             context['form'] = form
#             return JsonResponse(context)

# class QuestionLikeAjaxView(CreateView):
#
#     model = QuestionLike
#     fields = 'author', 'question'
#     context_object_name = 'question_like'
#     template_name = 'question_like.html'
#
#     def dispatch(self, request, pk=None, *args, **kwargs):
#         self.question = get_object_or_404(Question, id=pk)
#         return super(QuestionLikeAjaxView, self).dispatch(request, *args, **kwargs)
#
#     def question(self):
#         if not QuestionLike.objects.filter(user=self.request.user, question=self.question).exists():
#             return HttpResponse(QuestionLike.objects.filter(question=self.question).count())
