from django.core.mail import send_mail
from Reminders.celery import app
from .models import Reminders
from django.contrib.auth.models import User
from datetime import date, datetime, time
from celery import shared_task
from celery.utils.log import get_task_logger


@app.task
def send_reminders():
    '''
    Функция для отправки писем на E-mail с данными о напоминании,
    если наступило дата и время его отправки
    Функция работает в фоне с помощью библиотеки celery,
    запуск происходит раз в минуту
    '''

    # Из модели берутся ещё неотправленные напоминания с датой сегодня и ранее
    list_reminders_to_send = Reminders.objects.filter(is_notificated=False,
                                                      date__lte=date.today())

    for reminder_to_send in list_reminders_to_send:
        time_of_reminder = reminder_to_send.time

        # Время может быть не указано, в таком случае считаем его за 8:00
        if not time_of_reminder:
            time_of_reminder = time(hour=8)

        # Сравниваем системное время и время напоминания
        if time_of_reminder <= datetime.now().time():

            # Создаём тело письма
            message = f'Напоминание: {reminder_to_send.title} \n{reminder_to_send.date} в {time_of_reminder}'

            # Отправляем письмо
            is_send = send_mail(subject='Напоминание',
                                message=message,
                                from_email='vnbundin@gmail.com',
                                recipient_list=[User.objects.get(pk=reminder_to_send.user_id).email],
                                fail_silently=False)

            # Если письмо отправлено, отмечаем это в БД
            if is_send:
                reminder_to_send.is_notificated = True
                reminder_to_send.save()
