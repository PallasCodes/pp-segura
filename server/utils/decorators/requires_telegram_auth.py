from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django.contrib.auth import logout


def requires_telegram_auth(view_func):
  def wrapper_func(request, *args, **Kwargs):
    if request.session['telegram_auth']:
        return view_func(request, *args, **Kwargs)
    else:
        logout(request)
        return redirect('login')
      
  return wrapper_func