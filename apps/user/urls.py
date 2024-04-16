from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

app_name = "user"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "settings/password/",
        auth_views.PasswordChangeView.as_view(
            template_name="user/password/change.html",
            success_url=reverse_lazy("user:password_change_done"),
        ),
        name="password_change",
    ),
    path(
        "settings/password/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="user/password/change_done.html"
        ),
        name="password_change_done",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="user/password/reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="user/password/reset_confirm.html",
            success_url=reverse_lazy("user:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="user/password/reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
