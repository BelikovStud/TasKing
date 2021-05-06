from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdminConfig(admin.ModelAdmin):
    list_display = ('assignee','title','points')
