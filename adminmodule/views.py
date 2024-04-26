from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404




# Create your views here.

def projecthomepage(request):
    return render(request,'projecthomepage.html')

def signup(request):
    return render(request,'signup.html')

def studenthomepage(request):
    return render(request,'studenthomepage.html')

def facultyhomeproject(request):
    return render(request,'facultyhomeproject.html')


from django.contrib import messages
from django.contrib.auth.models import User,auth


def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'login.html')



def signup1(request):
    if request.method=='POST':
       username=request.POST['username']
       pass1=request.POST['password']
       pass2=request.POST['password1']
       if pass1==pass2:
           if User.objects.filter(username=username).exists():
              messages.info(request, 'OOPS! Username already taken')
              return render(request,'login.html')
           else:
               user=User.objects.create_user(username=username,password=pass1)
               user.save()
               messages.info(request,'Account created Successfully!')
               return render(request,'login.html')
       else:
           messages.info(request,'Password does not match')
           return render(request,'login.html')





def login1(request):
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            if len(username)==10:
                return redirect('studenthomepage')
            elif len(username)==4:
                return redirect('facultyhomeproject')

        else:
            if username=="admin" and pass1=="admin":
                return redirect('coursehomepage')
            messages.info(request,'Invalid Crendentials!')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

'''
from django.contrib.auth import get_user_model
from django.shortcuts import render

def facultylogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = Faculty.objects.filter(facultyid=username, password=password)
        print(user)
        if user is not None:
            return render(request, 'facultyhomeproject.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
'''

def facultylogin1(request):
    return render(request,'facultylogin.html')
def logout(request):
    auth.logout(request)
    return render(request,'login.html')