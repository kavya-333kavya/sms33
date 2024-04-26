from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password= models.CharField(max_length=100,blank=False)

    class Meta:
        db_table="admin_table"

    def str(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSE&IT", "CSIT"))
    department = models.CharField(max_length=100, blank=False,choices=department_choices)

    program_choices = (("B.Tech", "B.Tech"), ("M.Tech", "M.Tech"))
    program = models.CharField(max_length=50, blank=False, choices=program_choices)

    academic_choices = (("2023-24", "2023-24"), ("2022-23", "2022-23"))
    academicyear = models.CharField(max_length=20, blank=False,choices=academic_choices)

    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)

    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table="course_table"

    def str(self):
        return self.coursecode

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100,blank=False)

    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"),("OTHER", "OTHER"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(HONORS)"), ("CSE&IT", "CSIT"))
    department=models.CharField(max_length=50,blank=False,choices=department_choices)

    program_choices = (("B.TECH", "B.TECH"), ("M.TECH", "M.TECH"))
    program = models.CharField(max_length=50, blank=False,choices=program_choices)

    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)

    year = models.IntegerField(blank=False)
    password = models.CharField(max_length=100, blank=False,default="klu123")
    email=models.CharField(max_length=100,blank=False,unique=True)
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="student_table"

    def str(self):
        return str(self.studentid)

class Faculty(models.Model):
    id=models.AutoField(primary_key=True)
    facultyid=models.BigIntegerField(blank=False,unique=True)
    fullname=models.CharField(max_length=100,blank=False)

    gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHER", "OTHER"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices)

    department_choices = (("CSE(Regular)", "CSE(Regular)"), ("CSE(HONORS)", "CSE(HONORS)"), ("CSIT", "CSIT"))
    department=models.CharField(max_length=50,blank=False,choices=department_choices)

    qualification_choices = (("M.Tech", "M.Tech"), ("Ph.d", "Ph.d"))
    qualification = models.CharField(max_length=50, blank=False,choices=qualification_choices)

    designation_choices = (("professor", "Professor"), ("Associate professor", "Associate Professor"), ("Assistant professor", "Assintant Professor"))
    designation = models.CharField(max_length=50, blank=False,choices=designation_choices)

    password = models.CharField(max_length=100, blank=False,default="klu123")
    email=models.CharField(max_length=100,blank=False,unique=True)
    contact=models.CharField(max_length=20,blank=False,unique=True)

    class Meta:
        db_table="faculty_table"

    def str(self):
        return str(self.facultyid)

class StudentCourse(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        db_table = "student_course"

    def __str__(self):
        return f"{self.student.fullname} - {self.course.coursetitle}"



class FacultyCourse(models.Model):
    id = models.AutoField(primary_key=True)
    facultyid=models.BigIntegerField(blank=False,)
    courseid = models.BigIntegerField( blank=False,)
    class Meta:
        db_table="faccou_table"

    def str(self):
        return str(self.facultyid)