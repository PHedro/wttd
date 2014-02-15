# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


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
