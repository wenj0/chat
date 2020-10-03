from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=1000)
    email = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000)


class MessageForm(forms.Form):
    text = forms.CharField()


class CreateChatForm(forms.Form):
    name = forms.CharField()


class ChatInviteForm(forms.Form):
    username = forms.CharField()
