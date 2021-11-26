from typing import Type
from django.db import models
from django.db.models.expressions import Value
from django.utils import timezone
import datetime
import uuid
from django.conf import settings
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from django.urls import reverse
from django.utils.regex_helper import Choice
from store.models import *
from about.models import *
from store.models import *

User = get_user_model()

# class Base(models.Model):

#     creation_date = models.DateTimeField()
#     validity_start_date = models.DateTimeField() 
#     validity_end_date = models.DateTimeField() 
#     class Meta:
#         abstract=True 



class Category(models.Model):
    """
    all products catagories
    """
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.category

class Tag(models.Model):
    """
    Tag model's save tags.
    """
    #information
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

class ProductAttribute(models.Model):
    Type = (
        ('size','Size'),
        ('color', 'Color'),
        ('brand', 'Brand'),
    )
    Values = (
        ('red', 'Red'),
        ('yellow', 'Yellow'),
        ('brown', 'Brown'),
        ('green', 'Green'),
        ('blue', 'Blue'),
        ('pink', 'Pink'),
        ('gold', 'Gold'),
        ('purple', 'Purple'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
    )
    product = models.ForeignKey('ProductVersion', on_delete=models.CASCADE, related_name='versions')
    type = models.CharField(max_length=20, choices=Type)
    value = models.CharField(max_length=10, choices=Values)


class Card(models.Model):
    """
    Basket model's save basket's products.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='basket')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'

    def __str__(self):
        return self.product.name


class Image(models.Model):
    """
    Image model's save product's images.
    """
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_detail_images/')

    def __str__(self):
        return self.product.name


class Product(models.Model):

    #relation
    brand = models.ManyToManyField('store.Brand', db_index=True, null=True,blank=True, related_name='product_brand')
    colors = models.ManyToManyField('store.Color', db_index=True, null=True,blank=True,related_name='product_color')
    category = models.ManyToManyField('core.Category', db_index=True, null=True,blank=True, related_name='product_category')

    #Product information    
    slug = models.CharField(max_length=255, unique=False, blank=True, null=True)
    name = models.CharField(max_length=50)
    cover_image =  models.ImageField(upload_to='product_cover_image', null =True, blank = True)    
    price = models.IntegerField(default=100, null=True, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    description = models.CharField(max_length=100)
    
    discount_price = models.IntegerField(default=0, null=True, blank=True)
    designer = models.CharField(max_length=255)
    sale_percant = models.IntegerField(default=0, blank=True, null=True)
    sale_time = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        
        verbose_name = 'item'
        verbose_name_plural = 'item'


    def __str__(self):
        return self.name



    @property
    def new_price(self):
        
        if self.sale_percant != 0:
            self.price = round(self.price - self.price * self.sale_percant / 100, 2)
        
        return "$%s" % self.price
       

    @property
    def get_total(self):
        if self.discount_price:
            total = self.discount_price * self.quantity
            return total
        elif self.discount_price == 0.00 and self.sale != 0:
            x = self.price * (100 - self.sale) // 100
            return x * self.quantity
        elif self.discount_price == 0.00 and self.sale == 0:
            total = self.price * self.quantity
            return total
        else:
            total = self.discount_price * self.quantity
            return total
   

    def get_absolute_url(self):
        return reverse_lazy('store:product-detail', kwargs={
            'slug': self.slug
        })

    @property
    def image_url(self):
        if self.cover_image and hasattr(self.cover_image, 'url'):
            return self.cover_image.url
   
    

class ProductVersion(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    quantity = models.IntegerField(default=1)


class Blog(models.Model):
    #relation
    category = models.ManyToManyField('Category',db_index=True,)
    tags = models.ManyToManyField('Tag',db_index=True)
    # author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts',blank=True,null=True)

    #information
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/category_images/')
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.title


class Color(models.Model):
    """
    Color model's save all products colors. 
    Ex: Red, Yellow, Green...
    """
    #information
    color = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.color

class Brand(models.Model):
     """
     Products brand
     """
     #information
     brand = models.CharField(max_length=100)

     def __str__(self) -> str:
         return self.brand

class Review(models.Model):
    """
    Coments about product.
    """
    #relation
    product = models.ForeignKey('Product',db_index=True, on_delete=models.CASCADE, blank=True,null=True,related_name='reviews')
    comment = models.ForeignKey('self', db_index=True, related_name='comments', on_delete=models.CASCADE, blank=True,null=True)
    #information
    profile_img = models.ImageField(upload_to='profile_image', null =True, blank = True)
    rate = models.IntegerField(default=0,blank=True,null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    message = models.TextField(max_length=500)
    is_published = models.BooleanField(default=False)

    #####
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        if self.comment:
            return f"{self.comment} > {self.name}"
        return self.name


class Popular_Products(models.Model):
    """
    Popular products slide
    """
    img = models.ImageField(upload_to='slider_image', null=True, blank=True)
    name = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)


class Shopping_card(models.Model):
    """
    Shopping card of user model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='shoppingCardOfUser')
    product = models.ManyToManyField(Product, related_name='shoppingCardOfProduct')
    item = models.ManyToManyField("BasketItem", related_name='shoppingCardOfItem')

    class Meta:
        verbose_name = 'Shopping Card Of User'
        verbose_name_plural = 'Shopping Cards Of User'

    def total_price(self):
        total = 0
        for i in self.item.all():
            total += i.get_total_price
        return total

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.product.values())

    # @property
    # def cupon(self):
    #     if self.zip_id:
    #         return zip.objects.get(id=self.zip_id)
    #     return None
        
    # def get_discount(self):
    #     if self.zip_id:
    #         return (self.zip_id.discount / Decimal('100')) * self.get_total_price()
    #     return Decimal('0')

    # def get_total_price_after_discount(self):
    #     return self.get_total_price() - self.get_discount()  

class BasketItem(models.Model):
    """
    Basket item model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket_items')
    user_of_shopping_card = models.ForeignKey(Shopping_card, on_delete=models.CASCADE, related_name='shopping_card_item',null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_basket_item')
    quantity = models.IntegerField(default=0, null=True, blank=True)


    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'
    
    def __str__(self):
        return f"{self.product} - {self.quantity}"

    @property
    def get_total_price(self):
        return self.quantity * self.product.price

    

      
