from django.contrib.auth.models import User
from Group.models import Group
from Connections.models import GroupUserConnection

def is_user_in_group(user, grp):
        if user != grp.creator:
            qs = GroupUserConnection.get_all_users_of_group(grp)
            for grp_user_connection in qs:
                if grp_user_connection.user == user:
                    return True
            return False
        else:
            return True