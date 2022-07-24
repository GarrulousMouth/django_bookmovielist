from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import redirect, render, get_object_or_404
from .forms import SignUpForm, LoginForm, BookMovieListForm, ListItemForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import BookMovieList, ListItem, Chapter

# Обработка перехода на домашнюю страницу
def home(request):
    return render(request, 'bookmovielistapp/index.html')

# Регистрация
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # Проверка формы
        if form.is_valid():
            email = User.objects.filter(email=form.cleaned_data['email'])
            # Проверка на email в базе данных
            if not email.exists():
                # Сохранение формы с последующим входом
                form.save()
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
                login(request, user)
                return redirect('current')
            else:
                return render(request, 'registration/signup.html', {'form': SignUpForm(), 'error': 'Пользователь с таким адресом уже существует'})
        else:
            # Обработка ошибки несоответствия паролей
            if request.POST['password1'] != request.POST['password2']:
                return render(request, 'registration/signup.html', {'form': SignUpForm(), 'error': 'Пароли не совпадают'})
            # Проверка на зарегистрированного пользователя
            elif User.objects.filter(username=request.POST.get('username')).exists():
                return render(request, 'registration/signup.html', {'form': SignUpForm(), 'error': 'Пользователь с таким именем уже существует'})
    # Переход GET-запроса
    return render(request, 'registration/signup.html', {'form': SignUpForm()})

# Выход из учётной записи
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

# Вход в учётную запись
def loginuser(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # Аутентификация пользователя и вход при наличии пользователя
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('current')
            else:
                # Обработка несуществующего пользователя
                if not User.objects.filter(username=request.POST.get('username')).exists():
                    return render(request, 'registration/login.html', {'form':LoginForm(), 'error': 'Такого пользователя не существует'})
                # Обработка неверного пароля
                else:
                    return render(request, 'registration/login.html', {'form':LoginForm(), 'error': 'Неверный пароль'})
    return render(request, 'registration/login.html', {'form':LoginForm()})

def currentlist(request):
    # Фильтрация элементов таблицы, принадлежащих пользователю
    create_lists = BookMovieList.objects.filter(user=request.user)
    create_elem = ListItem.objects.filter(user=request.user)
    chapters = Chapter.objects.select_related().all()
    # Полчение AJAX-запроса и отправка ответа
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        result = request.GET.get('send_data')
        bookmovieid = BookMovieList.objects.filter(chapter=result, user=request.user)
        return JsonResponse(serializers.serialize("json", bookmovieid), safe=False)
    # Добавление нового раздела
    if request.method == 'POST' and 'create_list' in request.POST:
        form = BookMovieListForm(request.POST, prefix='lists')
        newlist = form.save(commit=False)
        # Присвоение раздела зарегистрированному пользователю
        newlist.user = request.user
        newlist.save()
        return redirect('current')
    # Добавление элемента в раздел
    if request.method == 'POST' and 'create_elem' in request.POST:
        try:
            form = ListItemForm(request.user, request.POST, prefix='elems')
            newelem = form.save(commit=False)
            # Присвоение элемента зарегистрированному пользователю
            newelem.user = request.user
            newelem.save()
            return redirect('current')
        except ValueError:
            return render(request, 'bookmovielistapp/currentlist.html', {'form1': BookMovieListForm(prefix='lists'), 'form2': ListItemForm(request.user, prefix='elems'), 'lists': create_lists, 'chapters': chapters, 'elems': create_elem, 'error':'Не правильные данные'})
    # GET-запрос с передачей списков и элементов пользователя
    return render(request, 'bookmovielistapp/currentlist.html', {'form1': BookMovieListForm(prefix='lists'), 'form2': ListItemForm(request.user, prefix='elems'), 'lists': create_lists, 'chapters': chapters, 'elems': create_elem})

def elemdelete(request, elem_pk):
    elem = get_object_or_404(ListItem, pk=elem_pk, user=request.user)
    if request.method == 'POST':
        elem.delete()
        return redirect('current')

def listdelete(request, list_pk):
    listelems = get_object_or_404(BookMovieList, pk=list_pk, user=request.user)
    if request.method == 'POST':
        listelems.delete()
        return redirect('current')

