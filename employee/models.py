from django.db import models
from datetime import date


class Position(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name


class Competence(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'

    def __str__(self):
        return self.name


class Skill(models.Model):
    DOMAIN = [
        ('Hard_skills', 'Hard skills'),
        ('Soft_skills', 'Soft skills'),
    ]
    name = models.CharField(max_length=250)
    domain = models.CharField(max_length=12, choices=DOMAIN)
    competence = models.ForeignKey(
        Competence,
        verbose_name='Компетенция',
        on_delete=models.SET_NULL,
        related_name='skill',
        null=True,
        blank=False,
        )

    class Meta:
        ordering = ['name']
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Employee(models.Model):
    GRADE = [
        ('No value', 'No value'),
        ('Junior', 'Junior'),
        ('Middle', 'Middle'),
        ('Senior', 'Senior'),
    ]

    fio = models.CharField(max_length=250)
    position = models.ForeignKey(
        Position,
        verbose_name='Должность',
        on_delete=models.SET_NULL,
        related_name='employee',
        null=True,
        blank=False,    
    )
    team = models.ForeignKey(
        Team,
        verbose_name='Команда',
        on_delete=models.SET_NULL,
        related_name='employee',
        null=True,
        blank=False,
    )
    graide = models.CharField(max_length=8, choices=GRADE, default=GRADE[0])

    class Meta:
        ordering = ['fio',]
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fio 


class Rating(models.Model):
    RATING = [
        ('no_value', 'Не оценивался'),
        ('lack', 'Не владеет'),
        ('base', 'Базовый'),
        ('confident', 'Уверенный'),
        ('expert', 'Экспертный'),
    ]
    DOMAIN = [
        ('Hard_skills', 'Hard skills'),
        ('Soft_skills', 'Soft skills'),
    ]

    fio = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name='Сотрудник'
    )
    skill = models.ForeignKey(
        Skill,
        verbose_name='Навык',
        on_delete=models.SET_NULL,
        related_name='employee',
        null=True,
        blank=False,
    )
    competence = models.ForeignKey(
        Competence,
        verbose_name='Компетенция',
        on_delete=models.SET_NULL,
        related_name='employee',
        null=True,
        blank=False,
    )
    rating = models.CharField(max_length=12, choices=RATING, default=RATING[0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['fio','skill',]
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
    
    def __str__(self):
        return (
            f'оценка {self.fio.fio} по {self.skill.name}, '
            f'{self.competence.name} на '
            f'{self.updated.strftime("%d.%m.%Y")} -- {self.rating}!'       
        )
