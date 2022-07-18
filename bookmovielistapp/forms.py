from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=250, required=True, help_text='eg.banana@gmail.com')
    password1 = forms.CharField(label='Пароль', max_length=100, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повторите пароль', max_length=100, required=True, widget=forms.PasswordInput(), help_text='Минимум 8 символов')
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')