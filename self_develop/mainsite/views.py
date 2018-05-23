from django.shortcuts import render,render_to_response
from django.core.mail import EmailMessage
from django.template import RequestContext
from django.template import Context, Template
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainsite.models import student_info
def login(request):
    #template = get_template('login.html')
    if request.user.is_authenticated:
        return HttpResponseRedirect('/student/')
    try:
        username = request.POST['usr_id']
        password = request.POST['usr_pass']
        user = auth.authenticate(username=username, password=password)
    except:
        user = None

        #user_id = None
        #user_password = None


    if user is not None:
        if user.is_active:
            auth.login(request,user)
            return HttpResponseRedirect('/student/')
    else:
        if request.POST:
            messages.error(request,'帳號或密碼錯誤!!')
        return render(request,'login.html')



        #return render_to_response('login.html')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/identify/')
        else:
            messages.error(request,'輸入格式有誤!')
    else:
        form = UserCreationForm()
    return render(request,'register.html',{'form':form})
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')
def identify(request):
    if request.POST:
        p=student_info.objects.create(major=request.POST['major'],name=request.POST['name'],number=request.POST['number'])
        p.save();
        return HttpResponseRedirect('/login/')
    return render(request,'identify.html')
def student(request):
    if request.user.is_authenticated:
        return render(request,'student.html')
    else:
        return HttpResponseRedirect('/login/')

def course(request):
    return render(request,'course.html')

def suggest_course(request):
    return render(request,'suggest_course.html')
# Create your views here.
