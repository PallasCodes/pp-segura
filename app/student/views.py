from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User

from .forms import StudentForm, UserForm
from .models import Student
from utils.decorators.user_is_professor import user_is_professor
from telegram.models import UserTelegram
from utils.decorators.requires_telegram_auth import requires_telegram_auth
from telegram.forms import UserTelegramForm


def register_student(request):
  if request.method == 'GET':
    context = { 
                'forms': [
                  UserForm,
                  UserTelegramForm,
                  StudentForm, 
                ]
              }
    
    return render(request, 'register-student.html', context)
  
  elif request.method == 'POST':
    student_form = StudentForm(request.POST)
    user_form = UserForm(request.POST)
    user_telegram_form = UserTelegramForm(request.POST)
    
    if student_form.is_valid():
      user = User.objects.create_user(
        username=request.POST['username'], 
        email=request.POST['email'], 
        password=request.POST['password'])
      
      Student.objects.create(
        user=user, 
        registration_number=request.POST['registration_number'], 
        full_name=request.POST['full_name'])
      
      UserTelegram.objects.create(user=user, chat_id=request.POST['chat_id'])

      return redirect('login')

    else:
      context = {
        'forms': [
          user_form,
          user_telegram_form,
          student_form, 
        ]
      }
      
      return render(request, 'register-student.html', context)
  
  else:
    return Http404()


@login_required
@user_is_professor
@requires_telegram_auth
def students_list(request):
  if request.method == 'GET':
    students = Student.objects.all()
    return render(request, 'students-list.html', { 'students': students })
  
  else:
    return Http404()