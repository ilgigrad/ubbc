# Register your models here.
from django.contrib import admin

from .admins._event_admin import EventAdmin
from .admins._event_edition_admin import EditionAdmin as EventEditionAdmin
from .admins._event_organizer_admin import OrganizerAdmin as EventOrganizerAdmin
from .models import Event, EventEdition, EventOrganizer

admin.site.register(Event, EventAdmin)
admin.site.register(EventEdition, EventEditionAdmin)
admin.site.register(EventOrganizer, EventOrganizerAdmin)
