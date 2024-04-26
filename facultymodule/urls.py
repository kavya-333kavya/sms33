from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('facultyhomeproject/', views.facultyhomeproject, name='facultyhomeproject'),
    path('viewprofile/',views.viewprofile,name='viewprofile'),

    path('facultycourses/',views.facultycourses,name='facultycourses'),
]
