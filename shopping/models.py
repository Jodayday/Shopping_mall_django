from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name="상품명")
    price = models.IntegerField(verbose_name="가격")
    description = models.TextField(verbose_name="설명")
    stock = models.IntegerField(verbose_name="재고", default=0)
    time = models.DateTimeField(auto_now_add=True, verbose_name="작성시간")

    class Meta:
        db_table = "product_table"
        verbose_name = "상품들"
        verbose_name_plural = "상품"

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name="구매자")
    product = models.ForeignKey(
        'shopping.Product', on_delete=models.CASCADE, verbose_name="상품")
    quantity = models.IntegerField(verbose_name="수량")
    time = models.DateTimeField(auto_now_add=True, verbose_name="주문시간")

    class Meta:
        db_table = "Order_table"
        verbose_name = "주문들"
        verbose_name_plural = "주문"

    def __str__(self):
        return "{} -> {} 주문".format(self.user, self.product)
