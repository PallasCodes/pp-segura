from django.forms import ModelForm, PasswordInput
from captcha.fields import CaptchaField
from django.contrib.auth.models import User


from .models import Student


class StudentForm(ModelForm):
  captcha = CaptchaField()
  class Meta:
    model = Student
    fields = ['registration_number', 'full_name']
    labels = {
      'registration_number': 'Matricula',
      'full_name': 'Nombre completo'
    }


class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'password', ]
    labels = {
      'username': 'Nombre de usuario',
      'password': 'Contraseña',
      'email': 'Email'
    }
    widgets = {
      'password': PasswordInput()
    }