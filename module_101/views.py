from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def view_no(request, view_no):
    try:
        if (int(view_no) % 2 == 0):
            return HttpResponse("Even View")
        else:
            return HttpResponse("Odd View")
    except ValueError:
        return HttpResponseNotFound("Invalide View")
