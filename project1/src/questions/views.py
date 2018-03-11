# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse


def question_id (request, quest_id):

    return HttpResponse('This is question №{}'.format(quest_id))


def question_list (request):

    return HttpResponse('Questions:')

