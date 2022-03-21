

from django.contrib import admin

# Register your models here.
from .models import UserInfo


class UserAdmin(admin.ModelAdmin):
    "관리자 페이지에 유저모델 등록 클래스"
    list_display = ('user_name', 'user_email', 'password',)
    "관리자 페이지에서 추가적인 정보 표시"


admin.site.register(UserInfo, UserAdmin)
