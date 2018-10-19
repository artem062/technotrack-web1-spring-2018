# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.test import TestCase, Client
import factory


class RegisterSiteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)


class SearchSiteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code, 200)


class LoginSiteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)


class LogoutSiteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)


class MainSiteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'Login_{0}'.format(n))
    email = factory.Sequence(lambda n: 'test_{0}@gmail.com'.format(n))


class UserSaveTest(TestCase):
    def setUp(self):
        self.users_count = 100
        for i in range(self.users_count):
            UserFactory.create()

    def test_status(self):
        self.assertEqual(User.objects.count(), self.users_count)
