from this import d
from django.shortcuts import redirect, render
from .forms import SignUpForm, LoginForm, BookMovieListForm, ListItemForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import BookMovieList, ListItem
# Create your views here.
def home(request):
    return render(request, 'bookmovielistapp/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = User.objects.filter(email=form.cleaned_data['email'])
            if not email.exists():
                form.save()
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('current')
            else:
                return render(request, 'bookmovielistapp/signup.html', {'form': SignUpForm(), 'error': 'Пользователь с таким адресом уже существует'})
        else:
            if request.POST['password1'] != request.POST['password2']:
                return render(request, 'bookmovielistapp/signup.html', {'form': SignUpForm(), 'error': 'Пароли не совпадают'})
            elif User.objects.filter(username=request.POST.get('username')).exists():
                return render(request, 'bookmovielistapp/signup.html', {'form': SignUpForm(), 'error': 'Пользователь с таким именем уже существует'})
    return render(request, 'bookmovielistapp/signup.html', {'form': SignUpForm()})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('current')
        else:
            if not User.objects.filter(username=request.POST.get('username')).exists():
                return render(request, 'bookmovielistapp/login.html', {'form':LoginForm(), 'error': 'Такого пользователя не существует'})
            else:
                return render(request, 'bookmovielistapp/login.html', {'form':LoginForm(), 'error': 'Неверный пароль'})
    return render(request, 'bookmovielistapp/login.html', {'form':LoginForm()})

def currentlist(request):
    create_lists = BookMovieList.objects.filter(user=request.user)
    create_elem = ListItem.objects.filter(user=request.user)
    if request.method == 'POST' and 'create_lists' in request.POST:
        form = BookMovieListForm(request.POST)
        newlist = form.save(commit=False)
        newlist.user = request.user
        newlist.save()
        return redirect('current')
    if request.method == 'POST' and 'create_elem' in request.POST:
        try:
            form = ListItemForm(request.POST)
            newelem = form.save(commit=False)
            newelem.user = request.user
            newelem.save()
            return redirect('current')
        except ValueError:
            return render(request, 'bookmovielistapp/currentlist.html', {'form1': BookMovieListForm(), 'form2': ListItemForm(), 'lists': create_lists, 'elems': create_elem, 'error':'Не правильные данные'})
    return render(request, 'bookmovielistapp/currentlist.html', {'form1': BookMovieListForm(), 'form2': ListItemForm(), 'lists': create_lists, 'elems': create_elem})
