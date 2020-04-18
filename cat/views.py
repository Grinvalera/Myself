from django.shortcuts import render
from .models import Cat, PhotoCat


def work(request):
    description = Cat.objects.all()
    photo = PhotoCat.objects.all()
    return render(request, 'cat.html', locals())
# Create your views here.
