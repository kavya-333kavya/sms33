from django.shortcuts import render, redirect


# Create your views here.
def facultyhomeproject(request):
    return render(request,'facultyhomeproject.html')
def viewprofile(request):
    return redirect("facultyprofile")



def facultycourses(request):
    return redirect("viewfaccourses")