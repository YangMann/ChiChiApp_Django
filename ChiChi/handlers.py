__author__ = 'JeffreyZhang'

from ChiChi.ajax import *


def ajax_handler(request, name):
    return eval(str(name))(request)
