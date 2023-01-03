from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
       username = request.POST["username"]
       password = request.POST["password"]
       user =  authenticate(request, username=username, password=password)
       
       if user is not None:
           login(request, user)
           return redirect("home")
       else:
           return render(request, "account/login.html", {
               "error": "username or password incorrect"
           })
       
    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
       username = request.POST["username"]
       email = request.POST["email"]
       firstName = request.POST["firstName"]
       lastName = request.POST["lastName"]
       password = request.POST["password"]
       repassword = request.POST["repassword"]
       
       if password == repassword:
           if User.objects.filter(username=username).exists():
               return render(request, "account/register.html", {"error": "username already exists"})
           else:
               if User.objects.filter(email = email).exists():
                   return render(request, "account/register.html", {"error": "email already exists"})
               else:
                   user = User.objects.create_user(username=username, email=email, first_name=firstName, last_name=lastName, password=password)
                   user.save()
                   return redirect("login")
       else:
           return render(request, "account/register.html", {"error": "password and re-password not match"})
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home") 