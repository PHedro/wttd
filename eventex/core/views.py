# coding: utf-8
from django.shortcuts import render
from django.template.context import RequestContext


def home(request):
    template = 'index.html'
    return render(request, template)