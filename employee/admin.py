from django.contrib import admin
from .models import Employee
from .models import Rating
from .models import Position
from .models import Team
from .models import Competence
from .models import Skill


admin.site.register(Team)
admin.site.register(Competence)
admin.site.register(Skill)
admin.site.register(Position)


@admin.register(Rating)
class RaitingAdmin(admin.ModelAdmin):
    list_filter = ['fio',]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ['team','grade']


admin.site.empty_value_display = 'Не задано'
