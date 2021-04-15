from django.db import models
from django.contrib.auth.models import User

class Reminders(models.Model):
    title = models.CharField(max_length=150, verbose_name='Текст уведомления')
    date = models.DateField(verbose_name='Дата уведомления')
    time = models.TimeField(blank=True, null=True, verbose_name='Время уведомления')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    is_notificated = models.BooleanField(default=False, verbose_name='Напоминание отправлено?')

    def __str__(self):
        return self.title
