from django.shortcuts import render
from django.views.generic.base import TemplateView
from about.forms import BillingData
from core.views import *


class OrderPage(TemplateView, SubscriberPage):
    template_name = "about-us.html"


class CheckoutPage(TemplateView, SubscriberPage):
    template_name = "checkout.html"


class BillingData(CreateView, SubscriberPage):

    form_class = BillingData
    template_name = 'checkout.html'
   
    def get_success_url(self):
        return reverse_lazy('core:main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# class BillingData(CreateView):
#     form_class = Billing_data
#     template_name = 'checkout.html'
#     models = Billing_data



