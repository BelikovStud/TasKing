from django.db import models
from django.contrib.auth.models import User
from Group.models import Group
from Connections.models import GroupUserConnection


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    crowns = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} profile'

