# Generated by Django 3.1.7 on 2021-04-05 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20210406_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminders',
            name='time',
            field=models.TimeField(blank=True, null=True, verbose_name='Время уведомления'),
        ),
    ]
