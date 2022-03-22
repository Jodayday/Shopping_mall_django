from django.contrib import admin

# Register your models here.

# import models
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'price', 'stock',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", 'product', "quantity")


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
