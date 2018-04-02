# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django import forms
from django.contrib.auth.views import LogoutView, LoginView


def page(request):

    return render(request, 'core/main_page.html')


class Login (LoginView):

    template_name = 'core/login.html'


class Logout(LogoutView):
    template_name = 'core/logout.html'


class RegisterForm (forms.Form):

    email = forms.EmailField(required=True)
    login = forms.CharField(required=True)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    avatar = forms.FileField(required=False)


def register(request):

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'core/register.html', {'register_form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            pass
        else:
            return render(request, 'core/register.html', {'register_form': form})


