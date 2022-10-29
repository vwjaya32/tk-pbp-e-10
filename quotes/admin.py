from django.contrib import admin
from .models import Image


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


# Register your models here.
admin.site.register(Image, ImageAdmin)
