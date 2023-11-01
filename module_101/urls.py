from django.urls import path
from . import views

urlpatterns = [
    path("<view_no>", views.view_no)
]
