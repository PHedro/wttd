# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        response = self.response
        self.assertContains(response, '<form')
        self.assertContains(response, '</form>')
        self.assertContains(response, '<input', 6)
        self.assertContains(response, 'type="text"', 3)
        self.assertContains(response, 'type="email"')
        self.assertContains(response, 'type="submit"')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Teste',
            cpf='12345678901',
            email='teste@teste.com',
            phone='21-999998888'
        )
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(302, self.response.status_code)

    def test_save(self):
        self.assertTrue(Subscription.objects.exists())


class SubscribeInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(
            name='Teste',
            cpf='123456789012',
            email='teste@teste.com',
            phone='21-999998888'
        )
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_form_errors(self):
        self.assertTrue(self.response.context['form'].errors)

    def test_dont_save(self):
        self.assertFalse(Subscription.objects.exists())