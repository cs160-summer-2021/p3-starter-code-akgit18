from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo/', views.demo, name='demo'),
    path('new_interaction/', views.new_interaction, name='new_interaction'),
    path('homepage/', views.homepage, name='homepage'),
    path('settings/', views.settings, name='settings')
]
