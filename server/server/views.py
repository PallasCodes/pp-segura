from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from utils import telegram
from telegram.models import UserTelegram
import random
import string


def login_view(request): 
    if request.method == 'GET':
      return render(request, "registration/login.html")
    
    elif request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            request.session['telegram_auth'] = False
            
            is_professor = request.user.groups.all().filter(name='professor').exists()
            request.session['is_professor'] = is_professor
            
            user_telegram = UserTelegram.objects.get(user=user)
            auth_token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            message_sent = telegram.send_message(user_telegram.chat_id, auth_token)
            
            if message_sent is not None:
                request.session['auth_token'] = auth_token
                
                return redirect('telegram_auth')
            else:
                pass
        else:
            messages.error(request, "Username or Password does not match...")
            
    return render(request, "registration/login.html")
