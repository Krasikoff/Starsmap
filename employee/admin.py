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
admin.site.register(Rating)
admin.site.register(Employee)
admin.site.register(Position)
admin.site.empty_value_display = 'Не задано'
