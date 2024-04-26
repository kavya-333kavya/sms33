from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("viewcourse/",views.viewcourses,name="viewcourses"),
    path("admincourse/",views.admincourse,name="admincourse"),
    path("addcourse/",views.addcourse,name="addcourse"),
    path("insertcourse",views.insertcourse,name="insertcourse"),
    path('coursenavbar/', views.coursenavbar, name='coursenavbar'),
    path('coursehome/', views.coursehomepage, name='coursehomepage'),
    path("addfaculty/",views.addfaculty,name="addfaculty"),
    path("viewfaculty/",views.viewfaculty,name="viewfaculty"),
    path("addfac/",views.addfac,name="addfac"),
    path("deletefaculty/",views.deletefaculty,name="deletefaculty"),
    path("facultydeletion/<int:fid>",views.facultydeletion,name="facultydeletion"),
    path("deletecourse/",views.deletecourse,name="deletecourse"),
    path("coursedeletion/<int:fid>",views.coursedeletion,name="coursedeletion"),
    path("assign1/",views.assign1,name="assign1"),
    path("assign/",views.assign,name="assign"),
    path("assigns/",views.assigns,name="assigns"),
    path("faccou/<str:cc>",views.faccou,name='faccou'),
    path("addstu/",views.addstu,name="addstu"),
    path("addstudent/",views.addstudent,name="addstudent"),
    path("viewstudent/",views.viewstudent,name="viewstudent"),
    path("deletestudent/",views.deletestudent,name="deletestudent"),
    path("studentdeletion/<int:sid>",views.studentdeletion,name="studentdeletion"),
    path('viewstucourses/',views.viewstucourses,name='viewstucourses'),
    path('viewfaccourses/',views.viewfaccourses,name='viewfaccourses'),
    path("studentprofile/",views.studentprofile,name='studentprofile'),
    path("facultyprofile/",views.facultyprofile,name='facultyprofile'),
    path('selectcourse/',views.selectcourse,name='selectcourse'),
    path('selectcourse 1/',views.selectcourse1,name='selectcourse1'),
]

