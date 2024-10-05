from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import (Candidate, Competence, LastRating, LeaderInTeam, Position,
                     Rating, Skill, Team, Vacancy)

User = get_user_model()


admin.site.register(Competence)
admin.site.register(Position)


class LeaderInline(admin.TabularInline):
    """Инлайн добавка лидера для админ страницы команды"""

    model = LeaderInTeam
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Регистрация админ. страницы команды"""

    inlines = (
        LeaderInline,
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Регистрация админ. страницы навыков"""

    list_filter = ['domain', 'competence',]


class RatingInline(admin.TabularInline):
    """Инлайн добавка оценок на дату для админ страницы рейтингов"""

    model = Rating
    extra = 1


@admin.register(LastRating)
class LastRatingAdmin(admin.ModelAdmin):
    """Регистрация админ. страницы оценок"""

    inlines = (
        RatingInline,
    )
    list_display = (
        'user', 'skill', 'last_match', 'last_date',
    )
    list_filter = ['user', 'skill', 'last_match', 'last_date']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Регистрация админ. страницы сотрудников"""

    filter_horizontal = ('groups', 'user_permissions', 'team')
    list_display = (
        'last_name', 'first_name', 'position', 'grade',
    )
    list_filter = ['team', 'grade', 'position']


class CandidateInline(admin.TabularInline):
    """Инлайн добавка кандидатов для админ страницы вакансий"""

    model = Candidate
    extra = 1


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Регистрация админ. страницы вакансий."""
    inlines = (
        CandidateInline,
    )
    list_filter = ['position',]


admin.site.empty_value_display = 'Не задано'
