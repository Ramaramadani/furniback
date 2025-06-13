from rest_framework import serializers
from .models import Users, Product, Order, Discount, ContactUs

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    # Validasi untuk gambar produk (jika gambar tidak diupload)
    def validate_gambar(self, value):
        if not value:
            raise serializers.ValidationError("Gambar produk diperlukan.")
        return value

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate(self, data):
        produk = data['produk']
        if produk.stok <= 0:
            raise serializers.ValidationError("Produk tidak tersedia dalam stok.")
        return data

    def create(self, validated_data):
        produk = validated_data['produk']

        # Mengurangi stok produk
        if produk.stok > 0:
            produk.stok -= 1
            produk.save()

            # Jika stok habis setelah pembelian, pindahkan ke Discount
            if produk.stok == 0:
                Discount.objects.create(
                    nama_produk=produk.nama_produk,
                    harga=produk.harga,
                    gambar=produk.gambar,  # Gambar tetap dipakai
                    harga_diskon=produk.harga * 0.8  # Misalnya: diskon 20%
                )
        else:
            raise serializers.ValidationError("Stok produk habis.")

        # Isi otomatis nama_produk dan harga dari produk
        validated_data['nama_produk'] = produk.nama_produk
        validated_data['harga'] = produk.harga

        return super().create(validated_data)

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
