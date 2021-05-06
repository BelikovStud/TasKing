from django.contrib import admin
from .models import Group

@admin.register(Group)
class GroupAdminConfig(admin.ModelAdmin):
    list_display = ('creator','prize')
