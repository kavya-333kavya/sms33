from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [

    path('student/studenthome/', views.studenthomepage, name='studenthomepage'),

    #path('',views.projecthomepage,name='projecthomepage'),

    path('signup',views.signup,name='signup'),
    path('signup1',views.signup1,name='signup1'),
    path('', views.login, name='login'),

    path('logout', views.logout, name='logout'),

    path('login1', views.login1, name='login1'),
    path('facultyhomeproject/', views.facultyhomeproject, name='facultyhomeproject'),
]