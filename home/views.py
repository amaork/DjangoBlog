# -*- coding: utf-8 -*-
import time
from .models import BlogInfo, Navigation
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def get_basic_info(request):
    return {

        'path': request.path,
        'blog': get_object_or_404(BlogInfo),
        'breadcrumbs': [Navigation(request.path, request.path[1:-1].title())]
    }


def homepage(request):
    content = get_basic_info(request)
    return render(request, 'home.html', content)


def about(request):
    content = get_basic_info(request)
    return render(request, 'about.html', content)
