from django.urls import path
from . import views
from contact.forms import *
from contact.views import ContactView, CustomLoginView, RegisterView, LogoutView,CustomPasswordResetView,CustomLogoutView,CustomPasswordResetConfirmView
from contact.views import *
from api.views import *
app_name = 'contact'

urlpatterns= [
    path('contact/', ContactView.as_view(), name="contact"),
    path('login/',   CustomLoginView.as_view(), name = "login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('forget-password/',CustomPasswordResetView.as_view(), name='forget-password'),
    path('confirm-password/<str:uidb64>/<str:token>/',
                                                 activate, name='confirm-password'),

    path('reset-password/<str:uidb64>/<str:token>/',
                                                CustomPasswordResetConfirmView.as_view(), name='reset_password'),
    # path('forget-password/', CustomPasswordResetView.as_view(), name='password-reset-view'),
    path('password-success/', views.password_success, name="password_success"),
]