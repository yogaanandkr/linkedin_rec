from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("logout", views.logout_view),
    path("profiles", views.profiles, name = 'profiles'),
    path("recommend", views.recommend, name = 'recommend'),
    path("profile/<int:id>", views.userdetail, name = 'user_detail')
]
