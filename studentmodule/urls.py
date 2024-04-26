from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('studentnavbar/',views.studentnavbar,name='studentnavbar'),
    path('viewprofile/',views.viewprofiles,name='viewprofiles'),
    path('studenthome/',views.studenthomepage,name='studenthomepage'),
    path('studentcourses/',views.studentcourses,name='studentcourses'),


]