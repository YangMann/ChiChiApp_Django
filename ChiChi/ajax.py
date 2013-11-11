from django.shortcuts import render_to_response

__author__ = 'JeffreyZhang'


def home(request):

    return render_to_response("includes/photoflow.html")


def adventure(request):

    return render_to_response("includes/adventure.html")


def blog(request):

    return render_to_response("includes/blog.html")
