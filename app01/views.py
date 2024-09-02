from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Soy el index</h1>")

def vista1(request):
    return HttpResponse("Esta es la APP de Alejandro Merino.")

# Create your views here.
