from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.http import JsonResponse


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

#Write a function to view each product

def item(request, pk):
    product = Product.objects.get(id=pk)
    
    
    return render(request, 'item.html', context={'product':product})

# Write a function to register user using the django admin auth
def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'You have Registered Succesfully {username} ��!')
            return redirect('login')
        else:
            messages.error(request, 'Whoops registration failed, please try again.')
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})


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


def category(request, cat):
    cat_products = Product.objects.filter(category__name=cat)
    categories = Category.objects.all()
    context = {'cat_products': cat_products, 'categories': categories}
    return render(request, 'category.html', context)