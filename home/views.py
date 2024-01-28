from django.shortcuts import render
from django.http import JsonResponse
#from .models import Billboard


def home(request):
    return render(request, 'home.html')


