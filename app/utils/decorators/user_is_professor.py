from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def user_is_professor(view_func):
  def wrapper_func(request, *args, **Kwargs):
    is_professor = request.user.groups.all().filter(name='professor').exists()
    
    if is_professor:
        return view_func(request, *args, **Kwargs)
    else:
        return HttpResponseForbidden('No tienes permisos para acceder a este recurso')
      
  return wrapper_func