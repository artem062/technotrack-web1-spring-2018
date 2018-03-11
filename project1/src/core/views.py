# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def page(request):

    return HttpResponse('This is Main Page')
