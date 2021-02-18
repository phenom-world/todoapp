from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.index, name="index"),
    path("update/<str:task_id>/", views.update, name="update"),
    path("delete/<str:task_id>/", views.deleteTask, name="delete"),
    path("acccounts/register/", views.register, name="register"),
    path("accounts/login/", views.loginPage, name="loginPage"),
    path("accounts/logout/", views.logoutPage, name="logoutPage"),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="accounts/form.html"),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/done.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/complete.html"
        ),
        name="password_reset_complete",
    ),
]