from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm, MessageForm, CreateChatForm, ChatInviteForm
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from .models import User, Message, Chat, ChatRole


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


def chat_view(request, chat_id):
    if not request.user.is_authenticated:
        return redirect("/login")
    chat = get_object_or_404(Chat.objects.all(), id=chat_id)
    try:
        role = ChatRole.objects.get(chat=chat, user=request.user)
    except ChatRole.DoesNotExist:
        return HttpResponseForbidden("Forbidden")
    if request.method == "POST":
        form = MessageForm(data=request.POST)
        form.is_valid()
        Message.objects.create(text=form.cleaned_data["text"], chat=chat, user=request.user)
    return render(request, "chat.html", {
        "messages": Message.objects.filter(chat=chat).order_by('datetime_created'),
        "chat": chat,
        "role": role
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
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method == "POST":
        form = CreateChatForm(data=request.POST)
        form.is_valid()
        chat = Chat.objects.create(name=form.cleaned_data["name"])
        ChatRole.objects.create(user=request.user, chat=chat)
        return redirect("/chat/{}".format(chat.id))
    return render(request, "create_chat.html", {})


def chat_invite_view(request, chat_id):
    if not request.user.is_authenticated:
        return redirect("/login")
    chat = get_object_or_404(Chat.objects.all(), id=chat_id)
    try:
        role = ChatRole.objects.get(chat=chat, user=request.user)
    except ChatRole.DoesNotExist:
        return HttpResponseForbidden("Forbidden")
    if role.role != ChatRole.ROLE_CREATOR:
        return HttpResponseForbidden("Forbidden")
    if request.method == "POST":
        form = ChatInviteForm(data=request.POST)
        form.is_valid()
        try:
            user = User.objects.get_by_natural_key(form.cleaned_data["username"])
            ChatRole.objects.get_or_create(user=user, chat=chat)
            return redirect("/chat/{}".format(chat.id))
        except User.DoesNotExist:
            return HttpResponseBadRequest("No such user")
    return render(request, "chat_invite.html", {"chat": chat})


def chat_members_view(request, chat_id):
    if not request.user.is_authenticated:
        return redirect("/login")
    chat = get_object_or_404(Chat.objects.all(), id=chat_id)
    try:
        role = ChatRole.objects.get(chat=chat, user=request.user)
    except ChatRole.DoesNotExist:
        return HttpResponseForbidden("Forbidden")
    members = list(map(lambda r: r.user, ChatRole.objects.filter(chat=chat).order_by("user__username")))
    return render(request, "chat_members.html", {"chat": chat, "members": members, "is_creator": role.role == ChatRole.ROLE_CREATOR})


def chats_view(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    chats = list(map(lambda r: r.chat, ChatRole.objects.filter(user=request.user).order_by("chat__name")))
    return render(request, "chats.html", {"chats": chats})
