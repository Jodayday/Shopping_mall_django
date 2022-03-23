from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from shopping.models import Product, Order


class ProductListView(ListView):
    model = Product
    # list 할 모델 선정
    template_name = "product/product.html"
    # 사용할 템플릿
    context_object_name = "products"
    # 사용할 탬플릿 태그명
