from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} is created successfully as patient')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})
