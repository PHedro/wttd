from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def new(request):
    return render(
        request,
        'subscriptions/subscription_form.html',
        {'form': SubscriptionForm()}
    )


def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(
            request,
            'subscriptions/subscription_form.html',
            {'form': form}
        )

    subscription = form.save()
    return HttpResponseRedirect(
        '/inscricao/%d/' % subscription.pk
    )


def detail(request, pk):
    subscription = Subscription.objects.get(pk=pk)
    return render(
        request,
        'subscriptions/subscription_detail.html',
        {'subscription': subscription}
    )