from django.shortcuts import render, redirect
from .forms import GroupCreationForm
from Connections.models import GroupUserConnection


def create_group_view(request):
    if request.method == 'POST':
        create_group_form = GroupCreationForm(request.POST)
        if create_group_form.is_valid():
            new_group = create_group_form.save(commit=False)
            new_group.creator = request.user
            new_group.save()
            new_grp_user_connection = GroupUserConnection(group=new_group, user=request.user, score=0)
            new_grp_user_connection.save()
            return redirect('mygroups')
    else:
        create_group_form = GroupCreationForm()
    return render(request, 'Group/create_group.html', {'form': create_group_form})
