from django.contrib import admin
from django.urls import path
from . import views

# pegando todas as views 

urlpatterns = [
    
    path('', views.index, name= 'index'),

    path('userInfo', views.user, name = 'info'),

    path('cache', views.cache_user, name = "cache" ),

    path('search', views.seach_group, name = 'search'),

    path('message', views.message, name = 'message')

]