from django.contrib import admin

# Register your models here.
from .models import BoardInfo


class BoardAdmin(admin.ModelAdmin):
    list_display = ("title", "writer", "register_time")


admin.site.register(BoardInfo, BoardAdmin)
