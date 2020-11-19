from rest_framework import serializers
from inventory_api import models

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password':{
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )

        return user


class RegionSerializer(serializers.ModelSerializer):
    """Serializes a region object"""
    class Meta:
        model = models.Region
        fields = ('id', 'name', 'is_active',)

class CategorySerializer(serializers.ModelSerializer):
    """Serializes a category object"""
    class Meta:
        model = models.Category
        fields = ('id', 'name', 'is_active',)

class BrandSerializer(serializers.ModelSerializer):
    """Serializes a Brand object"""
    class Meta:
        model = models.Brand
        fields = ('id', 'name','is_active', )

class ProductSerializer(serializers.ModelSerializer):
    """Serializes a Product object"""
    class Meta:
        model = models.Product
        fields = (
                    'id', 'name', 'slug','category', 'brand',
                    'retail_price','sale_price','qty',
                    'release_date','is_available'
                    )

class ProductItemSerializer(serializers.ModelSerializer):
    """Serializes a Product Item object"""
    class Meta:
        model = models.ProductItem
        fields = (
                    'id', 'product', 'description',
                    'unit_measure', 'measaure',
                    'unit_retail_price','unit_sale_price'
                    )


class OrderSerializer(serializers.ModelSerializer):
    """Serializes an Order object"""
    class Meta:
        model = models.Order
        fields = (
                    "__all__"

                    )

class OrderItemSerializer(serializers.ModelSerializer):
    """Serializes a region object"""
    class Meta:
        model = models.OrderItem
        fields = (
                     "__all__"

                    )
