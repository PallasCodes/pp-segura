from django.forms import ModelForm

from .models import UserTelegram


class UserTelegramForm(ModelForm):
  class Meta:
    model = UserTelegram
    fields = ['chat_id']
    labels = { 'chat_id': 'Telegram chat ID' }