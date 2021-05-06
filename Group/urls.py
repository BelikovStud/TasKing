from django.urls import path
from . import views as Group_Views

urlpatterns = [
    path('create/', Group_Views.create_group_view, name='create_group'),
]
