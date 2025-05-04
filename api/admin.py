from django.contrib import admin
from .models import Users, Product, Order, Discount, ContactUs

admin.site.register(Users)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(ContactUs)
