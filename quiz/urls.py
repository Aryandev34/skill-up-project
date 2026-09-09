from django.urls import path

from . import views

app_name = "quiz"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.SkillUpLoginView.as_view(), name="login"),
    path("logout/", views.SkillUpLogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("language/<slug:slug>/", views.select_level, name="select_level"),
    path(
        "language/<slug:slug>/quiz/<slug:difficulty>/",
        views.take_quiz,
        name="take_quiz",
    ),
]
