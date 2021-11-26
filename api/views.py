from django.contrib.auth.models import Permission
from django.core.checks import messages
from django.db.models.query import QuerySet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from store.models import Product
from api import serializers
from rest_framework import status
from rest_framework.response import Response
from store.models import Shopping_card
from api.serializers import *
from django.core import serializers

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework import generics,permissions
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveAPIView
from api.serializers import CardSerializer, ProductVersionSerializer, UserLoginSerializer, RegisterSerializer
from store.models import ProductVersion
from api.views import *
from django.http.response import Http404, JsonResponse

from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthToken(ObtainAuthToken):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        user_serializer = serializer.UserLoginSerializer(user)
        print(user_serializer.data, 'salam')
        return Response(user_serializer.data, status=200)


class RegisterVieww(generics.CreateAPIView):
    model = User
    serializer_class = RegisterSerializer


class LoginAPIView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                                    context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        user_serializer = serializer.UserSerializer(user)
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_detail':user_serializer.data,
        })





class ProductAPIView(APIView):
    permission_class = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        arr = []
        for item in Product.objects.all():
            serializer = ProductSerializer(item)
            arr.append(serializer.data)
        return Response(arr, status=200)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


   
class CardView(APIView):
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated]   


    def get(self, request, *args, **kwargs):
        card = Shopping_card.objects.filter(user=request.user).first()
        sebet = BasketItem.objects.filter(user_of_shopping_card=card,user=request.user)
        arr = []
        for i in sebet:
            serializer = CardItemSerializer(i)
            print(i)
            arr.append(serializer.data)
        serializer = self.serializer_class(request.user.shoppingCardOfUser)
        return Response(serializer.data, status=200)

    def post(self, request, *args, **kwargs ):
        quantity = request.data.get('quantity')
        print(quantity,'quantity')
        product_id = request.data.get('product_id')
        product = Product.objects.filter(id=product_id).first()
        print(product)

        if product:
            basket_item = BasketItem.objects.get_or_create(product=product,user=request.user)
            basket_item2 = BasketItem.objects.get(product=product,user=request.user)
            basket_item2.quantity += quantity
            basket_item2.save()
            print(basket_item2.quantity)
            basket, created = Shopping_card.objects.get_or_create(user = request.user) 
            basket.item.add(basket_item2)             
           
            arr = []

            for item in basket.item.all():
                serializer = CardItemSerializer(item)
                arr.append(serializer.data)
            
           
            message = {'success' : True , 'message' : 'Added to cart'}
            return Response(arr, status=200)
        message = {'success' : False, 'message' : 'product not found'}
        return Response(message, status=400)

    
class BasketItemDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CardItemSerializer

    def post(self, request, *args, **kwargs):
        itemId = request.data.get('itemId')
        BasketItem.objects.get(id=itemId).delete()
        item = BasketItem.objects.filter(user_of_shopping_card=request.user).first()
        if not item:
            return Response(status=404)
        serializer = CardItemSerializer(item)
        return Response(serializer.data, status=200)
  
        
            
