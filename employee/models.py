import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from employee.constants import DOMAIN, GRADE, RATING, ROLE_CHOICES, USER


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
    leader = models.CharField(max_length=250, blank=True, null=True)

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
        return (
            f'{self.name[:20]}...' 
            if len(self.name) > 20 else
            f'{self.name[:20]}'
        )


class User(AbstractUser):
    """Таблица сотрудников."""

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_hire = models.DateField(default=datetime.datetime.now)
    date_fire = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=8, choices=GRADE, default=GRADE[0])
    key_people = models.BooleanField(default=False)
    bus_factor = models.BooleanField(default=False)
    emi = models.FloatField(default=0.0)
    position = models.ForeignKey(
        Position,
        verbose_name='Должность',
        on_delete=models.SET_NULL,
        related_name='user',
        null=True,
        blank=False,
    )
    team = models.ManyToManyField(
        Team,
        verbose_name='Команда',
    )
    role = models.CharField(
        max_length=max(len(role) for role, _ in ROLE_CHOICES),
        choices=ROLE_CHOICES,
        default=USER,
    )

    class Meta:
        ordering = ['last_name', 'first_name',]
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return (
            f'{self.username}'
        )


class LastRating(models.Model):
    """Таблица дата последней оценки и соответствие навыка

    по сотруднику и навыку. Является связкой для временных рейтингов
    и user.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='lastrating',
        verbose_name='Сотрудник',
    )
    skill = models.ForeignKey(
        Skill,
        verbose_name='Навык',
        on_delete=models.SET_NULL,
        related_name='lastrating',
        null=True,
        blank=False,
    )
    last_match = models.BooleanField(default=False)
    last_date = models.DateField(default=datetime.datetime.now)

    class Meta:
        ordering = ['user', 'skill',]
        verbose_name = 'Оценка навыков'
        verbose_name_plural = 'Оценки навыков'

    def __str__(self):
        return (f'{self.last_match},')


class Rating(models.Model):
    """Таблица оценок навыков, компетенций."""
    last_rating = models.ForeignKey(
        LastRating,
        on_delete=models.CASCADE,
        related_name='rating',
        verbose_name='Последняя оценка',
    )
    score = models.IntegerField(choices=RATING, default=RATING[0])
    date_score = models.DateField(default=datetime.datetime.now)
    match = models.BooleanField(default=False)
    chief_proof = models.BooleanField(default=False)
    need_to_study = models.BooleanField(default=False)
    date_need = models.DateField(default=datetime.datetime.now)
    date_start = models.DateField(default=datetime.datetime.now)
    date_end = models.DateField(default=datetime.datetime.now)

    class Meta:
        ordering = ['last_rating',]
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return (
            f'оценка по навыку {self.last_rating} на '
            f'{self.date_score.strftime("%d.%m.%Y")} -- {self.score}!'
        )


class Vacancy(models.Model):
    """Таблица вакансий (требуемых должностей)"""

    closed = models.BooleanField(default=False)
    position = models.ForeignKey(
        Position,
        verbose_name='Должность',
        on_delete=models.SET_NULL,
        related_name='vacancy',
        null=True,
        blank=False,
    )
    team = models.ForeignKey(
        Team,
        verbose_name='Команда',
        on_delete=models.SET_NULL,
        related_name='vacancy',
        null=True,
        blank=False,
    )

    class Meta:
        ordering = ['position',]
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return (self.position.name)


class Candidate(models.Model):
    """Линки на HH.RU привязанные к вакансии (должности)."""

    vacancy = models.ForeignKey(
        Vacancy,
        related_name='condidate',
        verbose_name='Вакансия',
        on_delete=models.CASCADE,
    )
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['link',]
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'

    def __str__(self):
        return (self.link)
