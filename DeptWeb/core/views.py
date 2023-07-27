from django.shortcuts import render, HttpResponse
from django.contrib import messages


def home(request):
    return render(request, 'dist/index.html')

