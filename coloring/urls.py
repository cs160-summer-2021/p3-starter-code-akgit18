from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('demo/', views.homepage, name='homepage'),
    path('new_interaction/', views.new_interaction, name='new_interaction'),
    path('new_interaction/1', views.new_interaction, name='new_interaction'),
    path('new_interaction/2', views.new_interaction, name='new_interaction'),
    path('new_interaction/3', views.new_interaction, name='new_interaction'),
    path('new_interaction/4', views.new_interaction, name='new_interaction'),
    path('new_interaction/5', views.new_interaction, name='new_interaction'),
    path('new_interaction/6', views.new_interaction, name='new_interaction'),
    path('homepage/', views.homepage, name='homepage'),
    path('settings/', views.settings, name='settings'),
    path('help/', views.help, name='help')
]
