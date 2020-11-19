from django.urls import path, include

from rest_framework.routers import DefaultRouter

from inventory_api import views



router = DefaultRouter()

router.register('profile',views.UserProfileViewSet)
router.register('region',views.RegionViewSet)
router.register('category',views.CategoryViewSet)
router.register('brand',views.BrandViewSet)
router.register('product',views.ProductViewSet)
router.register('product-item',views.ProductItemViewSet)
router.register('order',views.OrderViewSet)
router.register('order-item',views.OrderItemViewSet)


urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),

]
