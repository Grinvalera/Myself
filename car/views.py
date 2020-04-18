from django.shortcuts import render
from .models import Car, Picture


def car(request):
    auto = Car.objects.all()
    auto_photo = Picture.objects.all()
    return render(request, 'car.html', locals())
# Create your views here.
