from django.contrib import admin
#from .models import student_info
# Register your models here.

<<<<<<< HEAD
#admin.site.register(student_info)
=======
from .models import Student, Department, Course, Studied

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Studied)
>>>>>>> grade
