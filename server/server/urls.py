from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from exercise.views import exercises_list

from server import views


urlpatterns = [
    path('', exercises_list),
    path('captcha/', include('captcha.urls')),
    path('telegram/', include('telegram.urls')),
    path('accounts/login/', views.login_view, name='login'),
    path('exercises/', include('exercise.urls'), name='exercise'),
    path('students/', include('student.urls'), name='student'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)