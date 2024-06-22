from django.urls import path

from exercise import views


urlpatterns = [
  path('', views.exercises_list, name='exercises_list'),
  path('register/', views.register_exercise, name='register_exercise'),
  path('register-homework/', views.register_homework, name='register_homework'),
  path('delete/<id>', views.delete_exercise, name='delete_exercise'),
  path('<id>/', views.exercise_detail, name='exercise_detail')
]