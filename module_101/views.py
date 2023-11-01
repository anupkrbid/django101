from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import NoReverseMatch, reverse

# Create your views here.


def index(request):
    html_response = """
        <ul>
            <li><a href="even">Even</a></li>
            <li><a href="odd">Odd</a></li>
            <li><a href="-1">-1</a></li>
            <li><a href="0">0</a></li>
            <li><a href="1">1</a></li>
            <li><a href="2">2</a></li>
            <li><a href="3">3</a></li>
            <li><a href="4">4</a></li>
        </ul>
    """
    return HttpResponse(html_response)


def view_type(request, view_type):
    if (view_type == "even"):
        return HttpResponse("Even View")
    elif (view_type == "odd"):
        return HttpResponse("Odd View")
    else:
        redirect_path = reverse("invalid-view-type")
        return HttpResponseRedirect(redirect_path)


def view_no(request, view_no):
    # if (view_no % 2 == 0):
    #     return HttpResponseRedirect("even")
    # else:
    #     return HttpResponseRedirect("/views/" + "odd")
    view_type = "even" if view_no % 2 == 0 else "odd"
    try:
        redirect_path = reverse(
            "view-type", args=[view_type])  # views/(even/odd)
        return HttpResponseRedirect(redirect_path)
    except NoReverseMatch:
        redirect_path = reverse("invalid-view-type")
        return HttpResponseRedirect(redirect_path)


def invalid_view_type(request):
    # return HttpResponseNotFound("Invalide View")
    error_message = "Invalid View"
    html_response = f"<h1>{error_message}</h1>"
    return HttpResponseNotFound(html_response)
