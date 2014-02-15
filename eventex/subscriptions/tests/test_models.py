#coding: utf-8
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