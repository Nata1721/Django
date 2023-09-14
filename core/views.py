from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("<h1>HOME<h1>")

def carreras(request):
    return HttpResponse("<h1>CARRERAS<h1>")

def docentes(request):
    return HttpResponse("<h1>DOCENTES<h1>")
