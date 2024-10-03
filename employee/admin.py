from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import(
    Rating, Position, Team, Competence, Skill, Vacancy, Candidate,
)


User = get_user_model()

admin.site.register(Team)
admin.site.register(Competence)
admin.site.register(Position)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_filter = ['domain','competence',]


@admin.register(Rating)
class RaitingAdmin(admin.ModelAdmin):
    list_filter = ['user',]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ['team','grade','position']


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_filter = ['position',]


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_filter = ['link',]


admin.site.empty_value_display = 'Не задано'
