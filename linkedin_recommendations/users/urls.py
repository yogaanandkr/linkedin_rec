from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = 'home'),
    path("logout", views.logout_view),
    path("profiles", views.profiles, name = 'profiles'),
    path("recommend", views.recommend, name = 'recommend'),
    path("profile/edit/rec/<int:id>", views.edit_rec_page, name = 'edit_rec'),
    path("rec_edit", views.rec_edit, name = 'rec_edit'),
    path("rec_delete", views.rec_delete, name = 'rec_delete'),
    path("profile/update_bio/<name>", views.get_profile_form, name = 'update_bio'),
    path("update_profile", views.updateprofile, name = 'update_profile'),
    path("profile/<str:name>", views.userdetail, name = 'user_detail'),
    path("upload_post", views.upload_post, name='upload_post'),
    path("follow", views.follow, name='follow'),
]
