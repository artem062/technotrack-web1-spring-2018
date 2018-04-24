# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LogoutView, LoginView
from core.models import User
from questions.models import Question, Answer
from categories.models import Category


def page(request):

    return render(request, 'core/main_page.html', {'categories': Category.objects.order_by('name')})


class ChangeForm(UserChangeForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = UserChangeForm.Meta.model
        fields = 'username', 'email',


def profile(request):

    user = User.objects.get(id=request.user.id)
    context = {
        'questions': Question.objects.filter(author=request.user),
        'answers': Answer.objects.filter(author=request.user)
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


class Login (LoginView):

    template_name = 'core/login.html'


class Logout(LogoutView):

    template_name = 'core/logout.html'


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = 'username', 'email'


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


