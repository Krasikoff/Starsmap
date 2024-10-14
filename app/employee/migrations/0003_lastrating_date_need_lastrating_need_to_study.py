# Generated by Django 4.2 on 2024-10-14 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_user_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastrating',
            name='date_need',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата запроса обучения'),
        ),
        migrations.AddField(
            model_name='lastrating',
            name='need_to_study',
            field=models.BooleanField(default=False, verbose_name='Требуется обучение'),
        ),
    ]
