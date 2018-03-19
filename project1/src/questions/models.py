# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from categories.models import Category


class Question(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='questions', verbose_name=u'Автор')
    categories = models.ManyToManyField(Category, blank=True, related_name='questions', verbose_name=u'Категории')
    name = models.CharField(max_length=255, verbose_name=u'Вопрос')
    is_archive = models.BooleanField(default=False, verbose_name=u'в архиве')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'Обновлено')

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name


class Answer(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answers', verbose_name=u'Автор')
    question = models.ForeignKey(Question,  related_name='answers', verbose_name=u'Вопрос')
    name = models.CharField(max_length=255, verbose_name=u'Ответ')
    is_archive = models.BooleanField(default=False, verbose_name=u'в архиве')
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name=u'Обновлено')

    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'
        ordering = 'name', 'question', 'id'

    def __unicode__(self):
        return self.name
