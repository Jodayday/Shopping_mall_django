from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from django.contrib.humanize.templatetags.humanize import intcomma
# import models
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'price_style', 'stock_style', "stock_status",)
    search_fields = ("name", "price",)

    def stock_style(self, obj):
        stock = intcomma(obj.stock)
        return f"{stock} 개"
    stock_style.short_description = "가격"

    def price_style(self, obj):
        price = intcomma(obj.price)
        return f"{price} 원"
    price_style.short_description = "가격"

    def stock_status(self, obj):
        if obj.stock < 2:
            return format_html(f"<b style='color:red;'>{obj.stock}</b>")
        elif obj.stock < 5:
            return format_html(f"<b style='color:green;'>{obj.stock}</b>")
        else:
            return format_html(f"<b>{obj.stock}</b>")
    stock_status.short_description = "재고상태"


class OrderAdmin(admin.ModelAdmin):
    list_filter = ("status",)
    # 필터 생성
    list_display = ("user", 'product', "quantity", 'status', 'styled_status')

    def styled_status(self, obj):
        # 함수를 만들어 등록가능
        if obj.status == "환불":
            return format_html(f"<b style='color:red;'>{obj.status}</b>")
        elif obj.status == "결제완료":
            return format_html(f"<b style='color:green;'>{obj.status}</b>")
        else:
            return format_html(f"<b>{obj.status}</b>")

    styled_status.short_description = "상태"
    # 함수의 헤더표시를 변경


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
