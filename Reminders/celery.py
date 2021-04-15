import os
from celery import Celery
from celery.schedules import crontab

# Настройка библиотеки celery, указание файла настроек
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Reminders.settings')
app = Celery('Reminders')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Указание поиска функций для запуска по всем приложениям
app.autodiscover_tasks()

# Регистрация функции отправки писем на выполнение каждую минуту
app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'board.tasks.send_reminders',
        'schedule': crontab(),
    },
}