# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Category
from django import forms
# from django.http import JsonResponse
# from jsonrpc import jsonrpc_method
# from django.core.serializers import serialize


class CategoriesListForm (forms.Form):

    sort = forms.ChoiceField(choices=(
        ('name', 'по имени'),
        ('-name', 'по имени в обратном'),
        ('id', 'по ID'),
    ), required=False, label='Сортировать')
    search = forms.CharField(required=False, label='Поиск')


def category_list(request):

    categories = Category.objects.values('id', 'name')
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


# @jsonrpc_method('api.category_list')
# def category_list(request):
#
#     categories = Category.objects.all()
#     form = CategoriesListForm(request.GET)
#     if form.is_valid():
#         data = form.cleaned_data
#         if data['sort']:
#             categories = categories.order_by(data['sort'])
#         if data['search']:
#             categories = categories.filter(name__icontains=data['search'])
#     return JsonResponse({'categories': serialize('json', categories)})


def category_detail(request, pk=None):

    category = get_object_or_404(Category, id=pk)
    context = {
        'category': category,
        'questions': category.questions.all().filter(is_archive=False).values('id', 'name'),
    }
    return render(request, 'categories/category_detail.html', context)


# @jsonrpc_method('api.category_detail')
# def category_detail(request, pk=None):
#
#     category = get_object_or_404(Category, id=pk)
#     return JsonResponse({
#         'category': serialize('json', [category]),
#         'questions': serialize('json', category.questions.all().filter(is_archive=False))
#     })
