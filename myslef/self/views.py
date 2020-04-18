from django.shortcuts import render
from .models import Valera


def home(request):
    all_me = Valera.objects.all()
    return render(request, 'myself.html', locals())
# Create your views here.
