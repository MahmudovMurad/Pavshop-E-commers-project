from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from core.models import *

class Subscriber(models.Model):
    """
    Email accounts
    """

    email = models.EmailField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True, blank=True)

    #moderations
    created_at = models.DateTimeField(auto_now=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.email
class Price(models.Model):
    """
    Price model's save all products price range. 
    Ex: 0.00$ - 50.0$ , 50.00$ - 100.0$, 100.00$ - 150.0$ ...
    """
    #information
    price = models.CharField(max_length=50, default='0.00$ - 50.00$')

    def __str__(self):
        return self.price 
        
class Color(models.Model):
    
    #information
    color = models.CharField(max_length=50)
    is_published = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.color

class Category(models.Model):
    """
    all products catagories
    """
    #information
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
class Comment(models.Model):    
    #relation
    blog = models.ForeignKey('Blog', db_index=True,on_delete=models.CASCADE,related_name='comments',
                                                                null=True, blank=True)
    parent = models.ForeignKey('self',db_index=True, null=True, blank=True,
                                            related_name='replies', on_delete=models.CASCADE)

    #information
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=80)
    message = models.TextField(max_length=500)
    active = models.BooleanField(default=True)
    #moderations
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_comments(self):
        return Comment.objects.filter(parent=self).filter(active=True)
    
class Blog(models.Model):
    #relation
    category = models.ManyToManyField('core.Category',db_index=True,)
    tags = models.ManyToManyField('Tag',db_index=True)
    author = models.ForeignKey('contact.User',on_delete=models.CASCADE,related_name='blog_posts',blank=True,null=True)

    #information
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='media/category_images/')
    description = models.TextField(max_length=2000)
    

    created_at = models.DateTimeField(auto_now=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)


    def __str__(self):
        return self.title
