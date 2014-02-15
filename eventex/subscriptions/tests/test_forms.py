# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_fields(self):
        expected_items = ['name', 'email', 'cpf', 'phone']
        form = SubscriptionForm()
        self.assertItemsEqual(expected_items, form.fields)