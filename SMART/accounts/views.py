from django.shortcuts import render, redirect
from accounts.forms import (
    RegistrationForm,
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
#f rom django.contrib.auth import update_session_auth_hash
#from django.contrib.auth.decorators import login_required




# Create your views here.
def home(request):
    numbers = [1,2,3,4,5]
    name = 'Roshani'

    args ={'myname': name}
    return render(request, 'accounts/home.html',args)


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/accounts/login')

    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)

#@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)
