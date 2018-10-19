# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, Client
from core.tests import UserFactory
from .models import Category
import json

import factory


class CategorySiteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)


class CategoryFactory(factory.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: 'category_{0}'.format(n))


class CategoryDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = CategoryFactory.create()

    def test_status(self):
        response = self.client.get('/category/{0}/'.format(self.category.pk))
        self.assertEqual(response.status_code, 200)


class CategorySaveTest(TestCase):
    def setUp(self):
        self.category_count = 100
        self.categories = {}
        for i in range(self.category_count):
            self.categories[i] = CategoryFactory.create()

    def test_count(self):
        self.assertEqual(Category.objects.count(), self.category_count)

    def test_status(self):
        for i in range(self.category_count):
            self.assertEqual(self.client.get('/category/{0}/'.format(self.categories[i].pk)).status_code, 200)


class CategoryTestFixtures(TestCase):
    fixtures = ['categories/fixtures/categories.json', ]

    def setUp(self):
        self.data = json.load(open('categories/fixtures/categories.json'))

        # for i in range(6):
        #     response = self.client.get('/category/{0}/'.format(data[i]['pk']))
        #     self.assertEqual(response..category.name, 200)
        #     self.assertEqual(response.status_code, 200)
        self.user = Client()

    def test_from_fixtures(self):
        for i in range(6):
            response = self.client.get('/category/{0}/'.format(self.data[i]['pk']))
            self.assertEqual(response.body.category.name, 200)
            self.assertEqual(response.status_code, 200)
