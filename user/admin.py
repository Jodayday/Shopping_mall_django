from django.contrib import admin

# Register your models here.

# import models
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "email",)


admin.site.register(User, UserAdmin)
