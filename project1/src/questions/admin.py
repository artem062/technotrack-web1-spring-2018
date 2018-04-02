# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = 'name', 'author', 'created', 'updated', 'is_archive', 'text'
    search_fields = 'name', 'author__username', 'text'
    list_filter = 'is_archive',
    raw_id_fields = 'author',
    filter_horizontal = 'categories',


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    list_display = 'name', 'question', 'author', 'created', 'updated', 'is_archive'
    search_fields = 'name', 'author__username'
    list_filter = 'is_archive',
    raw_id_fields = 'author',
