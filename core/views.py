from django.contrib.messages.api import success
from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
from django.utils.translation import pgettext
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormMixin
from store import form
from core.models import *
from core.views import *
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.list import ListView

from django.views.generic import FormView
from core.models import *
from core.form import *
from django.http import HttpResponseRedirect ,request
from rest_framework.generics import CreateAPIView
from rest_framework import serializers
from store.form import *
from .models import*

class SubscriberPage():
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data(**kwargs))

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context=self.get_context_data(**kwargs))



class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = (
            'email',
            )



class SubscribeAPIView(CreateAPIView):
    serializer_class = SubscriberSerializer


class CorePage(TemplateView, SubscriberPage):
    template_name = "base.html"


class BlogDetailPage(FormMixin, DetailView, SubscriberPage):

    form_class = ReviewForm
    model = Blog
    template_name = "blog-detail.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Product.objects.filter(id=self.kwargs['pk'])
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['brands'] = Brand.objects.all()
        return context

    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        return reverse('core:blog_detail', kwargs={"pk": self.object.pk})



    def form_valid(self, form):
        return super().form_valid(form)

   
    
 

class BlogListPage(CreateView, SubscriberPage):
    template_name = "blog-list.html"
    form_class = BlogListForm
    success_url = '/'
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['blogs'] = Blog.objects.all()
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()


        return context




   
class IndexPage(TemplateView, SubscriberPage):
    template_name = 'index.html'
    http_method_names = ['post', 'get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(**kwargs) )
    
class ProductList(ListView, SubscriberPage):
    model = Product
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['products'] = Product.objects.all()[:4]
        return context


class AboutPage(TemplateView, SubscriberPage):
    template_name = "about-us.html"


# def search(request):
#     query = request.GET.get('q')
#     if query:
#         products = Product.objects.filter(title__icontains=query)
#         return render(request, 'search.html', {'products': products})
#     else:
#         return redirect('/')

# class SearchPage(TemplateView):
#     method = ['get', 'post']
#     def search():
#         if request.method == "GET":
#             news = Product.query.all()
#             return render('product-list.html', news = news)
#         else:
#             searchKey = request.form["searchKey"]
#             search = "%{}%".format(searchKey)
#             searchVal = Product.query.filter(Product.title.like(search)).all()
#             return render('search.html', searchVal = searchVal)

# class SearchView(TemplateView):
#     model = Product
#     template_name = 'results.html'
   
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         return 
    
#     def get_context_data(self, **kwargs):
#         context = super(SearchView,self).get_context_data(**kwargs)
#         query = self.request.GET.get('q')

#         context['all_products'] = Product.objects.all().filter(title__icontains=query)
        
#         return context