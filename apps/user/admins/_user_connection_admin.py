from django.contrib import admin
from django.utils.html import mark_safe


class ConnectionLogAdmin(admin.ModelAdmin):
    list_display = (
        "mini_avatar",
        "user",
        "connected_at",
        "ip_address",
        "expire",
        "elapsed",
    )

    list_filter = ("connected_at",)

    search_fields = (
        "user__last_name",
        "user__first_name",
        "user__id",
        "user__email",
        "ip_address",
    )
    raw_id_fields = ("user",)
    readonly_fields = (
        "image",
        "connected_at",
        "ip_address",
        "expire",
        "elapsed",
    )
    ordering = ("-connected_at",)

    def expire(self, obj):
        return obj.expire_date

    expire.admin_order_field = "session__expire_date"  # Allows column order sorting

    def elapsed(self, obj):
        return obj.elapsed

    elapsed.admin_order_field = "-session__expire_date"  # Allows column order sorting

    def image(self, obj):
        if obj.user.profile.avatar:
            return mark_safe(
                f"<img src='{obj.user.profile.avatar.url}' style='width:75px;height:75px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:75px;height:75px;background-color:{obj.user.profile.color}'></div>"
        )

    def mini_avatar(self, obj):
        if obj.user.profile.avatar:
            return mark_safe(
                f"<img src='{obj.user.profile.avatar.url}' style='width:30px;height:30px;object-fit:cover;border-radius:50%;'>"
            )
        return mark_safe(
            f"<div id='avatar-img' style='border-radius:50%;width:30px;height:30px;background-color:{obj.user.profile.color}'></div>"
        )
