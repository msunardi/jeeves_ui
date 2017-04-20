from django.conf.urls import url

from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tour/', views.tour, name='tour'),
    url(r'^aboutpsu/', views.aboutpsu, name='aboutpsu'),
    url(r'^vision/', views.vision, name='vision'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^aboutme/', views.aboutme, name='aboutme'),
    url(r'^exmode/', views.exmode, name='exmode'),
]