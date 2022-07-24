from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import BookMovieList, ListItem

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=100, required=True)
    email = forms.EmailField(label='Email', max_length=250, required=True, help_text='eg.banana@gmail.com')
    password1 = forms.CharField(label='Пароль', max_length=100, required=True, widget=forms.PasswordInput(), help_text='Минимум 8 символов и только латинские символы')
    password2 = forms.CharField(label='Повторите пароль', max_length=100, required=True, widget=forms.PasswordInput(), help_text='Минимум 8 символов')
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100, required=True)
    password = forms.CharField(label='Пароль', max_length=100, required=True, widget=forms.PasswordInput())

    class Meta:
        model = AuthenticationForm
        fields = ('username', 'password',)

class BookMovieListForm(forms.ModelForm):
    class Meta:
        model = BookMovieList
        fields = ('name', 'chapter')
        labels = {
            'name': 'Название',  
            'chapter': 'Раздел', 
        }

    

class ListItemForm(forms.ModelForm):
    year_of_issue = forms.DateField(label='Год выпуска', input_formats=['%Y'], widget=forms.TextInput(attrs={'maxlength': '4'}), required=False)
    day_complete = forms.DateField(label='День прочтения/просмотра', widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = ListItem
        fields = ('name', 'author', 'description', 'year_of_issue', 'day_complete', 'likes', 'chapter', 'bookmovieid')
        labels = {
            'name': 'Название', 
            'author': 'Автор/Режиссёр', 
            'description': 'Описание', 
            'likes': 'Выделить', 
            'chapter': 'Раздел', 
            'bookmovieid': 'Подраздел',
        }

    def __init__(self, user, *args, **kwargs):
        super(ListItemForm, self).__init__(*args, **kwargs)
        self.fields['bookmovieid'].queryset =  BookMovieList.objects.filter(user=user)