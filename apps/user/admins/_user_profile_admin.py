from django.contrib import admin
from django.utils.html import mark_safe
from import_export.admin import ExportMixin


class ProfileAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        "email",
        "full_name",
        "mini_avatar",
        "gender",
        "year",
        "nationality",
        "city",
        "active",
        "staff",
        "is_organizer",
        "is_athlete",
        "is_volunteer",
    )
    readonly_fields = (
        "large_avatar",
        "active",
        "staff",
        "is_organizer",
        "is_athlete",
        "is_volunteer",
    )
    raw_id_fields = ("user",)

    list_filter = (
        "gender",
        "nationality",
        "country",
        "user__is_active",
        "user__is_staff",
    )

    search_fields = ("city", "user__first_name", "user__last_name")
    # ordering = ("-date_joined",)

    def large_avatar(self, obj):
        if obj.avatar:
            return mark_safe(
                f"<img src='{obj.avatar.url}' style='width:75px;height:75px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:75px;height:75px;background-color:{obj.color}'></div>"
        )

    large_avatar.short_description = "avatar"

    def mini_avatar(self, obj):
        if obj.avatar:
            return mark_safe(
                f"<img src='{obj.avatar.url}' style='width:30px;height:30px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:30px;height:30px;background-color:{obj.color}'></div>"
        )

    mini_avatar.short_description = "avatar"

    def year(self, obj):
        if obj.birth_date:
            return obj.birth_date.year
        return None

    year.admin_order_field = "birth_date__year"  # Allows column order sorting

    def telephone(self, obj):
        if obj.profile:
            return obj.telephone
        return None

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

    def staff(self, obj):
        return obj.user.is_staff

    staff.admin_order_field = "user__is_staff"  # Allows column order sorting
    staff.boolean = True

    def is_organizer(self, obj):
        return obj.user.is_organizer

    is_organizer.admin_order_field = "user__organizer"  # Allows column order sorting
    is_organizer.boolean = True
    is_organizer.short_description = "organizer"

    def is_volunteer(self, obj):
        return obj.user.is_volunteer

    is_volunteer.admin_order_field = "user__volunteer"  # Allows column order sorting
    is_volunteer.boolean = True
    is_volunteer.short_description = "volunteer"

    def is_athlete(self, obj):
        return obj.user.is_athlete

    is_athlete.admin_order_field = "user__athlete"  # Allows column order sorting
    is_athlete.boolean = True
    is_athlete.short_description = "athlete"
