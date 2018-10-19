# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Question, Answer
from core.tests import UserFactory
from mock import patch
import questions
import factory

from django.test import TestCase, Client


class QuestionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Question

    name = factory.Sequence(lambda n: 'question_{0}'.format(n))
    author = factory.SubFactory(UserFactory)


class QuestionSaveTest(TestCase):
    def setUp(self):
        self.question_count = 100
        self.user = UserFactory.create()
        self.questions = {}
        for i in range(self.question_count):
            self.questions[i] = QuestionFactory.create()

    def test_count(self):
        self.assertEqual(Question.objects.count(), self.question_count)

    def test_status(self):
        for i in range(self.question_count):
            response = self.client.get('/question/{0}/'.format(self.questions[i].pk))
            self.assertEqual(response.status_code, 200)


class AnswerFactory(factory.DjangoModelFactory):
    class Meta:
        model = Answer

    name = factory.Sequence(lambda n: 'answer_{0}'.format(n))
    author = factory.SubFactory(UserFactory)
    question = factory.SubFactory(QuestionFactory)


class AnswerSaveTest(TestCase):
    def setUp(self):
        self.answer_count = 100
        self.user = UserFactory.create()
        self.question = QuestionFactory.create()
        for i in range(self.answer_count):
            AnswerFactory.create()

    def test_count(self):
        self.assertEqual(Answer.objects.count(), self.answer_count)


class QuestionsSiteTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status(self):
        response = self.client.get('/question/')
        self.assertEqual(response.status_code, 200)


class QuestionDetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserFactory.create()
        self.question = QuestionFactory.create()

    def test_entry_list(self):
        response = self.client.get('/question/{0}/'.format(self.question.pk))
        self.assertEqual(response.status_code, 200)


class TestQuestionsMock(TestCase):
    def setUp(self):
        # self.question_count = 100
        self.user = UserFactory.create()
        # self.questions = {}
        # for i in range(self.question_count):
        #     self.questions[i] = QuestionFactory.create()

    @patch('questions.views.question_detail')
    def test_question_site_with_mock(self, questions_detail_mock):
        questions_detail_mock.return_value = 200
        self.assertEqual(questions.views.question_detail(), 200)
