from django.shortcuts import render, redirect
from .models import Profile
from .forms import registerForm


def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid:
            new_user = form.save()
            new_profile = Profile(user=new_user)
            new_profile.save()
            return redirect('home')
    else:
        form = registerForm()
    return render(request, 'Users/register.html',{'form': form})


def login(render):
    if request.method =='POST':
        aba = 2
    else:
        return render(request, 'Users/login.html')