# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.views import LogoutView, LoginView
from core.models import User


def page(request):

    return render(request, 'core/main_page.html')


class ChangeForm(UserChangeForm):

    email = forms.EmailField(required=True)


def profile(request):

    user = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        return render(request, 'core/profile.html', {'profile_form': ChangeForm(instance=user)})
    elif request.method == 'POST':
        form = ChangeForm(request.POST, instance=user)
        if form.is_valid():
            data = form.cleaned_data
            user.username = data['login']
            user.email = data['email']
            user.save()
            return redirect('core:profile')
        else:
            return render(request, 'core/profile.html', {'profile_form': form})


class Login (LoginView):

    template_name = 'core/login.html'


class Logout(LogoutView):

    template_name = 'core/logout.html'


class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)


def register(request):

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


