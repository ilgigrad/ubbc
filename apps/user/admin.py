from django.contrib import admin

from .admins._user_admin import UserAdmin
from .admins._user_connection_admin import ConnectionLogAdmin as UserConnectionLogAdmin
from .admins._user_profile_admin import ProfileAdmin as UserProfileAdmin
from .models import User, UserConnectionLog, UserProfile

admin.site.register(User, UserAdmin)
admin.site.register(UserConnectionLog, UserConnectionLogAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
