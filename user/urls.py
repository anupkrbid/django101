from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_users, name="all-users-path"),
    path("new", views.create_user, name="create-user-path"),
    path("<int:user_id>", views.get_user_by_id, name="specific-user-path-id"),
    path("<slug:user_slug>", views.get_user_by_slug,
         name="specific-user-path-slug")
]
