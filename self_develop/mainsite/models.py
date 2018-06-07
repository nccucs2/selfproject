from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
# Create your models here.

#class student_info(models.Model):
#    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
#    major=models.TextField(blank=True)
#    name=models.TextField(blank=True)
#    number=models.CharField(max_length=10)
=======
from django.contrib.auth import get_user_model
from django.conf import settings

class Student(models.Model):
    #Student_ID = models.IntegerField(default=0, primary_key=True)
    student = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    Name = models.CharField(max_length=200,default='SOME STRING')
    def __str__(self):
        return self.Name

class Department(models.Model):
    Name = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return self.Name
    Student_Belong = models.ManyToManyField(Student)

class Course(models.Model):
    AcademicYear = models.IntegerField()
    Semester  = models.IntegerField()
    Code = models.CharField(max_length=50,primary_key=True)
    Name = models.CharField(max_length=200)
    ClassField = models.CharField(max_length=200)
    Credit = models.DecimalField(max_digits=2,decimal_places=1)
    Remark = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.Name

class Studied(models.Model):
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course_Code = models.ForeignKey(Course, on_delete=models.CASCADE)
    Score = models.DecimalField(default=-1,max_digits=4,decimal_places=1)
    GPA = models.DecimalField(default=-1,max_digits=4,decimal_places=1)
    def __str__(self):
        return '%s %s' % (self.Course_Code, self.Student_ID.Name)
>>>>>>> grade
