from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from Guardian.decorators import unauthenticated_user, allowed_users, admin_only
from .models import UserForm
from Oracle.models import Employee
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from Oracle.views import *
# Create your views here.

@unauthenticated_user
def SignUp(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            user = form.save()
            group = Group.objects.get(name='employee')
            user.groups.add(group)
            Employee.objects.create(user=user)
            return redirect('/guardian/login/')
        else:
            messages.error(request, 'We got some errors dude!')
    context = {
        'form': form,
    }
    return render(request, 'Guardian/SignUp.html', context)

#Login
@unauthenticated_user
def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully!!!')
                return redirect('/')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'Guardian/login.html', context)


def Logout(request):
    logout(request)
    return redirect('/guardian/login/')

