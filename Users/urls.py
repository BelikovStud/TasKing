from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as User_Views

urlpatterns = [
    path('register/', User_Views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
]
