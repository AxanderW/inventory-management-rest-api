#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from inventory_api import serializers
from inventory_api import models
from inventory_api import permissions

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class RegionViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating region objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.RegionSerializer
    queryset= models.Region.objects.all()
    permission_classes = (IsAuthenticated,permissions.AccessUpdateInventory)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class CategoryViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating category objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.CategorySerializer
    queryset= models.Category.objects.all()
    permission_classes = (IsAuthenticated,permissions.AccessUpdateInventory)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class BrandViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating brand objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.BrandSerializer
    queryset= models.Brand.objects.all()
    permission_classes = (IsAuthenticated,permissions.AccessUpdateInventory)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

class ProductViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating product objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProductSerializer
    queryset= models.Product.objects.all()
    permission_classes = (IsAuthenticated,permissions.AccessUpdateInventory)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','slug',)

class ProductItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating product item objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProductItemSerializer
    queryset= models.ProductItem.objects.all()
    permission_classes = (IsAuthenticated, permissions.AccessUpdateInventory)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('description',)


class OrderViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating order objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.OrderSerializer
    queryset= models.Order.objects.all()
    permission_classes = (IsAuthenticated,permissions.AccessUpdateInventory)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('order_id',)

class OrderItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, updating order items objects"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.OrderItemSerializer
    queryset= models.OrderItem.objects.all()
    permission_classes = (IsAuthenticated,permissions.AccessUpdateInventory)
