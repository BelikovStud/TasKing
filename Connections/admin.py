from django.contrib import admin
from .models import GroupUserConnection, GroupTaskConnection

@admin.register(GroupTaskConnection)
class GroupTaskConnectionAdminConfig(admin.ModelAdmin):
    list_display = ('group','task')


@admin.register(GroupUserConnection)
class GroupUserConnection(admin.ModelAdmin):
    list_display = ('group','user')