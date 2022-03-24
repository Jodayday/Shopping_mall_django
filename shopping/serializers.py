from rest_framework import serializers
# 데이터를 json으로 변경
from shopping.models import Product


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price', 'stock')
