from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'recipes/home.html', context={'name':'Roberto'})

def sobre(request):
    return HttpResponse('SOBRE')

def contacto(request):
    return render(request, 'me-apague/temp.html')