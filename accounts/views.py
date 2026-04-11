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

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {"error": "Username already exists"})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )
        
        user.role = role
        user.save()


        auth_login(request, user)

        return redirect('home')

    return render(request, 'signup.html')


# Login

def api_login(request):
     if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            auth_login(request, user)
            return redirect('home')

        return render(request, 'login.html', {'error': 'Invalid credentials'})

     return render(request, 'login.html')


# accounts/views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User


# def login_page(request):
#     return render(request, "login.html")


# def signup_page(request):
#     return render(request, "signup.html")


# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         if User.objects.filter(username=username).exists():
#             return render(request, "signup.html", {"error": "User already exists"})

#         User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )

#         return redirect("home")

#     return render(request, "signup.html")


# def api_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             return redirect("home")

#         return render(request, "login.html", {"error": "Invalid credentials"})


# def logout_view(request):
#     logout(request)
#     return redirect("login_page")