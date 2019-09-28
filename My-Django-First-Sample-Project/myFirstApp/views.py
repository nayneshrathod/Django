from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h1>WElcome Hello Method</h1>");


def msg(request):
    return HttpResponse("<h1>This is Hellow def</h1>");


def tp(request):
    return HttpResponse("<h1>this is also usr timepass</h1>");