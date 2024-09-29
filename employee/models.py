from django.db import models
import datetime


class Position(models.Model):
    """Таблица должностей."""

    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Team(models.Model):
    """Таблица команд."""
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name


class Competence(models.Model):
    """Таблица компетенций."""

    name = models.CharField(max_length=250)

    class Meta:
        ordering = ['name']
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Таблица навыков."""

    DOMAIN = [
        ('Hard skills', 'Hard skills'),
        ('Soft skills', 'Soft skills'),
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
    """Таблица сотрудников."""

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
    grade = models.CharField(max_length=8, choices=GRADE, default=GRADE[0])
    date_last_rating = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['fio',]
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.fio


class Rating(models.Model):
    """Таблица оценок навыков, компетенций."""

    RATING = [
        ('Не оценивался', 'Не оценивался'),
        ('Не владеет', 'Не владеет'),
        ('Базовый', 'Базовый'),
        ('Уверенный', 'Уверенный'),
        ('Экспертный', 'Экспертный'),
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
    rating = models.CharField(max_length=13, choices=RATING, default=RATING[0])
    key_people = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['fio', 'skill',]
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return (
            f'оценка {self.fio.fio} по {self.skill.name}, '
            f'{self.competence.name} на '
            f'{self.updated.strftime("%d.%m.%Y")} -- {self.rating}!'
        )
