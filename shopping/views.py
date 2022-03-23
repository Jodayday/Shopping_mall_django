
from django.shortcuts import redirect, render
from django.views.generic import ListView, FormView, DetailView
from django.urls import reverse
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
        context['form'] = OrderForm(self.request)
        # 폼클래스 생성하면서 request전달
        return context
        # 해당을 추가함으로써 detaill.html에 form 속성을 사용할수있음


class OrderView(FormView):
    form_class = OrderForm
    success_url = "/shop/"

    def form_invalid(self, form):
        # 실패했을때 동작함
        return redirect(reverse("shopping:detail", args=(form.product,)))

    def get_form_kwargs(self, **kwargs):
        # 어떤인자값을 전달할지 설정하는 함수
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw
