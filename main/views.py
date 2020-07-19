from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial

# Create your views here.


def home(request):
    return render(request, 'main/home.html', {"tutorials": Tutorial.objects.all()})
