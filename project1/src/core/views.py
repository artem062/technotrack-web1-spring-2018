# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def page(request):

    return render(request, 'core/main_page.html')


def login(request):

    return render(request, 'core/login.html')


def logout(request):

    return render(request, 'core/logout.html')


def register(request):

    return render(request, 'core/register.html')
