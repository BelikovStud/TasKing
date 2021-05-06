from django.urls import path
from . import views

urlpatterns = [
    path('my-groups', views.my_groups, name='mygroups'),
    path('group/<group_id>/', views.view_group, name='mygroups'),
    path('assign/<task_id>/', views.assign, name='assign'),
]
