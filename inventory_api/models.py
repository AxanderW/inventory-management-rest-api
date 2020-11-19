from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save new super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of user"""
        return self.email


class Region(models.Model):
    """Datbase model for Regions in the system"""
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of region"""
        return self.name


class Category (models.Model):
    """Database model for categories in the system"""
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of category"""
        return self.name

class Brand (models.Model):
    """Database model for brands in the system"""
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of brand"""
        return self.name


class Product(models.Model):
    """Database model for products in the system"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE,

    )
    brand = models.ForeignKey(
        Brand,
        on_delete = models.CASCADE,


    )
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)

    sale_price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    default = 0 )

    qty = models.IntegerField(default=0)
    release_date = models.DateField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def increase_product_qty(self):
        self.qty +=1
        return self.qty


    def reduce_product_qty(self):
        self.qty -=1
        return self.qty


    def __str__(self):
        """Return string representation of product"""
        return self.name

class ProductItem(models.Model):
    """Database model for a product item in the system"""
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE,

    )
    description = models.TextField(blank=True, null=True)
    unit_measure = models.CharField(blank=True, null=True, max_length=100)
    measaure = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    default = 0 )

    unit_retail_price = models.DecimalField(max_digits=10, decimal_places=2,
                                            null=True
                                            )


    unit_sale_price = models.DecimalField(max_digits=10,
                                    decimal_places=2,
                                    null=True )


    def __str__(self):
        """Return string representation of product item"""
        return f"{self.product}: {self.id}"


class Order(models.Model):
    """Database model for an order in the system"""
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """Return string representation of product"""
        return self.id

class OrderItem(models.Model):
    """Database model for an order item in the system"""
    order_id = models.ForeignKey(
        Order,
        on_delete = models.CASCADE,

    )
    product_item = models.ForeignKey(
        ProductItem,
        on_delete = models.CASCADE,

    )
    qty = models.IntegerField()

    def sub_total(self):
        return self.product_item.unit_sale_price * self.qty

    def __str__(self):
        """Return string representation of order item"""
        return f"{self.product_item}: {self.qty}"
