"""bookmovielist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookmovielistapp import views
from django.contrib.auth import views as auth_views
from bookmovielistapp.forms import UserPasswordResetForm, UserSetPasswormForm, UserPasswordChangeForm

urlpatterns = [
    path('admin/', admin.site.urls),
    # Домашняя страница
    path('', views.home, name='home'),
    # Регистрация
    path('signup', views.signup, name='signup'),
    # Вход
    path('login', views.loginuser, name='loginuser'),
    # Выход
    path('logout', views.logoutuser, name='logoutuser'),
    # Страница личного списка
    path('current', views.currentlist, name='current'),
    # Удаление элемента
    path('current/<int:elem_pk>/elemdelete', views.elemdelete, name='elemdelete'),
    # Удаление списка
    path('current/<int:list_pk>/listdelete', views.listdelete, name='listdelete'),
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html', form_class=UserPasswordChangeForm), name="password_change"),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name="password_change_done"),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html', form_class=UserPasswordResetForm), name="password_reset"),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html', form_class=UserSetPasswormForm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
