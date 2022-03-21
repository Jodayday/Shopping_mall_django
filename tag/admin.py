from django.contrib import admin

# Register your models here.
from tag.models import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Tag, TagAdmin)
