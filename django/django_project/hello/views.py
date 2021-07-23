from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def menna(request):
    return HttpResponse("Menna is Happy")


def mama(request):
    return HttpResponse("Mama is in my heart")

def hello_pepole(request, name):
    return HttpResponse(f"you are welcome here {name.capitalize()}")
