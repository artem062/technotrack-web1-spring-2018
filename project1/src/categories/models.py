# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name=u'Имя категории')
    # photo = models.FileField(null=True, upload_to='photos', blank=True)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'
        ordering = 'name', 'id'

    def __unicode__(self):
        return self.name
