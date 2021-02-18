from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def home(request):
    context = {}
    return render(request, "accounts/home.html", context)


def register(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account Created for " + username)
            return redirect("loginPage")
    context = {"form": form}
    return render(request, "accounts/register.html", context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Username or password is incorrect")
    context = {}
    return render(request, "accounts/login.html", context)


def logoutPage(request):
    logout(request)
    return redirect("loginPage")


@login_required
def index(request):
    tasks = Task.objects.order_by("complete", "due")
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("index")

    context = {"tasks": tasks, "form": form}
    return render(request, "index.html", context)


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {"form": form}

    return render(request, "update.html", context)


def deleteTask(request, task_id):
    item = Task.objects.get(id=task_id)
    if request.method == "POST":
        item.delete()
        return redirect("index")
    return render(request, "delete.html", {"item": item})
