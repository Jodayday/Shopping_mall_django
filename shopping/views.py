
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView
from django.db import transaction
# db 트렌젝션
from django.utils.decorators import method_decorator
# @ 데코레이터를 사용하기
from user.decorators import login_required, login_level


from shopping.forms import OrderForm, ProductForm
from shopping.models import Order, Product
from user.models import User
# Create your views here.


class ProductListView(ListView):
    model = Product
    # list 할 모델 선정
    template_name = "product/product.html"
    # 사용할 템플릿
    context_object_name = "products"
    # 사용할 탬플릿 태그명


@method_decorator(login_level, name="dispatch")
class ProductCreateView(FormView):
    template_name = "product/register_product.html"
    form_class = ProductForm
    success_url = "/shop/"

    def form_valid(self, form):
        _p = Product(
            name=form.data.get("name"),
            price=form.data.get("price"),
            description=form.data.get("description"),
            stock=form.data.get("stock"),
            # form.data.get의 요청은 필드
        )
        _p.save()
        return super().form_valid(form)
        # 오버라이딩 했던것이기에 부모의 함수를 호출


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


@method_decorator(login_required, name="dispatch")
class OrderView(FormView):
    form_class = OrderForm
    success_url = "/shop/"

    def form_valid(self, form):
        with transaction.atomic():
            # db 트렌젝션 설정
            p = Product.objects.get(pk=form.data.get("product"))
            order = Order(
                user=User.objects.get(pk=self.request.session.get('user')),
                product=p,
                quantity=form.data.get("quantity"),
            )
            order.save()
            p.stock -= int(form.data.get("quantity"))
            p.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # 실패했을때 동작함
        return redirect(reverse("shopping:detail", args=(form.data.get("product"),)))

    def get_form_kwargs(self, **kwargs):
        # 어떤인자값을 전달할지 설정하는 함수
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


@ method_decorator(login_required, name="dispatch")
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
