from django.shortcuts import render

# Create your views here.


def get_users(request):
    return render(request, "user/users.html", {
        "users": [{
            "name": "anup",
            "id": 1
        }, {
            "name": "absinthe",
            "id": 2
        }]
    })


def get_user(request, user_id):
    return render(request, "user/user.html", {
        "name": "anup",
        "id": user_id
    })


def create_user(request):
    return render(request, "user/user.html", {
        "name": "anup",
        "id": 1
    })
