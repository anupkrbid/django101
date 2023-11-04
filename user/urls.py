from django.urls import path
from . import views

urlpatterns = [
    path("", views.get_users, name="all-users-path"),
    path("new", views.create_user, name="create-user-path"),
    path("<int:user_id>", views.get_user, name="specific-user-path")
]
