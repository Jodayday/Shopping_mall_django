from django.db import models

# Create your models here.


class User(models.Model):
    email = models.EmailField(verbose_name="이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    time = models.DateTimeField(auto_now_add=True, verbose_name="가입시간")

    class Meta:
        db_table = "user_table"
        verbose_name = "유저들"
        verbose_name_plural = "유저"

    def __str__(self) -> str:
        return self.email
