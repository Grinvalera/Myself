from django.contrib import admin
from .models import Cat, PhotoCat


class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']

    class Meta:
        model = Cat


class PhotoCatAdmin(admin.ModelAdmin):
    list_display = ['id']

    class Meta:
        model = PhotoCat


admin.site.register(PhotoCat, PhotoCatAdmin)
admin.site.register(Cat, CatAdmin)
# Register your models here.
