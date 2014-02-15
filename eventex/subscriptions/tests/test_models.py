#coding: utf-8
from datetime import datetime
from django.db import IntegrityError
from django.test import TestCase
from eventex.subscriptions.models import Subscription

__author__ = 'phedro'


class SubscriptionTest(TestCase):
    def setUp(self):
        self.subscription = Subscription(
            name='Teste',
            cpf='12345678901',
            email='teste@teste.com',
            phone='21999998888'
        )

    def test_create(self):
        self.subscription.save()
        self.assertEqual(1, self.subscription.pk)

    def test_has_create_at(self):
        self.subscription.save()
        self.assertIsInstance(self.subscription.created_at, datetime)


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name='Teste',
            cpf='12345678901',
            email='teste@teste.com',
            phone='21-999998888'
        )

    def test_cpf_unique(self):
        subscription = Subscription(
            name='Teste',
            cpf='12345678901',
            email='teste2@teste.com',
            phone='21-999998888'
        )
        self.assertRaises(IntegrityError, subscription.save)