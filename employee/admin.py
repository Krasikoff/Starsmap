from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import (Candidate, Competence, LastRating, Position, Rating,
                     Skill, Team, Vacancy)

User = get_user_model()

admin.site.register(Team)
admin.site.register(Competence)
admin.site.register(Position)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_filter = ['domain', 'competence',]


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1


@admin.register(LastRating)
class LastRatingAdmin(admin.ModelAdmin):
    inlines = (
        RatingInline,
    )
    list_display = (
        'user', 'skill', 'last_match', 'last_date',
    )
    list_filter = ['user', 'skill', 'last_match', 'last_date']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('groups', 'user_permissions', 'team')
    list_display = (
        'last_name', 'first_name', 'position', 'grade',
    )
    list_filter = ['team', 'grade', 'position']


class CandidateInline(admin.TabularInline):
    model = Candidate
    extra = 1


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    inlines = (
        CandidateInline,
    )
    list_filter = ['position',]


admin.site.empty_value_display = 'Не задано'
