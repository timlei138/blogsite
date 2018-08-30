# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def index(request):
    list = {'0':0,'1':1,'2':2,}
    return render(request, 'blog/templates/index.html',{'count':list})
