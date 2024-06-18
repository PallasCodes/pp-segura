from django.db import models
from django.contrib.auth.models import User


class UserTelegram(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  chat_id = models.CharField(max_length=30, unique=True)
