# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LogoutView, LoginView
from core.models import User
from questions.models import Question, Answer
from categories.models import Category
from django.http import JsonResponse
# from jsonrpc import jsonrpc_method
from django.core.serializers import serialize
from django.core.files.base import ContentFile
import base64
import hashlib
from .prof import profiler


# @profiler
def page(request):

    return render(request, 'core/main_page.html', {'categories': Category.objects.order_by('name').values('id', 'name')})


# @jsonrpc_method('api.page')
# def page(request):
#
#     return JsonResponse({'categories': serialize('json', Category.objects.order_by('name'))})


class ChangeForm(UserChangeForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = UserChangeForm.Meta.model
        fields = 'username', 'email',


# @profiler
def profile(request):

    user = User.objects.get(id=request.user.id)
    context = {
        'questions': Question.objects.filter(author=request.user).values('id', 'name'),
        'answers': Answer.objects.filter(author=request.user).values('id', 'name')
    }
    if request.method == 'GET':
        context['profile_form'] = ChangeForm(instance=user)
        return render(request, 'core/profile.html', context)
    elif request.method == 'POST':
        form = ChangeForm(request.POST, instance=user)
        if form.is_valid():
            data = form.cleaned_data
            user.username = data['login']
            user.email = data['email']
            user.save()
            return redirect('core:profile')
        else:
            context['profile_form'] = form
            return render(request, 'core/profile.html', context)


# @jsonrpc_method('api.profile')
# def profile(request):
#     user = User.objects.get(id=request.user.id)
#     if request.method == 'GET':
#         mainForm = ChangeForm(instance=user)
#     elif request.method == 'POST':
#         form = ChangeForm(request.POST, instance=user)
#         if form.is_valid():
#             data = form.cleaned_data
#             user.username = data['login']
#             user.email = data['email']
#             user.save()
#             return redirect('core:profile')
#         else:
#             mainForm = form
#     print mainForm
#     return JsonResponse({
#         'questions': serialize('json', Question.objects.filter(author=request.user)),
#         'answers': serialize('json', Answer.objects.filter(author=request.user)),
#     })


class Login (LoginView):

    template_name = 'core/login.html'


class Logout(LogoutView):

    template_name = 'core/logout.html'


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = 'username', 'email'


# @profiler
def search(request):
    if request.method == 'GET':
        return render(request, 'core/register.html', {'register_form': RegisterForm()})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User()
            user.username = data['login']
            user.email = data['email']
            user.save()
            return redirect('core:profile')
        else:
            return render(request, 'core/register.html', {'register_form': form})


# @profiler
def register(request):

    if request.method == 'GET':
        return render(request, 'core/register.html', {'register_form': RegisterForm()})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:profile')
        else:
            return render(request, 'core/register.html', {'register_form': form})


# def register_json(request):
#
#     if request.method == 'GET':
#         return JsonResponse({'register_form': RegisterForm()})
#     elif request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('core:profile')
#         else:
#             return JsonResponse({'register_form': form})


# def generate_key(filename, category_id):
#     h = hashlib.new('md5')
#     h.update('{}{}'.format(filename, category_id).encode('utf8'))
#     return h.hexdigest()
#
#
# @jsonrpc_method('api.upload_file')
# def upload_file(request, base64_content, file_name, category_id):
#     content = base64.b64decode(base64_content)
#     category = Category.objects.all().filter(id=category_id).first()
#     key = generate_key(file_name, category.id)
#     category.photo.save(key, ContentFile(content.decode('utf8')))
#     return content
