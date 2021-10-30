from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/guardian/login/')
def Dashboard(request):
    return render(request, 'Core/one.html')
