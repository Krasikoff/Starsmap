# Generated by Django 4.2 on 2024-10-07 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.ManyToManyField(related_name='user', to='employee.team', verbose_name='Команда'),
        ),
    ]
