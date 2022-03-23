
from django import forms
from shopping.models import Product, Order
from user.models import User
from django.db import transaction


class ProductForm(forms.Form):
    name = forms.CharField(max_length=128, label="상품명",
                           error_messages={'required': "상품명을 입력해주세요."})
    price = forms.IntegerField(label="가격",
                               error_messages={'required': "가격을 입력해주세요."})
    description = forms.CharField(label="설명",
                                  error_messages={'required': "설명을 입력해주세요."})
    stock = forms.IntegerField(label="재고",
                               error_messages={'required': "재고를 입력해주세요."})

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        if name and price and description and stock:
            _p = Product(
                name=name,
                price=price,
                description=description,
                stock=stock,
            )
            _p.save()


class OrderForm(forms.Form):
    product = forms.IntegerField(label="상품", widget=forms.HiddenInput)
    quantity = forms.IntegerField(label="수량",)

    def __init__(self, request, *args, **kwargs):
        # request를 폼에서 엑세스하기 위해 가져옴
        super().__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get("product")
        quantity = cleaned_data.get("quantity")
        user = self.request.session.get('user')

        if product and quantity and user:
            with transaction.atomic():
                # db 트렌젝션 설정
                p = Product.objects.get(pk=product)
                order = Order(
                    user=User.objects.get(pk=user),
                    product=p,
                    quantity=quantity,
                )
                order.save()
                p.stock -= quantity
                p.save()
        else:
            self.product = product
            self.add_error("quantity", "구매할 수량을 입력해주세요.")
