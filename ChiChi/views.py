# Create your views here.
from django.http import HttpResponse, Http404
#from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist

import json


def hello(request):
    return HttpResponse("Hello world")


def index(request):

    return render_to_response("index.html")


def about(request):
    try:
        return render_to_response("about.html")
    except TemplateDoesNotExist:
        raise Http404()


def photo_flow(request):

    pass


def blog(request):
    try:
        return render_to_response("blog.html")
    except TemplateDoesNotExist:
        raise Http404()
