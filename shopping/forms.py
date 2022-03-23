
from django import forms
from shopping.models import Product


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
