from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import BookMovieList, ListItem

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'input-style input-login input-registration', 'placeholder':'\ue971'}))
    email = forms.EmailField(label='Email', max_length=250, required=True, help_text='eg.banana@gmail.com', widget=forms.EmailInput(attrs={'class': 'input-style input-email input-registration', 'placeholder':'\ue945'}))
    password1 = forms.CharField(label='Введите пароль', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'input-style input-pass input-registration input-registration_pass1', 'placeholder':'\ue98f'}), help_text='Минимум 8 символов и только латинские символы')
    password2 = forms.CharField(label='Повторите пароль', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'input-style input-pass input-registration input-registration_pass2', 'placeholder':'\ue98f'}))
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'mb-20px input-style input-login input-registration', 'placeholder':'\ue971'}))
    password = forms.CharField(label='Пароль', max_length=100, required=True, widget=forms.PasswordInput(attrs={'class': 'mb-20px input-style input-pass input-registration', 'placeholder':'\ue98f'}))

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
        widgets = {
            'name': forms.TextInput(attrs={'class':'mb-20px input-style input-form'}),
            'chapter': forms.Select(attrs={'class': 'mb-20px input-style'})
        }

    

class ListItemForm(forms.ModelForm):
    year_of_issue = forms.DateField(label='Год выпуска', input_formats=['%Y'], widget=forms.TextInput(attrs={'class': 'mb-10px input-style input-form', 'maxlength': '4'}), required=False)
    day_complete = forms.DateField(label='День прочтения/просмотра', widget=forms.DateInput(attrs={'class': 'mb-10px input-style', 'type': 'date'}), required=False)
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
        widgets = {
            'name': forms.TextInput(attrs={'class':'mb-10px input-style input-form'}),
            'author': forms.TextInput(attrs={'class':'mb-10px input-style input-form'}),
            'description': forms.Textarea(attrs={'class':'mb-10px input-style textarea input-form'}),
            'likes': forms.CheckboxInput(attrs={'class':'mb-10px input-style'}),
            'chapter': forms.Select(attrs={'class':'mb-10px input-style'}),
            'bookmovieid': forms.Select(attrs={'class': 'mb-10px input-style'})
        }

    def __init__(self, user, *args, **kwargs):
        super(ListItemForm, self).__init__(*args, **kwargs)
        self.fields['bookmovieid'].queryset =  BookMovieList.objects.filter(user=user)