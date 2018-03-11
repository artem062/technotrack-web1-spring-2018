# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def category_id (request, cat_id):

    return HttpResponse('This is category №{}'.format(cat_id))


def category_list (request):

    return HttpResponse('Categories:')

