from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, 'bookmovielistapp/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = User.objects.filter(email=form.cleaned_data['email'])
            print(form.cleaned_data['username'])
            if not email.exists():
                form.save()
            else:
                return render(request, 'bookmovielistapp/signup.html', {'form': SignUpForm(), 'error': 'Пользователь с таким адресом уже существует'})
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'bookmovielistapp/signup.html', {'form': SignUpForm(), 'error': 'Пароли не совпадают'})
        elif User.objects.filter(username=request.POST.get('username')).exists():
            return render(request, 'bookmovielistapp/signup.html', {'form': SignUpForm(), 'error': 'Пользователь с таким именем уже существует'})
    return render(request, 'bookmovielistapp/signup.html', {'form': SignUpForm()})