from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('demo/', views.demo, name='demo'),
    path('new_interaction/', views.new_interaction, name='new_interaction'),
    path('homepage/', views.homepage, name='homepage'),
    path('settings/', views.settings, name='settings'),
    path('help/', views.help, name='help'),

    path('clown/', views.clown, name='clown'),
    path('butterfly/', views.butterfly, name='butterfly'),
    path('simple/', views.simple, name='simple'),
    path('triangles/', views.triangles, name='triangles'),
    path('flower/', views.flower, name='flower'),
]
