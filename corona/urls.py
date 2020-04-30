from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from corona import views


def home(request):
    return render(request, 'home_corona.html')


urlpatterns = [
    path('', home, name='home'),
    path('ac/', views.active_count, name='ac'),
    path('cd/', views.cured_discharged, name='cd'),
    path('d/', views.death, name='d'),
    path('m/', views.migrate, name='m'),
]
