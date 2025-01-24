from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('HOME 6')

def sobre(request):
    return HttpResponse('SOBRE')

def contacto(request):
    return HttpResponse('CONTACTO')