#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

# 请求中间件
import sys,os

from django.conf import settings
from django.conf.urls import url
from django.views.generic import View
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from wsgiref.simple_server import make_server

class A_middleware():
    def process_request(self,request):
        print("A is process")
        return None

class B_middleware():
    def process_request(self,request):
        print('B is process')
        return None

class C_middleware():
    def process_request(self,request):
        request.META['myflag'] = "attach attribute to request"
        print('C is process')
        return None

def v_index(req):
    attch_str = req.META['myflag']
    rsp = "this is not the point"+attch_str
    return HttpResponse(rsp)

urlpatterns = [
    url(r'^$',v_index),
]

settings.configure()
settings.ROOT_URLCONF = sys.modules[__name__]
settings.DEBUG = True
settings.MIDDLEWARE_CLASSES=('__main__.A_middleware','__main__.B_middleware','__main__.C_middleware')

wsgi_app = get_wsgi_application()
httpd = make_server('0.0.0.0',8000,wsgi_app)
print('starting serving at 8000...')
httpd.serve_forever()
