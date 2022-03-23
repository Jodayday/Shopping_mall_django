
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView

from shopping.forms import OrderForm, ProductForm
from shopping.models import Order, Product

# Create your views here.


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
    # list 할 모델 선정 (모든 값이 나옴)
    # queryset = Product.objects.all()
    # 모델과 쿼리셋의 차이는 조건값만 할지 아닐지 정하는것
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


class ProductOrderView(ListView):
    template_name = "order/order.html"
    context_object_name = "Orders"

    def get_queryset(self):
        queryset = Order.objects.filter(
            user__pk=self.request.session.get('user'))
        # order_model의 user는 User_model의 포링키
        print(self.request.session.get('user'))
        return queryset
        # queryset를 오버라이딩 해서 재지정함
