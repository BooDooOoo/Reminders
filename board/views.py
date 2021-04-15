from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import UserRegisterForm, UserLoginForm, ReminderForm
from django.contrib import messages
from .models import Reminders
from django.contrib.auth.models import User

# Функция для регистрации нового пользователя
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'board/register.html', {'form': form})

# Функция для входа пользователя
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'board/login.html', {'form': form})

# Функция для выхода пользователя
def user_logout(request):
    logout(request)
    return redirect('login')

# Основная функция для вывода списка напоминаний, создания нового или изменения существующего
def index(request):

    # Если пользователь не вошёл, то выводим страницу с просьбой о входе
    if not request.user.is_authenticated:
        return render(request, 'board/not_ligin_index.html')

    # Получаем список уведомлений для текущего юзера, которые ещё не отправлены
    list_reminders = Reminders.objects.filter(user__username=request.user.username, is_notificated=False)

    # Если получаем POST запрос из формы
    if request.method == 'POST':
        form = ReminderForm(data=request.POST)

        # И форма прошла валидацию
        if form.is_valid():

            # При изменении напоминаня проверяем наличие записи в БД обновляем поля записи
            is_update_remind = Reminders.objects.filter(id=form.cleaned_data['id'])
            if is_update_remind:
                update_remind = is_update_remind[0]
                update_remind.title = form.cleaned_data['title']
                update_remind.date = form.cleaned_data['date']
                update_remind.time = form.cleaned_data['time']
                update_remind.save()

                return redirect('home')

            # Если записи в БД не нашлось, то создаём её и заполняем поля
            else:
                user_id = User.objects.get(username=request.user.username)
                new_remind = Reminders.objects.create(title=form.cleaned_data['title'],
                                                      date=form.cleaned_data['date'],
                                                      time=form.cleaned_data['time'],
                                                      user=user_id)
                new_remind.save()
                return redirect('home')

    # В ином случае получен POST запрос, возвращаем пустую форму и список напоминаний юзера
    else:
        form = ReminderForm()
    return render(request, 'board/index.html', {'reminders': list_reminders, 'form': form})

# Функция удаления напоминания
def delete_reminder(request, id_reminder):
    Reminders.objects.get(id=id_reminder).delete()
    return redirect('home')
