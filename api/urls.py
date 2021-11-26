from rest_framework import views
from django.urls import path
from . import views
from contact.views import RegisterView
from api.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('registerapi/', RegisterVieww.as_view(), name='auth_register'),
    path('loginapi/', TokenObtainPairView.as_view(), name='auth_login'),
    path('refreshapi/', TokenRefreshView.as_view(), name='auth_refresh'),
    path('card/', views.CardView.as_view(), name='card'),
    # path('productsapi/', ProductsAPIView.as_view(), name='post'),
    path('product/', views.ProductAPIView.as_view(), name='product'),
    path('basket_item_delete/', BasketItemDeleteView.as_view(), name='basket_item_delete'),
    # path('basket/', views.BasketAPIView.as_view(), name='basket'),
]