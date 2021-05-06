from django.urls import path
from . import views as User_Views

urlpatterns = [
    path('register/', User_Views.register, name='register'),
]
