from django.db import models
from django.contrib.auth.models import User
from Group.models import Group
from Connections.models import GroupUserConnection


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    crowns = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} profile'

    def is_user_in_group(self, grp):
        if self.user != grp.creator:
            qs = GroupUserConnection.get_all_users_of_group(grp)
            for grp_user_connection in qs:
                if grp_user_connection.user == self.user:
                    return True
            return False
        else:
            return True
