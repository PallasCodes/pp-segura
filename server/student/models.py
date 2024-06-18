from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  registration_number = models.CharField(max_length=9, unique=True)
  full_name = models.CharField(max_length=80)
  
  def __str__(self):
    return self.full_name