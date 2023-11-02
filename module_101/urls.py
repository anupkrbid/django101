from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="path-view-list"),
    path("invalid-view-type", views.invalid_view_type,
         name="path-invalid-view-type"),
    path("<int:view_no>", views.view_no, name="path-view-no"),
    path("<str:view_type>", views.view_type, name="path-view-type"),
]
