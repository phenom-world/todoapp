from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}), label = False)
	due= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due Date...'}), label = False)
	complete = forms.BooleanField(required= False, widget= forms.CheckboxInput(attrs={'class':"col-1"}))

	class Meta:
		model = Task
		fields = '__all__'
