from athlete.models import Athlete
from django.contrib import admin

from .admins._athlete_admin import AthleteAdmin
from .models import Athlete

admin.site.register(Athlete, AthleteAdmin)
