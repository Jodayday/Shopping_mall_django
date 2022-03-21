from django.contrib import admin

# Register your models here.
from .models import BoardInfo, Tag


class BoardAdmin(admin.ModelAdmin):
    list_display = ("title", "writer", "register_time")


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Tag, TagAdmin)
admin.site.register(BoardInfo, BoardAdmin)
