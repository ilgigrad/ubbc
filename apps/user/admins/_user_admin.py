from django.contrib import admin
from django.utils.html import mark_safe
from import_export.admin import ExportMixin


class UserAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        "mini_avatar",
        "email",
        "first_name",
        "last_name",
        "staff",
        "date_joined",
        "active",
        "is_organizer",
        "is_athlete",
        "is_volunteer",
    )
    readonly_fields = (
        "id",
        "large_avatar",
        "is_organizer",
        "is_athlete",
        "is_volunteer",
    )

    list_filter = (
        "is_active",
        "is_staff",
        "date_joined",
    )
    search_fields = ("last_name", "first_name", "id", "email")
    ordering = ("-date_joined",)
    actions = [
        "set_not_staff",
        "deactivate",
        "activate",
    ]

    def deactivate(self, request, queryset):
        queryset.update(is_active=False)

    def activate(self, request, queryset):
        queryset.update(is_active=True)

    def set_not_staff(self, request, queryset):
        queryset.update(is_staff=False)

    def active(self, obj):
        return obj.is_active

    active.boolean = True
    active.short_description = "active"
    active.admin_order_field = "is_active"

    def staff(self, obj):
        return obj.is_staff

    staff.boolean = True
    staff.short_description = "staff"
    staff.admin_order_field = "is_staff"

    def first_name(self, obj):
        return obj.first_name.capitalize()

    first_name.admin_order_field = "first_name"  # Allows column order sorting

    def last_name(self, obj):
        return obj.last_name.upper()

    last_name.admin_order_field = "last_name"  # Allows column order sorting

    def save_model(self, request, obj, form, change):
        if (
            not User.objects.filter(pk=obj.pk).exists()
            or obj.password != User.objects.get(pk=obj.pk).password
        ):
            obj.set_password(obj.password)
        obj.save()

    def large_avatar(self, obj):
        if obj.profile:
            avatar = obj.profile.avatar
            color = obj.profile.color
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
        if obj.profile:
            avatar = obj.profile.avatar
            color = obj.profile.color
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

    mini_avatar.short_description = "avatar"

    def is_organizer(self, obj):
        return obj.is_organizer

    is_organizer.admin_order_field = "organizer"  # Allows column order sorting
    is_organizer.boolean = True
    is_organizer.short_description = "organizer"

    def is_volunteer(self, obj):
        return obj.is_volunteer

    is_volunteer.admin_order_field = "volunteer"  # Allows column order sorting
    is_volunteer.boolean = True
    is_volunteer.short_description = "volunteer"

    def is_athlete(self, obj):
        return obj.is_athlete

    is_athlete.admin_order_field = "athlete"  # Allows column order sorting
    is_athlete.boolean = True
    is_athlete.short_description = "athlete"
