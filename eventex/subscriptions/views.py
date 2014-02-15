from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            form.full_clean()
            subscription = Subscription(**form.cleaned_data)
            subscription.save()
            return HttpResponseRedirect('/inscricao/%d/' % subscription.pk)
    return render(
        request,
        'subscriptions/subscription_form.html',
        {'form': SubscriptionForm()}
    )