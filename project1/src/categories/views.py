# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Category
from django import forms
from likes.models import Like


class CategoriesListForm (forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'по имени'),
        ('-name', 'по имени в обратном'),
        ('id', 'по ID'),
    ), required=False, label='Сортировать')
    search = forms.CharField(required=False, label='Поиск')


def category_list(request):

    categories = Category.objects.all()
    form = CategoriesListForm(request.GET)
    if form.is_valid():
        data = form.cleaned_data
        if data['sort']:
            categories = categories.order_by(data['sort'])
        if data['search']:
            categories = categories.filter(name__icontains=data['search'])
    context = {
        'categories': categories,
        'categories_form': form
    }
    return render(request, 'categories/categories_list.html', context)


def category_detail(request, pk=None):

    category = get_object_or_404(Category, id=pk)
    likes = Like.objects.all()

    context = {
        'category': category,
        'questions': category.questions.all().filter(is_archive=False),
        'likes': likes
    }
    return render(request, 'categories/category_detail.html', context)
