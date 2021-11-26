from about.models import Shipping_info
from os import name
from django.urls.resolvers import URLPattern
from django.urls import path
from django.views.generic import TemplateView
from about import views
from about.views import BillingData, OrderPage , CheckoutPage


urlpatterns= [
    path('info/', OrderPage.as_view(), name="order"),
    path('check/', BillingData.as_view(), name="check"),
    ]