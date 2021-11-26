from django.urls.resolvers import URLPattern
from django.urls import path
from store import views
from store.views import *


app_name = 'store'
urlpatterns= [
    # path('check/', CheckoutPage.as_view(), name="check"),
    path('shopping-cart/', ShoppingCartPage.as_view(), name="cart"),
    path('product-list/', ProductListPage.as_view(), name="product-list"),
    path('product-detail/<int:pk>/',ProductDetailPage.as_view(), name = "product-detail"),
]