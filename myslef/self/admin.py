from django.contrib import admin
from .models import Valera, Photo


class ValeraAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'picture']

    class Meta:
        model = Valera


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['photo']

    class Meta:
        model = Photo


admin.site.register(Valera, ValeraAdmin)
admin.site.register(Photo, PhotoAdmin)
# Register your models here.
