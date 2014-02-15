from django.http import HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            subscription = form.save()
            return HttpResponseRedirect(
                '/inscricao/%d/' % subscription.pk
            )
    return render(
        request,
        'subscriptions/subscription_form.html',
        {'form': form}
    )