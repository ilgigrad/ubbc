from django.contrib import admin
from django.utils.html import mark_safe
from event.models import EventOrganizer


class OrganizerInline(admin.TabularInline):
    model = EventOrganizer
    fields = ("user", "mini_avatar", "role", "full_name", "email")
    readonly_fields = ("mini_avatar", "role", "full_name", "email")
    ordering = ("-created_at",)

    max_num = 0
    extra = 1
    can_delete = True
    show_change_link = True

    def mini_avatar(self, obj):
        if obj.user.profile:
            avatar = obj.user.profile.avatar
            color = obj.user.profile.color
        else:
            avatar = None
            color = "#000000"

        if avatar:
            return mark_safe(
                f"<img src='{avatar.url}' style='width:30px;height:30px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:30px;height:30px;background-color:{color}'></div>"
        )

    def email(self, obj):
        return obj.user.email

    def full_name(self, obj):
        return obj.user.full_name
