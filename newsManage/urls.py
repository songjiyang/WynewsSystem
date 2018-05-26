from django.conf.urls import url
# -*- coding: utf-8 -*-
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^single/$', views.single, name='single'),
]