from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg, Min, Max

from .models import User

# Create your views here.


def get_users(request):
    users = User.objects.all().order_by("-name")  # adding `-` makes it DESC
    total_users = users.count()
    aggregate_age = users.aggregate(Avg("age"), Max("age"), Min("age"))

    return render(request, "user/users.html", {
        "users": users,
        "total_users": total_users,
        "aggregate_age": aggregate_age
    })


def get_user_by_id(request, user_id):
    # try:
    #     user = User.objects.get(pk=user_id)
    # except
    #     raise Http404();
    user = get_object_or_404(User, pk=user_id)
    return render(request, "user/user.html", {
        "user": user
    })


def get_user_by_slug(request, user_slug):
    # try:
    #     user = User.objects.get(pk=user_id)
    # except
    #     raise Http404();
    user = get_object_or_404(User, slug=user_slug)
    return render(request, "user/user.html", {
        "user": user
    })


def create_user(request):
    return render(request, "user/user.html", {
        "name": "anup",
        "id": 1
    })
