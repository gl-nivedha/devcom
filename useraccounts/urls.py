from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path('register/',views.user_register,name='register'),
    path('login/',views.login,name='login'),
   

]