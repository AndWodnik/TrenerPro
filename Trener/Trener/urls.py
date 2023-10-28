"""
URL configuration for Trener project.

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
from TrenerApp import views
from TrenerApp.views import CustomLoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('temp/', views.temp, name='temp'),
    path('person_list/', views.person_list, name='person_list'),
    path('person/<int:person_id>/', views.person, name='person_view'),
    path('add_person/', views.add_person, name='add_person'),
    path('add_excercise/', views.add_excercise, name='add_excercise'),
    path('excercise/', views.excercise_list, name='excercise_list'),
    path('excercise/edit/<int:excercise_id>/', views.edit_excercise, name='edit_excercise'),
    path('modules/', views.ModuleListView.as_view(), name='module_list'),
    path('module/<int:module_id>/', views.module_detail, name='module_detail'),
    path('module/<int:module_id>/add_exercise/', views.add_module_exercise, name='add_module_exercise'),
    path('dom/', views.startingpage2, name='startingpage2'),
]