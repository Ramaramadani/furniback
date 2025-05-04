from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('discounts', DiscountViewSet)
router.register('contact', ContactUsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
