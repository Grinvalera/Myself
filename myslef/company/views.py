from django.shortcuts import render
from .models import Company, PictureCompany


def company(request):
    description = Company.objects.all()
    picture = PictureCompany.objects.all()
    return render(request, 'company.html', locals())
# Create your views here.
