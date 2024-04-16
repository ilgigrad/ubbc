from django.contrib import admin
from django.utils.html import mark_safe
from import_export.admin import ExportMixin


class OrganizerAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        "mini_avatar",
        "email",
        "full_name",
        "_event",
        "role",
        "active",
    )

    raw_id_fields = ("user", "event")

    readonly_fields = ("large_avatar", "email", "full_name", "_event")

    list_filter = (
        "user__profile__gender",
        "user__profile__nationality",
        "user__profile__country",
        "user__is_active",
    )

    search_fields = ("user__profile__city", "user__first_name", "user__last_name")

    def large_avatar(self, obj):
        if obj.user and obj.user.profile:
            avatar = obj.user.profile.avatar
            color = obj.user.profile.color
        else:
            avatar = None
            color = "#000000"

        if avatar:
            return mark_safe(
                f"<img src='{avatar.url}' style='width:75px;height:75px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:75px;height:75px;background-color:{color}'></div>"
        )

    large_avatar.short_description = "avatar"

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

    email.admin_order_field = "user__email"  # Allows column order sorting

    def full_name(self, obj):
        return obj.user.full_name

    full_name.admin_order_field = "user__last_name"  # Allows column order sorting

    def active(self, obj):
        return obj.user.is_active

    active.admin_order_field = "user__is_active"  # Allows column order sorting
    active.boolean = True

    def _event(self, obj):
        return obj.event.name

    _event.admin_order_field = "event__name"  # Allows column order sorting
