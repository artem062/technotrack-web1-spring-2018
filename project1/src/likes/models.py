# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from categories.models import Category
from questions.models import Question, Answer

# Create your models here.


class Like(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', verbose_name=u'Автор')
    categories = models.ForeignKey(Category, blank=False, related_name='likes', verbose_name=u'Категория')
    question = models.ForeignKey(Question, blank=False, related_name='likes', verbose_name=u'Вопрос')
    answer = models.ForeignKey(Answer, blank=False, related_name='likes', verbose_name=u'Ответ')
    put = models.DateTimeField(auto_now=True, verbose_name=u'Обновлено')

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'

    def __unicode__(self):
        return self.name
