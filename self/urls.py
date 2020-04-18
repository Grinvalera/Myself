from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/', include('car.urls')),
    path('company/', include('company.urls')),
    path('cat/', include('cat.urls'))
]