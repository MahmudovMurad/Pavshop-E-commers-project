from django.http import request
from rest_framework import fields, serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from contact.views import logout
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from contact.task import send_confirmation_mail
from core.models import *
from rest_framework_jwt.settings import api_settings
# from rest_framework.exceptions import NotAuthenticated
from store.models import  BasketItem, Card, Product, ProductVersion, Shopping_card
# from rest.apps.user.models import User
from contact.task import send_confirmation_mail

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'surname',
            'email',
            'phone',
            'image',
            'address1',
            'address2',
            'country_state',
            'town',
            'token',
        )

    def get_token(self, user):
        token, created = Token.objects.get_or_create(user=user)
        return token.key

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('name', 'surname', 'email', 'password1', 'password2', 'phone','address1',)
        extra_kwargs = {
            'name': {'required': True},
            'surname': {'required': True}
        }


    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            name=validated_data['name'],
            surname=validated_data['surname'],
            is_active=False
        )
        user.set_password(validated_data['password1'])
        user.save()
        send_confirmation_mail(user)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = User.objects.filter(email=email)
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }    



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = (
            'color',
        )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'price',
        )

class ProductSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
            

    read_only_fields = ('is_active', 'is_staff')

    def get_discount_price(self, obj):
        if obj.sale_percant != 0 and obj.discount_price == 0.00:
            return obj.price * (100 - obj.sale_percant) // 100
        return obj.discount_price



class ProductListSerializer(ProductSerializer):
    colors = ColorSerializer(many=True)
    prices_range = PriceSerializer(many=True)


# class ProductSerializer(serializers.ModelSerializer):
    # discount_price = serializers.SerializerMethodField()

    # class Meta:
    #     model = Product
    #     fields = (
    #         'name', 
    #         'price', 
    #         'discount_price',
    #         'cover_image', 
    #         'description',
    #         'sale_percant', 
    #         'sale_time', 
    #         'colors',
    #         'brand',
    #         'id'
    #     )

    # read_only_fields = ('is_active', 'is_staff')

    # def get_discount_price(self):
    #     if self.sale_percant != 0:
    #         self.price = round(self.price - self.price * self.sale_percant / 100, 2) 
    #     return "$%s" % self.price
       
class ShoppingCardSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Shopping_card
        fields = '__all__'



class ProductVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVersion
        fields = (
            'product',
            'image',
            'quantity',
            )

    read_only_fields = ('is_active', 'is_staff')



class CardSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many = True)
    class Meta:
        model = Card
        fields = '__all__'


class CardItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = BasketItem
        fields = '__all__'