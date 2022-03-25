
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="상품명")
    price = models.IntegerField(verbose_name="가격")
    description = models.TextField(verbose_name="설명")
    stock = models.IntegerField(verbose_name="재고",)
    time = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")

    class Meta:
        db_table = "product_table"
        verbose_name = "상품"
        verbose_name_plural = "상품목록"

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name="구매자")
    product = models.ForeignKey(
        'shopping.Product', on_delete=models.CASCADE, verbose_name="상품")
    quantity = models.IntegerField(verbose_name="수량")
    status = models.CharField(
        choices=(
            ('대기중', '대기중'),
            ('결제대기', '결제대기'),
            ('결제완료', '결제완료'),
            ('환불', '환불'),
            # db표기, admin표기
        ),
        max_length=32, verbose_name="상태", default='대기중')
    memo = models.TextField(verbose_name="메모", null=True, blank=True,)
    # null,blank >> True 입력을 해도되고 안해도 되고 설정
    time = models.DateTimeField(auto_now_add=True, verbose_name="주문시간")

    class Meta:
        db_table = "Order_table"
        verbose_name = "주문"
        verbose_name_plural = "주문목록"

    def __str__(self):
        return "{} -> {} 주문".format(self.user, self.product)
