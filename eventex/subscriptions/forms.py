#coding: utf-8
from django import forms


class SubscriptionForm(forms.Form):
    name = forms.ChoiceField()
    cpf = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()