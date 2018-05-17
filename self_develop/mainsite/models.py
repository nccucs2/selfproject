from django.db import models

# Create your models here.

class Student(models.Model):
    Student_ID = models.IntegerField(default=0)
    Name = models.CharField(max_length=200)
    def __int__(self):
        return self.Student_ID
