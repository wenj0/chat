from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, MessageForm, CreateChatForm
from django.http import HttpResponseBadRequest
from .models import User, Message, Chat


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
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        form.is_valid()
        Message.objects.create(text=form.cleaned_data["text"], user=request.user)
    return render(request, "messages.html", {
        "messages": Message.objects.all()
    })


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        form.is_valid()
        User.objects.create_user(username=form.cleaned_data["username"], email=form.cleaned_data["email"],
                                 password=form.cleaned_data["password"])
        return redirect("/login")
    return render(request, "register.html", {})


def create_chat_view(request):
    if request.method == "POST":
        form = CreateChatForm(data=request.POST)
        form.is_valid()
        chat = Chat.objects.create(name=form.cleaned_data["name"])
        return redirect("/chat/{}/".format(chat.id))
    return render(request, "create_chat.html", {})