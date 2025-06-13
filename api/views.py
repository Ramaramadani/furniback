from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Product, Order, Discount, ContactUs
from .serializers import UsersSerializer, ProductSerializer, OrderSerializer, DiscountSerializer, ContactUsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)  # Mengizinkan multipart untuk file gambar

    # Override 'create' method untuk menangani form-data termasuk gambar
    def create(self, request, *args, **kwargs):
        # Proses gambar dan data produk
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Simpan produk baru
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
