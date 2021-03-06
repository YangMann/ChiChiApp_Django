# Create your views here.
import datetime
from django.http import HttpResponse, Http404
#from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response
from django.template import TemplateDoesNotExist

import json
from ChiChi.models import Comment


def hello(request):
    return HttpResponse("Hello world")


def index(request):
    return render_to_response("index.html")


def about(request):
    try:
        return render_to_response("about.html")
    except TemplateDoesNotExist:
        raise Http404()


def home(request):
    return render_to_response("includes/photoflow.html")


def photo_flow(request):
    return


def adventure(request):
    return render_to_response("adventure.html")


def blog(request):
    try:
        return render_to_response("includes/blog.html")
    except TemplateDoesNotExist:
        raise Http404()


def submit_comment(request):
    errors = []
    if request.method == "GET":
        t_content = request.GET['t_content']
        if not t_content:
            errors.append('please write down something')
        else:
            comment = Comment.objects.create(content=t_content, time=datetime.datetime.now(), user_id='qiaoliang0924')
            comment.save()
            return render_to_response('index.html', {'submit': True})
    return render_to_response('index.html', {'errors': errors})
