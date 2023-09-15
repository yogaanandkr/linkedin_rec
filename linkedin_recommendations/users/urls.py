from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path("profile/<int:id>", views.UserProfile.as_view()),
]
