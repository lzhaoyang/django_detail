#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.views.decorators.http import require_GET,require_POST
from wsgiref.simple_server import make_server

@require_POST
def v_index(req):
    print(req.method)
    rsp = HttpResponse('啊哈')
    rsp.set_cookie('user','liuzhaoyang')
    return rsp

urlpatterns = [
    url(r'^$',v_index),
]

settings.configure()
settings.DEBUG = True
settings.ROOT_URLCONF = sys.modules[__name__]
settings.MIDDLEWARE_CLASSES = ()

wsgi = get_wsgi_application()
httpd = make_server('0.0.0.0',7000,wsgi)

print('start serving at 0.0.0.0:7000')
print(sys.modules[__name__])
# sys.modules 是一个字典，它包含了从 Python 开始运行起，被导入的所有模块。
# 键字就是模块名，键值就是模块对象。请注意除了你的程序导入的模块外还有其它模块。
# Python 在启动时预先装入了一些模块，如果你在一个 Python IDE 环境下，sys.modules
#  包含了你在 IDE 中运行的所有程序所导入的所有模块。
# for i in sys.modules:
#     print(str(i))
httpd.serve_forever()
