from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from employee.constants import RATING, GRADE, DOMAIN, ROLE_CHOICES, USER


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
            f'{self.last_name} {self.first_name} {self.position} '
            f'{self.grade} {self.role} нанят {self.date_hire}'
        )


class Rating(models.Model):
    """Таблица оценок навыков, компетенций."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Сотрудник'
    )
    skill = models.ForeignKey(
        Skill,
        verbose_name='Навык',
        on_delete=models.SET_NULL,
        related_name='rating',
        null=True,
        blank=False,
    )
    competence = models.ForeignKey(
        Competence,
        verbose_name='Компетенция',
        on_delete=models.SET_NULL,
        related_name='rating',
        null=True,
        blank=False,
    )
    need_to_study = models.BooleanField(default=False)
    score = models.IntegerField(choices=RATING, default=RATING[0])
    date_score = models.DateField(default=datetime.datetime.now)
    date = models.DateField(default=datetime.datetime.now)
    date_start = models.DateField(default=datetime.datetime.now)
    date_end = models.DateField(default=datetime.datetime.now)
    match = models.BooleanField(default=False)
    chief_proof = models.BooleanField(default=False)

    class Meta:
        ordering = ['user', 'skill',]
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return (
            f'оценка {self.user.last_name} {self.user.first_name} по '
            f'{self.skill.name} {self.competence.name} на '
            f'{self.date.strftime("%d.%m.%Y")} -- {self.score}!'
        )


class LastDateMatch(models.Model):
    """Таблица дата последней оценки и соответствие навыка по сотруднику и навыку.
    
    ее можно или развить как статическую таблицу, или убрать и перенести данные в raiting.
    """     
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Сотрудник'
    )
    skill = models.ForeignKey(
        Skill,
        verbose_name='Навык',
        on_delete=models.SET_NULL,
        related_name='lastdatematch',
        null=True,
        blank=False,
    )
    competence = models.ForeignKey(
        Competence,
        verbose_name='Компетенция',
        on_delete=models.SET_NULL,
        related_name='lastdatematch',
        null=True,
        blank=False,
    )
    match = models.BooleanField(default=False)
    date_last_score = models.DateField(default=datetime.datetime.now)

    class Meta:
        ordering = ['user', 'skill', 'date_last_score']
        verbose_name = 'Соответствие на последнюю дату'
        verbose_name_plural = 'Соответствия на последнюю дату'

    def __str__(self):
        return (
            f'{self.user.last_name} {self.user.first_name} '
            f'{self.skill.name} {self.competence.name} на '
            f'{self.date_last_score.strftime("%d.%m.%Y")} -- {self.match}!'
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
