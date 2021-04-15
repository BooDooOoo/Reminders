from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Reminders

# Форма для регистрации нового пользователя
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Форма для входа
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# Форма для создания или изменения полей напоминания
class ReminderForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    date = forms.DateField(initial='Set Date', input_formats=['%b %d, %Y'])
    date.widget.attrs.update({'class': 'form-control btn formDatepicker px-0',
                              'type': "button",
                              'id': "datepicker",
                              })
    time = forms.TimeField(initial='Set Time', input_formats=['%I:%M %p'], required=False)
    time.widget.attrs.update({'class': 'form-control btn formTimepicker px-0',
                              'id': 'timepicker'
                              })

    class Meta:
        model = Reminders
        fields = ['id', 'title', 'date', 'time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
