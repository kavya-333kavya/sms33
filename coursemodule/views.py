from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Admin, Faculty, Course, Student
def admincourse(request):
    return render(request,"admincourse.html")

def addcourse(request):
    return render(request,"addcourse.html")

def insertcourse(request):
    if request.method=="POST":
        dept=request.POST["dept"]
        program=request.POST["program"]
        ay=request.POST["ay"]
        sem=request.POST["sem"]
        year=request.POST["year"]
        ccode=request.POST["ccode"]
        ctitle=request.POST["ctitle"]

        course=Course(department=dept,program=program,academicyear=ay,semester=sem,year=year,coursecode=ccode,coursetitle=ctitle)

        Course.save(course)

        message="Course Added Successfully"

        return render(request,"addcourse.html",{"msg":message})

def coursenavbar(request):
        return render(request, 'coursenavbar.html')



def coursehomepage(request):
        return render(request, 'coursehomepage.html')

def viewcourses(request):
    courses=Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursedata":courses,"count":count})

def deletecourse(request):
    faculty = Course.objects.all()
    count = Course.objects.count()

    return render(request, "deletecourse.html", {"facultydata": faculty, "count": count})

def coursedeletion(request,fid):
    Course.objects.filter(id=fid).delete()
    #return HttpResponse("Faculty deleted Successfully")
    return redirect("deletecourse")

def addfac(request):
    return render(request,'addfaculty.html')

def addfaculty(request):
    if request.method=="POST":
        facultyid=request.POST["facultyid"]
        fullname=request.POST["fullname"]
        gender=request.POST["gender"]
        department=request.POST["department"]
        qualification=request.POST["qualification"]
        designation=request.POST["designation"]
        password=request.POST["password"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        faculty=Faculty(facultyid=facultyid,fullname=fullname,gender=gender,department=department,qualification=qualification,designation=designation,password=password,email=email,contact=contact)
        Faculty.save(faculty)
        s=User.objects.create_user(username=facultyid,password=password)
        s.save()
    message="Faculty Added Successfully!"

    return render(request,"addfaculty.html",{"msg":message})
def viewfaculty(request):
    courses=Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":courses,"count":count})

def deletefaculty(request):
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()


    return render(request,"deletefaculty.html",{"facultydata":faculty,"count":count})

def facultydeletion(request,fid):
    Faculty.objects.filter(id=fid).delete()
    #return HttpResponse("Faculty deleted Successfully")
    return redirect("deletefaculty")


from django.shortcuts import render, redirect
from .models import Faculty, FacultyCourse

from django.shortcuts import render, redirect
from .models import FacultyCourse, Faculty


def faccou(request, cc):
    faculty_list = Faculty.objects.all()
    if request.method == "POST":
        faculty_id = request.POST.get("fruits")  # Correcting the form field name
        assign = FacultyCourse(facultyid=faculty_id, courseid=cc)  # Correcting model field names
        assign.save()
        print("Submitted")
        return redirect('assign1')  # Redirecting to a success URL after successful form submission

    message = "Faculty Added Successfully!"
    return render(request, "faccou.html", {"list": faculty_list, "msg": message})


def assigns(request):

    if request.method=="POST":
        coursecode=request.POST["coursecode"]
        facultyid=request.POST["facultyid"]
        assign=FacultyCourse(facultyid=facultyid,courseid=coursecode)
        assign.save()

    message = "Faculty Added Successfully!"

    return render(request, "assign1.html", {"msg": message})

def assign(request):
    return render(request,'assign.html')
def assign1(request):
    faculty = Course.objects.all()
    return render(request, "assign1.html", {"facultydata": faculty})


def addstu(request):
    return render(request,'addstudent.html')

def addstudent(request):
    if request.method=="POST":
        studentid=request.POST["studentid"]
        fullname=request.POST["fullname"]
        gender=request.POST["gender"]
        department=request.POST["department"]
        program=request.POST["program"]
        semester=request.POST["semester"]
        year=request.POST["year"]
        password=request.POST["password"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        student=Student(studentid=studentid,fullname=fullname,gender=gender,department=department,program=program,semester=semester,year=year,password=password,email=email,contact=contact)
        Student.save(student)
        s = User.objects.create_user(username=studentid, password=password)
        s.save()


    message="Student Added Successfully!"

    return render(request,"addstudent.html",{"msg":message})
def viewstudent(request):
    courses=Student.objects.all()
    count = Student.objects.count()
    return render(request,"viewstudent.html",{"studentdata":courses,"count":count})

def deletestudent(request):
    student=Student.objects.all()
    count = Student.objects.count()


    return render(request,"deletestudent.html",{"studentdata":student,"count":count})

def studentdeletion(request,sid):
    Student.objects.filter(id=sid).delete()
    #return HttpResponse("Faculty deleted Successfully")
    return redirect("deletestudent")



from django.shortcuts import render
from .models import Student
from django.contrib.auth.models import User

def studentprofile1(request):
    return render(request,'studentprofile.html')
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Student

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Student

@login_required
def studentprofile(request):
    # Fetch the currently logged-in user
    user = request.user

    # Fetch the corresponding student details
    try:
        student = Student.objects.get(studentid=user.username)
    except Student.DoesNotExist:
        student = None

    return render(request, 'studentprofile.html', {'student': student})

def facultyprofile(request):
    # Fetch the currently logged-in user
    user = request.user

    # Fetch the corresponding student details
    try:

        student = Faculty.objects.get(facultyid=user.username)
        print(student)
    except Student.DoesNotExist:
        student = None

    return render(request, 'facultyprofile.html', {'student': student})


from django.shortcuts import render
from .models import Faculty, Course, FacultyCourse
from django.contrib.auth.decorators import login_required

@login_required
def viewfaccourses(request):
    user = request.user

    try:
        # Retrieve the faculty object associated with the logged-in user
        fac = Faculty.objects.get(facultyid=user.username)

        # Retrieve all courses associated with the faculty
        faculty_courses = FacultyCourse.objects.filter(facultyid=fac.facultyid)
        course_ids = [fc.courseid for fc in faculty_courses]
        courses = Course.objects.filter(id__in=course_ids)

        # Count the total number of courses
        count = courses.count()
    except Faculty.DoesNotExist:
        # If no faculty object found for the user, set fac to None and initialize an empty list of courses
        fac = None
        courses = []
        count = 0

    # Render the template with the retrieved data
    return render(request, "facultycourses.html", {"coursedata": courses, "count": count, "fac": fac})


def viewstucourses(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    stu=FacultyCourse.objects.all()
    fac=Faculty.objects.all()
    return render(request, "studentcourses.html", {"coursedata": courses, "count": count,"stu":stu,"fac":fac,})


from django.shortcuts import render, redirect
from .models import Course, Student, Faculty, StudentCourse

def selectcourse1(request):
    return render(request,'selectcourse.html')
from django.shortcuts import render, redirect
from .models import Student, Course, Faculty, StudentCourse

def selectcourse(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        course_id = request.POST.get("course_id")
        faculty_id = request.POST.get("faculty_id")

        # Fetch student, course, and faculty objects based on IDs
        student = Student.objects.get(id=student_id)
        course = Course.objects.get(id=course_id)
        faculty = Faculty.objects.get(id=faculty_id)

        # Create a new StudentCourse object and save it
        StudentCourse.objects.create(student=student, course=course, faculty=faculty)

        return redirect("student_courses")  # Redirect to student courses page after successful selection

    # Fetch all courses and faculties to display in the form
    courses = Course.objects.all()
    faculties = Faculty.objects.all()
    return render(request, "selectcourse.html", {"courses": courses, "faculties": faculties})
