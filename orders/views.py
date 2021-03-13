from django.shortcuts import render
from django.conf import settings
from django.views.generic import TemplateView
import stripe

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key'] = settings.STRIPE_TEST_PUBLISHABLE_KEY
        context['price'] = self.request.GET.get('price')
        context['amount'] = int("".join(list(context['price'].split('.'))))
        return context


def charge(request, pk):
    if request.method == 'POST':
        charge = stripe.Charge.create(amount=int(request.POST.get('amount')),
                                      currency='usd',
                                      description='Purchase all books',
                                      source=request.POST['stripeToken']
                                      )
        return render(request, 'orders/charge.html', context={
            'pk': pk,
        })