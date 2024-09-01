from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})