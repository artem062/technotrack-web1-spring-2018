# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import CategoryLike, QuestionLike, AnswerLike
# Register your models here.


@admin.register(CategoryLike)
class CategoryLikeAdmin(admin.ModelAdmin):

    list_display = 'author', 'category', 'put'
    search_fields = 'author', 'category'


@admin.register(QuestionLike)
class QuestionLikeAdmin(admin.ModelAdmin):

    list_display = 'author', 'question', 'put'
    search_fields = 'author', 'question'


@admin.register(AnswerLike)
class AnswerLikeAdmin(admin.ModelAdmin):

    list_display = 'author', 'answer', 'put'
    search_fields = 'author', 'answer'
