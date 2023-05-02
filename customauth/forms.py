from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Login",
        "autofocus": "",}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password"}))


class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
