from django.contrib import admin
from volunteer.models import Volunteer

from .admins._volunteer_admin import VolunteerAdmin
from .models import Volunteer

admin.site.register(Volunteer, VolunteerAdmin)
