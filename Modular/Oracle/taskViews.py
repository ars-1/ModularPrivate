from django.shortcuts import redirect, render
from Guardian.views import login
from django.contrib.auth.decorators import login_required
from Guardian.decorators import admin_only

from Oracle.forms import TaskForm
from .tasks import Task, TaskStatus

@login_required(login_url='/guardian/login/')
@admin_only
def Tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'Oracle/Tasks/tasks.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def addTask(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/oracle/tasksList/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Tasks/addTask.html', context)


@login_required(login_url='/guardian/login/')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('/oracle/tasksList/')
    context = {
        'form': form,
    }
    return render(request, 'Oracle/Tasks/addTask.html', context)

@login_required(login_url='/guardian/login/')
@admin_only
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/oracle/tasksList/')
    context = {
        'task': task,
    }
    return render(request, 'Oracle/Tasks/deleteTask.html', context)