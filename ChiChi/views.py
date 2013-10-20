# Create your views here.
from django.http import HttpResponse, Http404
#from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist


def hello(request):
    return HttpResponse("Hello world")


def index(request):
    #return HttpResponse("ChiChi")
    return render_to_response("includes/base.html")


def about(request):
    try:
        return render_to_response("about.html")
    except TemplateDoesNotExist:
        raise Http404()
