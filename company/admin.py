from django.contrib import admin
from .models import Company, PictureCompany


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['description']

    class Meta:
        model = Company


class PictureCompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo']

    class Meta:
        model = PictureCompany


admin.site.register(PictureCompany, PictureCompanyAdmin)
admin.site.register(Company, CompanyAdmin)
# Register your models here.
