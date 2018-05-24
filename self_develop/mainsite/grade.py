from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages 
from .models import Student, Department, Course, Studied



def grade(request):

    myString= "this is a python string."
    data={  'student': Student.objects.all(),
            'department':Department.objects.all(),
            'course':Course.objects.all(),
            'studied':Studied.objects.all()
           }
    return render(request,'grade.html',{"myString": myString},data)
