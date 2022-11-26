from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    repeat_password = forms.CharField(widget=forms.PasswordInput, min_length=8)
