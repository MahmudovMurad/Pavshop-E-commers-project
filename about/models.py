from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField, BooleanField, DateTimeField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from .models import*
from contact.models import *
import uuid

User = get_user_model()


# Create your models here.
class Shipping_info(models.Model):
    """
    User Shipping detail 
    """
    #relations
    info = models.ForeignKey('contact.User', db_index=True,on_delete=models.CASCADE,related_name='shipping_info',
                                                                null=True, blank=True)

    #table details
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    city_town = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)


class Billing_data(models.Model):
    """
    User Billing detail 
    """
    #relations
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ckeckout')

    #table details
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    company_name = models.CharField(max_length=50)
    city_town = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)




class ZipCode(models.Model):
    """
    product discount code
    """
    code = models.CharField(max_length=15)
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.code
        



class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ManyToManyField("store.Product", related_name='current_wishlist')

    class Meta:
        verbose_name = 'wishlist'
        verbose_name_plural= 'wishlists'

class Order(models.Model):
    #relations
    id = models.UUIDField(unique=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    checkout = models.ForeignKey(Billing_data, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField("store.Product", related_name='current_orders')
    #informations
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

        def __str__(self) -> str:
            return f'{self.user} - Order NO: {self.id}' 

        # @property
        # def shipping(self):
        #     shipping = False
        #     orderitems = self.orderitem_set.all()
        #     for i in orderitems:
        #         if i.product.digital == False:
        #             shipping = True
        #     return shipping  
    
        # #Total price
        # @property
        # def get_cart_total(self):
        #     orderitems = self.orderitem_set.all()
        #     total = sum([item.get_total for item in orderitems])
        #     return total
        
        # #Total items
        # @property
        # def get_cart_items(self):
        #     orderitems = self.orderitem_set.all()
        #     total = sum([item.quantity for item in orderitems])
        #     return total
        