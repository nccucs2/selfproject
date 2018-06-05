from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class student_info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    major=models.TextField(blank=True)
    name=models.TextField(blank=True)
    number=models.CharField(max_length=10)
