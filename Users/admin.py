from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdminConfig(admin.ModelAdmin):
    list_display = ('user','crowns')