from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import NoReverseMatch, reverse
from django.template.loader import render_to_string

# Create your views here.


def index(request):
    string_urls = {
        "even": "Go to Even Path",
        "odd": "Go to Odd Path",
        "qwerty": "Go to Invalid Path (qwerty)",
    }
    no_urls = {
        "-1": "Go to Invalid Path (-1)",
        "0": "Go to Even Path (0)",
        "1": "Go to Odd Path (1)",
        "2": "Go to Even Path (2)",
        "3": "Go to Odd Path (3)"
    }
    list_string_urls = list(string_urls.keys())
    list_no_urls = list(no_urls.keys())

    # Creating HTML string manually
    #
    # list_items = ""
    # for item in list_string_urls:
    #     # item.capitalize()
    #     path = reverse("path-view-type", args=[item])
    #     list_items += f"<li><a href=\"{path}\">{string_urls[item]}</a></li>"

    # for item in list_no_urls:
    #     try:
    #         path = reverse("path-view-no", args=[item])
    #     except:
    #         path = reverse("path-invalid-view-type")
    #     list_items += f"<li><a href=\"{path}\">{no_urls[item]}</a></li>"

    # html_response = f"""<ul>{list_items}</ul>"""
    # return HttpResponse(html_response)

    # Rendering HTML using templates
    #
    string_view_list = []
    for item in list_string_urls:
        path = reverse("path-view-type", args=[item])
        string_view_list.append({"arg": item, "text": string_urls[item]})

    no_view_list = []
    for item in list_no_urls:
        try:
            path = reverse("path-view-no", args=[item])
        except:
            path = reverse("path-invalid-view-type")
        no_view_list.append({"path": path, "text": no_urls[item]})
    #
    # html_text = render_to_string("module_101/views.html",  {
    #     "string_views": string_view_list,
    #     "no_views": no_view_list
    # })
    # return HttpResponse(html_text)
    return render(request, "module_101/views.html", {
        "string_views": string_view_list,
        "no_views": no_view_list
    })


def view_type(request, view_type):
    header_html_text = render_to_string("partials/header.html", {
        "active_page": view_type.capitalize()
    })
    if (view_type == "even"):
        return HttpResponse(header_html_text + "<br>" + "Even View")
    elif (view_type == "odd"):
        return HttpResponse(header_html_text + "<br>" + "Odd View")
    else:
        redirect_path = reverse("path-invalid-view-type")
        return HttpResponseRedirect(redirect_path)


def view_no(request, view_no):
    # if (view_no % 2 == 0):
    #     return HttpResponseRedirect("even")
    # else:
    #     return HttpResponseRedirect("/views/" + "odd")
    view_type = "even" if view_no % 2 == 0 else "odd"
    try:
        redirect_path = reverse(
            "path-view-type", args=[view_type])  # views/(even/odd)
        return HttpResponseRedirect(redirect_path)
    except NoReverseMatch:
        redirect_path = reverse("path-invalid-view-type")
        return HttpResponseRedirect(redirect_path)


def invalid_view_type(request):
    # return HttpResponseNotFound("Invalide View")
    error_message = "Invalid View"
    html_response = f"<h1>{error_message}</h1>"
    return HttpResponseNotFound(html_response)
    """ create a 404.html in the root template folder 
        which will be returned by this Http404 class automatically
    """
    # raise Http404
