from django.contrib import admin
from event.models import EventEdition


class EditionInline(admin.TabularInline):
    model = EventEdition
    fields = ("year", "date")
    ordering = ("year",)

    max_num = 0
    extra = 1
    can_delete = True
    show_change_link = True
