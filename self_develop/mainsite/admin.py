from django.contrib import admin

# Register your models here.

from .models import Student, Department, Course, Studied

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Studied)
