from django.contrib import admin
from django.utils.html import mark_safe
from import_export.admin import ExportMixin

from ._event_edition_inline import EditionInline as EventEditionInline
from ._event_organizer_inline import OrganizerInline as EventOrganizerInline


class EventAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        "mini_logo",
        "name",
        "country",
    )
    readonly_fields = (
        "id",
        "large_logo",
    )

    list_filter = ()
    search_fields = ("name", "description", "telephone", "email")
    ordering = ("-created_at",)
    inlines = (EventEditionInline, EventOrganizerInline)

    def large_logo(self, obj):
        if obj.logo:
            return mark_safe(
                f"<img src='{obj.logo.url}' style='width:75px;height:75px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:75px;height:75px;background-color:{obj.color}'></div>"
        )

    large_logo.short_description = "logo"

    def mini_logo(self, obj):
        if obj.logo:
            return mark_safe(
                f"<img src='{obj.logo.url}' style='width:30px;height:30px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:30px;height:30px;background-color:{obj.color}'></div>"
        )

    mini_logo.short_description = "avatar"
