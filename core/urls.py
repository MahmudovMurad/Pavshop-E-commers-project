from os import name
from django.urls.resolvers import URLPattern
from django.urls import path
from django.views.generic import TemplateView
from core import views
from core.views import *


app_name = 'core'

urlpatterns= [
    path('core/', CorePage.as_view(), name="core"),
    path('blog_detail/<int:pk>/', BlogDetailPage.as_view(), name="blog_detail"),

    path('blog-list/', BlogListPage.as_view(), name="blog-list"),
    path('', ProductList.as_view(), name="main"), 
    path('about/', AboutPage.as_view(), name="about"),
    # path("shop/s", SearchView.as_view(), name="search"),
    path('subscribe/', views.SubscribeAPIView.as_view(), name="subscribe")
]
        