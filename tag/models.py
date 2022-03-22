
from django.db import models

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name="태그")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="생성시간")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "TagInfo_table"
        verbose_name = "태그"
        verbose_name_plural = "태그들"
