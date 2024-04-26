from django.shortcuts import render, redirect


# Create your views here.

def studentnavbar(request):
    return render(request,'studentnavbar.html')

def viewprofiles(request):
    return  redirect("studentprofile")

def studenthomepage(request):
    return render(request,'studenthomepage.html')

def studentcourses(request):
     return redirect('viewstucourses')