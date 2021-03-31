from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms

class CreateUserForm (UserCreationForm):
    username = forms.CharField(max_length=200, label="Enter your username",required=True, widget= forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    email = forms.EmailField(max_length=200, label = "Enter your email",required= True, widget= forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))

    password1 = forms.CharField(max_length=200, label="Enter a password",required=True,  widget= forms.PasswordInput(
        attrs={
            'class':'form-control'
        }
    ))

    password2 = forms.CharField(max_length=200, label="Enter the password again!",required=True ,widget= forms.PasswordInput(
        attrs={
            'class':'form-control',
        }
    ))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class DateInput(forms.DateInput):
    input_type = "date"

class TimeInput(forms.TimeInput):
    input_type = "time"

class addTask(forms.ModelForm):
    task_name = forms.CharField(required=True, max_length=200, label="Enter the task", widget=forms.TextInput(
        attrs={
            "class":"form-control",
            "placeholder":"Enter your task"
        }
    ))

    due_date = forms.DateField(widget=DateInput(
        attrs={
            "class":"form-control"
        }
    ), label="Enter the due_date")

    due_time = forms.TimeField(label="Enter the due time", widget=TimeInput(
        attrs={
            'class':'form-control'
        }
    ))

    class Meta:
        model = works
        fields = ["task_name", "due_date", "due_time"]