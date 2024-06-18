from django.urls import path
from telegram import views


urlpatterns = [
  path('auth/', views.auth, name='telegram_auth')
]