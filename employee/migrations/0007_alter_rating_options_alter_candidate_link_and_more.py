# Generated by Django 4.2 on 2024-10-06 13:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_leaderinteam'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rating',
            options={'ordering': ['last_rating', '-date_score'], 'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.AlterField(
            model_name='candidate',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to='employee.vacancy', verbose_name='Вакансия'),
        ),
        migrations.AlterField(
            model_name='competence',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='lastrating',
            name='last_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата последней оценки'),
        ),
        migrations.AlterField(
            model_name='lastrating',
            name='last_match',
            field=models.BooleanField(default=False, verbose_name='Соответствие на последнюю дату'),
        ),
        migrations.AlterField(
            model_name='leaderinteam',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leaderinteam', to=settings.AUTH_USER_MODEL, verbose_name='Лидер'),
        ),
        migrations.AlterField(
            model_name='leaderinteam',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leaderinteam', to='employee.team', verbose_name='Команда'),
        ),
        migrations.AlterField(
            model_name='position',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='chief_proof',
            field=models.BooleanField(default=False, verbose_name='Навык подтвержден руководителем'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='date_end',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата окончания обучения'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='date_need',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата запроса обучения'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='date_score',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата оценки'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='date_start',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата начала обучения'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='match',
            field=models.BooleanField(default=False, verbose_name='Соответствие'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='need_to_study',
            field=models.BooleanField(default=False, verbose_name='Требуется обучение'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.IntegerField(choices=[(0, 'Не оценивался'), (1, 'Не владеет'), (2, 'Начинающий'), (3, 'Базовый'), (4, 'Уверенный'), (5, 'Экспертный')], default=(0, 'Не оценивался'), verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='domain',
            field=models.CharField(choices=[('Hard skills', 'Hard skills'), ('Soft skills', 'Soft skills')], max_length=12, verbose_name='Домен'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_fire',
            field=models.DateField(blank=True, null=True, verbose_name='Уволен'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_hire',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Принят'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=250, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('No value', 'No value'), ('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior')], default=('No value', 'No value'), max_length=8, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=250, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('hr', 'HR'), ('team_chief', 'Руководитель'), ('user', 'Пользователь')], default='user', max_length=10, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='closed',
            field=models.BooleanField(default=False, verbose_name='Вакансия закрыта'),
        ),
    ]
