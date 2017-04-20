# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'index_active': True})

def tour(request):
    return render(request, 'main/tour.html', {'tour_active': True})

def aboutpsu(request):
    return render(request, 'main/uikit-aboutpsumcecs.html', {'aboutpsu_active': True})

def vision(request):
    return render(request, 'main/vision.html', {'vision_active': True, 'video_server': 'http://192.168.1.51:8080'})

def dashboard(request):
    return render(request, 'main/dashboard.html', {'dashboard_active': True})

def aboutme(request):
    return render(request, 'main/uikit-aboutme.html', {'aboutme_active': True})

def exmode(request):
    return render(request, 'main/uikit-exmode.html', {'exmode_active': True})
