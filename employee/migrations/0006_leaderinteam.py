# Generated by Django 4.2 on 2024-10-05 16:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_lastrating_options_remove_team_leader'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderInTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaderinteam', to=settings.AUTH_USER_MODEL)),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='leaderinteam', to='employee.team')),
            ],
            options={
                'verbose_name': 'Лидер',
                'verbose_name_plural': 'Лидеры',
                'ordering': ['team'],
            },
        ),
    ]
