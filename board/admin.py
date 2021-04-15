from django.contrib import admin
from django import forms
from .models import Reminders

class BoardAdminForm(forms.ModelForm):

    class Meta:
        model = Reminders
        fields = '__all__'

class BoardAdmin(admin.ModelAdmin):
    form = BoardAdminForm
    list_display = ('id', 'user', 'title', 'date', 'time', 'is_notificated')

# Регистрация в админке модели Reminders и вывод полей
admin.site.register(Reminders, BoardAdmin)
