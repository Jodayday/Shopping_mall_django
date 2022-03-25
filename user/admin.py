from django.contrib import admin

# Register your models here.

# import models
from .models import User, Book, Author


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "level",)

    def changelist_view(self, request, extra_context=None):
        extra_context = {"title": "사용자 목록"}
        return super().changelist_view(request, extra_context)

    def change_view(self, request, object_id=None, form_url='', extra_context=None):
        email = User.objects.get(pk=object_id)
        extra_context = {'title': f'{email.email} 수정'}
        return super().change_view(request, object_id, form_url, extra_context)


admin.site.register(User, UserAdmin)


class BookInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]


admin.site.register(Author, AuthorAdmin)
