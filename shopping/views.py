from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView

# Create your views here.

from shopping.models import Product, Order
from shopping.forms import ProductForm, OrderForm


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
    # queryset = Product.objects.all()
    # 모델과 쿼리셋의 차이는 뭘까?
    template_name = "product/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        # 값을 추가하고 싶을때
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm()
        return context


class OrderView(FormView):
    form_class = OrderForm
    success_url = "/shop/"
