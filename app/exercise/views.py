from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
import uuid
from datetime import date, datetime
from django.contrib import messages

from student.models import Student
from .models import Exercise, HomeWork
from .forms import ExerciseForm
from utils.decorators.user_is_professor import user_is_professor
from utils.evaluador import evaluar
from utils.decorators.requires_telegram_auth import requires_telegram_auth


@login_required
@requires_telegram_auth
def exercises_list(request):
  if request.method == 'GET':
    exercises = Exercise.objects.all()
    return render(request, 'exercises-list.html', { 'exercises': exercises })
  else:
    return Http404()
  
  
@login_required
@user_is_professor
@requires_telegram_auth
def register_exercise(request):
  if request.method == 'GET':
    return render(request, 'register-exercise.html', { 'form': ExerciseForm })
  
  elif request.method == 'POST':
    form = ExerciseForm(request.POST, request.FILES)
    
    if form.is_valid():
      form.save()
      messages.success(request, 'Ejercicio registrado correctamente')
      return redirect('exercises_list')
    
    else:
      return render(request, 'register-exercise.html', { 'form': form })
    
  else:
    return Http404()
  
  
@login_required
@requires_telegram_auth
def exercise_detail(request, id):
  exercise = get_object_or_404(Exercise, pk=id)
  homework = HomeWork.objects.filter(exercise=exercise).filter(student__pk=request.user.id).first()
  today = date.today()
  
  context = { 'exercise': exercise, 'homework': homework, 'today': today }
  
  if request.session['is_professor']:
    homeworks = HomeWork.objects.filter(exercise__pk=id)
    context['homeworks'] = homeworks 
  
  return render(request, 'exercise.html', context)


@login_required
@requires_telegram_auth
def register_homework(request):
  if request.method == 'POST':
    exercise = Exercise.objects.get(pk=request.POST['exercise'])    
    
    if exercise.end_date > date.today():
      student = Student.objects.get(pk=request.user.id)
      homework = HomeWork.objects.create(student=student, exercise=exercise)
      homework.code.save(str(uuid.uuid4()) + '.py', request.FILES['file'])
      result = evaluar(homework.code.path, exercise.cases.path)
      homework.score = result.count(True)
      homework.save()
      messages.success(request, 'Tú tarea ha sido entregada')
    
    return redirect('exercise_detail', id=exercise.id)
    
  else:
    return Http404()
  
  
@login_required
@user_is_professor
@requires_telegram_auth
def delete_exercise(request, id):
   exercise = get_object_or_404(Exercise, pk=id)
   exercise.delete()
   messages.success(request, 'Ejercicio eliminado correctamente')
   
   return redirect('exercises_list')