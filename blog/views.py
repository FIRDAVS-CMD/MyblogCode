from django.http import HttpResponse
from django.shortcuts import render


def hello(request):  # new
    return HttpResponse("<h1>Hello world</h1>")
