from django.shortcuts import render, redirect
from .models import GroupUserConnection, GroupTaskConnection
from Group.models import Group
from Task.models import Task
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


def assign(request, task_id):
    curr_task = Task.objects.filter(id=task_id).first()
    if not curr_task:
        return redirect('home')
    grp = GroupTaskConnection.objects.filter(task=curr_task).first().group
    if not is_user_in_group(request.user,grp):
        return redirect('home')
    else:
        curr_task.assignee = request.user
        curr_task.save()
        name = grp.name
        prize = grp.prize
        tasks = GroupTaskConnection.get_all_tasks_of_group(grp)
        participents = GroupUserConnection.get_all_users_of_group(grp)
        return render(request, 'Connections/group.html', {
            'name':name, 
            'prize':prize,
            'tasks':tasks,
            'par':participents
            })


def approve(request, task_id):
    curr_task = Task.objects.filter(id=task_id).first()
    if not curr_task:
        return redirect('home')
    grp = GroupTaskConnection.objects.filter(task=curr_task).first().group
    if grp.creator is not request.user:
        return redirect('home')
    else:
        curr_task.approve()
        curr_task.save()
        name = grp.name
        prize = grp.prize
        tasks = GroupTaskConnection.get_all_tasks_of_group(grp)
        participents = GroupUserConnection.get_all_users_of_group(grp)
        return render(request, 'Connections/group.html', {
            'name':name, 
            'prize':prize,
            'tasks':tasks,
            'par':participents
            })


def dsapprove(request, task_id):
    curr_task = Task.objects.filter(id=task_id).first()
    if not curr_task:
        return redirect('home')
    grp = GroupTaskConnection.objects.filter(task=curr_task).first().group
    if grp.creator is not request.user:
        return redirect('home')
    else:
        curr_task.disapprove()
        curr_task.save()
        name = grp.name
        prize = grp.prize
        tasks = GroupTaskConnection.get_all_tasks_of_group(grp)
        participents = GroupUserConnection.get_all_users_of_group(grp)
        return render(request, 'Connections/group.html', {
            'name':name, 
            'prize':prize,
            'tasks':tasks,
            'par':participents
            })