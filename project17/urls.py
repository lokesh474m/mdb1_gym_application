"""
URL configuration for project17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mdb1/',mdb1,name='mdb1'),
    path('registration/',registration,name='registration'),
    path('login/',login,name='login'),
    path('menu_card/',menu_card,name='menu_card'),
    path('password/',password,name='password'),
    path('pushup/',pushup,name='pushup'),
    path('running/',running,name='running'),
    path('push_down/',push_down,name='push_down'),
    path('floor_press/',floor_press,name='floor_press'),
    path('dumbbell_bridge/',dumbbell_bridge,name='dumbbell_bridge'),
    path('cardio/',cardio,name='cardio'),
    path('calisthenics/',calisthenics,name='calisthenics'),
    path('cable_cross/',cable_cross,name='cable_cross'),
    path('bench_press/',bench_press,name='bench_press'),
]
