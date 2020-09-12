from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm
from django.http import HttpResponseBadRequest
from .models import User


def home_view(request):
    return render(request, "index.html", {})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest()
        form.clean()
        user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user:
            login(request, user)
            return redirect("/")
    return render(request, "login.html", {})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")


def messages_view(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    return render(request, "messages.html", {})

"""
if request.method == "POST":
    ...
    User.objects.create_user(**form.cleaned_data)
    redirect("/login")
return render
"""