#!/usr/bin/env python3
# encoding:utf-8
# written by:liuzhaoyang

from django.conf import settings
from django.conf.urls import url
from django.core.urlresolvers import RegexURLResolver

settings.configure()
settings.DEBUG = True

def v_index(request):
    return "this is from index"

def v_news(request):
    return "this is from news"

def v_blogs(request):
    return "this is from blogs"

mysite_urlpatterns = [
    url(r'^$',v_index),
    url(r'^news/$',v_news),
    url(r'^blogs/$',v_blogs)
]
# 路由解析的前缀剔除
# reslver = RegexURLResolver(r'^mysite/',mysite_urlpatterns)
#
# 解析器返回的东西
#
# view_func,args,kwargs = reslver.resolve('mysite/news/')
# print(view_func(None))

resolver = RegexURLResolver(r'^/',mysite_urlpatterns)
test_urls = ['','news/','blogs/','whoami/','/','a/b/c/d']
for url in test_urls:
    try:
        view,args,kwargs = resolver.resolve(url)
        print('found match for %s.calling...' % url)
        print(view(None))
    except:
        print('no match for %s' % url)

