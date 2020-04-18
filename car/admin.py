from django.contrib import admin
from .models import Car, Picture


class CarAdmin(admin.ModelAdmin):
    list_display = ['description']

    class Meta:
        model = Car


class PictureAdmin(admin.ModelAdmin):
    list_display = ['photo']

    class Meta:
        model = Picture


admin.site.register(Picture, PictureAdmin)
admin.site.register(Car, CarAdmin)
# Register your models here.
