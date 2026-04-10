from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import User


def login_page(request):
    return render(request, 'login.html')


def signup_page(request):
    return render(request, 'signup.html')


# Signup

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if not username or not password or not role:
            return render(request, 'signup.html', {"error": "Required fields missing"})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {"error": "Username already exists"})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )

        auth_login(request, user)

        return redirect('home')

    return render(request, 'signup.html')


# Login

def api_login(request):
     if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)   
            return redirect('home')     

        return render(request, 'login.html', {'error': 'Invalid credentials'})

     return render(request, 'login.html')

