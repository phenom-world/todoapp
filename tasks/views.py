from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Task.objects.order_by('complete', 'due')
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'index.html', context)


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'update.html', context)


def deleteTask(request, task_id):
    item = Task.objects.get(id=task_id)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    return render(request, 'delete.html', {'item': item})
