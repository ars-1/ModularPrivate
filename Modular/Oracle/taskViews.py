from django.shortcuts import redirect, render
from Guardian.views import login
from django.contrib.auth.decorators import login_required

from Oracle.forms import TaskForm
from .tasks import Task, TaskStatus

@login_required(login_url='/guardian/login/')
def Tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'Oracle/Tasks/tasks.html', context)


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


def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/oracle/tasksList/')
    context = {
        'task': task,
    }
    return render(request, 'Oracle/Tasks/deleteTask.html', context)