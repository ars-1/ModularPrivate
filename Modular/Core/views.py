from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Oracle.models import Attendance, Employee, Task

# Create your views here.

@login_required(login_url='/guardian/login/')
def Dashboard(request):
    emp = Employee.objects.all().count()
    attendances = Attendance.objects.all()[0:emp][::-1]
    tasks = Task.objects.all()[0:10][::-1]
    context = {
        'attendances': attendances,
        'tasks': tasks,
    }
    return render(request, 'Core/one.html', context)
