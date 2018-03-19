# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from .models import Category


def category_list(request):

    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'categories/categories_list.html', context)


def category_detail(request, pk=None):

    category = Category.objects.get(id=pk)

    context = {
        'category': category,
        'questions': category.questions.all().filter(is_archive=False)
    }
    return render(request, 'categories/category_detail.html', context)
