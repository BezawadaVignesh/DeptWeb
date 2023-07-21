from django.shortcuts import render, HttpResponse
from django.contrib import messages


def home(request):
    return HttpResponse("Hello World")

