from django.shortcuts import render, redirect
from django.http import Http404
from utils import telegram
from django.contrib.auth import logout


def auth(request):
  if request.method == 'GET':
    return render(request, 'telegram-auth.html')
  
  elif request.method == 'POST':
    if request.POST['code'] == request.session['auth_token']:
      request.session['telegram_auth'] = True
      return redirect('exercises_list')
    else:
      #TODO: add error message
      logout(request)
      return render(request, 'wrong-telegram-code.html')
    
  else:
    return Http404()