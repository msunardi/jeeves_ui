# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'index_active': True})

def tour(request):
    return render(request, 'main/tour.html', {'tour_active': True})

def waypoint(request, nav):
    locations = {'ee': ('EE Fishbowl', 'ee_fishbowl.jpg'), \
                 'NEAR_lab': ('NEAR Lab', 'near1.jpg'), \
                 'robot_lab': ('Intelligent Robotics Lab', 'robotics1.jpg'), \
                 'Biomedical_lab': ('Biomedical Signal Processing Lab', 'biomedical2.jpg'), \
                 'stairs': ('EB Stairs/Elevators', 'eb_stairs.jpg')}
    location_name, image = locations[nav]
    return render(request, 'main/waypoint.html', {'location_name': location_name, 'image': image})

def aboutpsu(request):
    return render(request, 'main/aboutpsumcecs.html', {'aboutpsu_active': True})

def vision(request):
    return render(request, 'main/vision.html', {'vision_active': True, 'video_server': 'http://192.168.1.4:8080'})

def dashboard(request):
    return render(request, 'main/dashboard.html', {'dashboard_active': True})

def aboutme(request):
    return render(request, 'main/uikit-aboutme.html', {'aboutme_active': True})

def exmode(request):
    return render(request, 'main/uikit-exmode.html', {'exmode_active': True})

def console(request):
    return render(request, 'main/console.html')