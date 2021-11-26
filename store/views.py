from store.models import Review
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from store.form import ReviewForm
from store.models import *
from core.views import *
from django.urls import *
from store.models import Review,Tag,Blog,Popular_Products,Product,Color,Brand
from core.models import *
from django.http import HttpResponse

class ShoppingCartPage(TemplateView, SubscriberPage):
    template_name = "shopping-cart.html"

# class CheckoutPage(TemplateView, SubscriberPage):
#     template_name = "checkout.html"


class ProductPage(DetailView, SubscriberPage):
    form_class = Product
    model = Product
    context_object_name = "productdes"
    template_name = "product-detail.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        return context




class ProductDetailPage(FormMixin, DetailView, SubscriberPage):
    form_class = ReviewForm
    model = Product
    context_object_name = "product"
    template_name = "product-detail.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(id=self.kwargs['pk'])
        context['posts'] = Product.objects.all()
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
        return reverse('store:product-detail', kwargs={"pk": self.object.pk})



    def form_valid(self, form):
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = self.get_form()
    #     return context

    
class ImageView(DetailView):
    model = Image
    template_name = "product-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = Image.objects.all()
        return context

class ProductListPage(ListView, SubscriberPage):
    model = Product
    paginate_by = 6
    template_name = "product-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['brands'] = Brand.objects.all()
        context['products'] = Product.objects.all()
        return context


class PostView(View):

    def get_object(self):
        return Product.objects.filter(id = self.kwargs['pk'].first())
    
    def update_view_count(self):
        product = self.get_object()
        product.view_count += 1
        product.save()


# class SearchPage(TemplateView):
#     method = ['get', 'post']
#     def search():
#         if request.method == "GET":
#             news = Product.query.all()
#             return render('product-list.html', news = news)
#         else:
#             searchKey = request
#             search = "%{}%".format(searchKey)
#             searchVal = Product.query.filter(Product.title.like(search)).all()
#             return render('search.html', searchVal = searchVal)