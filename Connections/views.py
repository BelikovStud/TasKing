from django.shortcuts import render, redirect
from .models import GroupUserConnection, GroupTaskConnection
from Group.models import Group
from django.contrib.auth.models import User
from Users.is_user_in_group import is_user_in_group
from Users.models import Profile

def my_groups(request):
    grps = GroupUserConnection.get_all_groups_of_user(request.user)
    return render(request, 'Connections/mygroups.html', {'groups':grps})


def view_group(request, group_id):
    curr_grp = Group.objects.filter(id=group_id).first()
    if not curr_grp:
        return redirect('home')
    elif not is_user_in_group(request.user,curr_grp):
        return redirect('home')
    else:
        name = curr_grp.name
        prize = curr_grp.prize
        tasks = GroupTaskConnection.get_all_tasks_of_group(curr_grp)
        participents = GroupUserConnection.get_all_users_of_group(curr_grp)
        return render(request, 'Connections/group.html', {
            'name':name, 
            'prize':prize,
            'tasks':tasks,
            'par':participents
            })

