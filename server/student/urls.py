from django.urls import path

from student import views


urlpatterns = [
    path('register/', views.register_student, name = 'register_student'),
    path('', views.students_list, name = 'students_list'),
]
