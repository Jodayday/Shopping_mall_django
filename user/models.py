from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(verbose_name="이메일")
    level = models.CharField(max_length=16, verbose_name="등급", choices=(
        ("admin", "관리자"),  # (값,표시)
        ("seller", "판매자"),
        ("buyer", "구매자"),
    ))
    password = models.CharField(max_length=128, verbose_name="비밀번호")
    time = models.DateTimeField(auto_now_add=True, verbose_name="가입시간")

    class Meta:
        db_table = "user_table"
        verbose_name = "유저들"
        verbose_name_plural = "유저"

    def __str__(self) -> str:
        return self.email
