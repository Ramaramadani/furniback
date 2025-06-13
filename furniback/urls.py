from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet  # Mengimpor ProductViewSet dari api.views

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API untuk produk
]
