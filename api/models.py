from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100)
    gmail = models.EmailField()
    kontak = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

class Product(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    gambar = models.ImageField(upload_to='products/')
    stok = models.IntegerField(default=0)  # Tambahan field stok

class Order(models.Model):
    produk = models.ForeignKey(Product, on_delete=models.CASCADE)
    waktu_pembelian = models.DateTimeField(auto_now_add=True)
    nama_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    SHIPPING_CHOICES = [
        ('JNT', 'JNT Delivery'),
        ('Cargo', 'Cargo'),
        ('Pickup', 'Self Pickup'),
    ]
    shipping_info = models.CharField(max_length=10, choices=SHIPPING_CHOICES)

class Discount(models.Model):
    nama_produk = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    gambar = models.ImageField(upload_to='discounts/')
    harga_diskon = models.DecimalField(max_digits=10, decimal_places=2)


class ContactUs(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    saran = models.TextField()
