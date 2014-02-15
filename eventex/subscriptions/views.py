from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/inscricao/%d/' % 1)
    return render(
        request,
        'subscriptions/subscription_form.html',
        {'form': SubscriptionForm()}
    )