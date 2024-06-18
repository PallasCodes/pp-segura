from django.db import models

from student.models import Student


class Exercise(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=500)
  input_description = models.CharField(max_length=200)
  output_description = models.CharField(max_length=200)
  cases = models.FileField(upload_to='cases', blank=True, null=True)
  start_date = models.DateField()
  end_date = models.DateField()
  num_cases = models.IntegerField()
  
  def get_cases_file_name(self):
    return str(self.cases).replace('cases/', '')


class HomeWork(models.Model): 
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
  date = models.DateField(auto_now_add=True, null=True)
  score = models.IntegerField(null=True)
  code = models.FileField(upload_to='code', blank=True, null=True)
  
  def get_homework_file_name(self):
    return str(self.code).replace('code/', '')
