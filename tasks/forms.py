from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Add new task..."}), label=False
    )
    due = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Due Date..."}), label=False
    )
    complete = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "col-10"})
    )

    class Meta:
        model = Task
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
