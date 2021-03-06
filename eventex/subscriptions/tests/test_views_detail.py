#coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class DetailTest(TestCase):
    def setUp(self):
        subscription = Subscription.objects.create(
            name='Teste',
            cpf='12345678901',
            email='teste@teste.com',
            phone='21-999998888'
        )
        self.response = self.client.get(
            '/inscricao/%d/' % subscription.pk
        )

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.response,
            'subscriptions/subscription_detail.html'
        )

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.response, 'Teste')


class DetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)