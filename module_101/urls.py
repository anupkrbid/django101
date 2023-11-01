from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("invalid-view-type", views.invalid_view_type, name="invalid-view-type"),
    path("<int:view_no>", views.view_no),
    path("<str:view_type>", views.view_type, name="view-type"),
]
