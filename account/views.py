from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth


# from .forms import RegistrationFrom


# Base view for app
def signup_view(request):
    if request.method == "POST":

        uname = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        if pass1 != pass2:
            return HttpResponse("Your password not same ")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect("login")

    return render(
        request,
        "account/signup.html",
    )


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("passw")
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return HttpResponse("incorect data")
    return render(request, "account/login.html")


def logout_view(request):
    auth.logout(request)
    return redirect("login")
