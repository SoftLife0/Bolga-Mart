from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def item(request):
    products = Product.objects.all()
    return render(request, 'item.html', context={'products':products})

# Write a function to register user using the django admin auth
def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Account created successfully. Please login.')
        return redirect('login')
    else:
        return render(request, 'register.html', {})


# Write a function to login user using the django admin auth
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user = user.username
            messages.success(request, f'Welcome Back {user} 😊!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid login, please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html', {})    


def logout_user(request):
    logout(request)
    messages.success(request, 'Thanks for stopping by 👋')
    return redirect('login')