from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Avg, Min, Max

from .models import User, Access
from .forms import UserForm

# Create your views here.


def get_users(request):
    users = User.objects.all().order_by("-name")  # adding `-` makes it DESC
    total_users = users.count()
    aggregate_age = users.aggregate(Avg("age"), Max("age"), Min("age"))

    form = UserForm()

    return render(request, "user/users.html", {
        "users": users,
        "total_users": total_users,
        "aggregate_age": aggregate_age,
        "form": form
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
    #     user = User.objects.get(slug=user_slug)
    # except
    #     raise Http404();
    user = get_object_or_404(User, slug=user_slug)
    return render(request, "user/user.html", {
        "user": user
    })


def create_user(request):
    # if request.method == "POST"
    # name = request.POST["name"]
    # email = request.POST["name"]
    # age = request.POST["name"]
    # access = request.POST["access"]
    # passport = request.POST["passport"]

    form = UserForm(request.POST)

    if (form.is_valid()):
        # clean_data = form.cleaned_data
        # access = Access.objects.get(type=clean_data["access"])
        # user = User(name=clean_data["name"], email=clean_data["email"], age=clean_data["age"],
        #             access=access, passport=clean_data["passport"])
        form.save()
        redirect_path = reverse("specific-user-path-id", args=[1])
        return HttpResponseRedirect(redirect_path)

    redirect_path = reverse("all-users-path")
    return HttpResponseRedirect(redirect_path)


def update_user(request, user_id):
    existing_user = User.objects.get(pk=user_id)
    form = UserForm(request.POST, instance=existing_user)  # updating

    if (form.is_valid()):
        form.save()
        redirect_path = reverse("specific-user-path-id", args=[user_id])
        return HttpResponseRedirect(redirect_path)

    redirect_path = reverse("specific-user-path-id", args=[user_id])
    return HttpResponseRedirect(redirect_path)
