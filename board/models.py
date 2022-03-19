from django.db import models

# Create your models here.


class BoardInfo(models.Model):
    "db 테이블 필드 설정 id는 자동으로 추가됨"
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey(
        'userconfig.UserInfo', on_delete=models.CASCADE, verbose_name="작성자")
    # 다른 모델의 값을 참조 포링키
    register_time = models.DateTimeField(
        auto_now_add=True, verbose_name="작성시간")

    def __str__(self):
        "클래스 문자로 변경시 표시될 값"
        return self.title

    class Meta:
        db_table = 'Board_table'
        "db테이블 이름 정의"
        verbose_name = "게시글"
        "개별사용자 명칭"
        verbose_name_plural = "게시판"
        "복수사용자 명칭"
