from django.urls import path
from . import views as Main_Views

urlpatterns = [
    path('', Main_Views.home_view),
]
