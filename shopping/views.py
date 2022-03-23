from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView

# Create your views here.

from shopping.models import Product, Order
from shopping.forms import ProductForm


class ProductListView(ListView):
    model = Product
    # list 할 모델 선정
    template_name = "product/product.html"
    # 사용할 템플릿
    context_object_name = "products"
    # 사용할 탬플릿 태그명


class ProductCreateView(FormView):
    template_name = "product/register_product.html"
    form_class = ProductForm
    success_url = "/shop/"


class ProductDetail(DetailView):
    model = Product
    template_name = "product/product_detail.html"
    context_object_name = "product"
    # queryset = Product.objects.all()
