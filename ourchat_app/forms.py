from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000)


class RegisterForm(forms.Form):
    pass