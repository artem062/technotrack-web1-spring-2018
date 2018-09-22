# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from categories.models import Category
from questions.models import Question, Answer

# Create your models here.


class CategoryLike(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='category_like', verbose_name=u'Автор')
    category = models.ForeignKey(Category, blank=False, related_name='category_like', verbose_name=u'Категория')
    put = models.DateTimeField(auto_now=True, verbose_name=u'Поставлен')

    class Meta:
        verbose_name = u'Лайк категории'
        verbose_name_plural = u'Лайки категории'

    def __unicode__(self):
        return self.author.username


class QuestionLike(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='question_like', verbose_name=u'Автор')
    question = models.ForeignKey(Question, blank=False, related_name='question_like', verbose_name=u'Вопрос')
    put = models.DateTimeField(auto_now=True, verbose_name=u'Поставлен')

    class Meta:
        verbose_name = u'Лайк вопроса'
        verbose_name_plural = u'Лайки вопроса'

    def __unicode__(self):
        return self.author.username


class AnswerLike(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answer_like', verbose_name=u'Автор')
    answer = models.ForeignKey(Answer, blank=False, related_name='answer_like', verbose_name=u'Ответ')
    put = models.DateTimeField(auto_now=True, verbose_name=u'Поставлен')

    class Meta:
        verbose_name = u'Лайк ответа'
        verbose_name_plural = u'Лайки ответа'

    def __unicode__(self):
        return self.author.username
