from django.contrib import admin
from django.utils.html import mark_safe
from import_export.admin import ExportMixin


class EditionAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        "mini_logo",
        "name",
        "country",
        "year",
        "date",
    )

    readonly_fields = (
        "id",
        "name",
        "large_logo",
        "country",
        "telephone",
        "email",
    )

    raw_id_fields = ("event",)

    list_filter = ("year", "event__country")
    search_fields = (
        "event__name",
        "event__description",
        "event__telephone",
        "event__email",
        "event__telephone",
    )
    ordering = ("-created_at",)

    def email(self, obj):
        return obj.event.email

    email.admin_order_field = "event__email"  # Allows column order sorting

    def name(self, obj):
        return obj.event.name

    name.admin_order_field = "event__name"  # Allows column order sorting

    def telephone(self, obj):
        return obj.event.telephone

    telephone.admin_order_field = "event__name"  # Allows column order sorting

    def country(self, obj):
        return obj.event.country

    country.admin_order_field = "event__country"  # Allows column order sorting

    def large_logo(self, obj):
        if obj.event:
            color = obj.event.color
        else:
            color = "#000000"

        if obj.event and obj.event.logo:
            return mark_safe(
                f"<img src='{obj.event.logo.url}' style='width:75px;height:75px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:75px;height:75px;background-color:{color}'></div>"
        )

    large_logo.short_description = "logo"

    def mini_logo(self, obj):
        if obj.event:
            color = obj.event.color
        else:
            color = "#000000"

        if obj.event and obj.event.logo:
            return mark_safe(
                f"<img src='{obj.event.logo.url}' style='width:30px;height:30px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:30px;height:30px;background-color:{color}'></div>"
        )

    mini_logo.short_description = "avatar"
