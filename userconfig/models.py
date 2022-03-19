from django.db import models

# Create your models here.


class UserInfo(models.Model):
    "db 테이블 필드 설정 id는 자동으로 추가됨"
    user_name = models.CharField(max_length=64, verbose_name="사용자명")
    user_email = models.EmailField(max_length=128, verbose_name="이메일")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    register_time = models.DateTimeField(
        auto_now_add=True, verbose_name="가입시간")

    def __str__(self):
        "클래스 문자로 변경시 표시될 값"
        return self.user_name

    class Meta:
        db_table = 'UserInfo_table'
        "db테이블 이름 정의"
        verbose_name = "사용자"
        "개별사용자 명칭"
        verbose_name_plural = "사용자들"
        "복수사용자 명칭"
