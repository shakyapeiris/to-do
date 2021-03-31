from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Your account created successfully")
            return redirect('login')

        else:
            messages.info(request, "Some of your data insterted is not valid. Please try again")
            return redirect('register')

    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def loginPage(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user_create = authenticate(username = username, password = password)

        if user_create is not None:
            login(request, user_create)
            return redirect('home')

        else:
            messages.info(request, "Some of your login credentials are wrong")
            return redirect('login')

    return render(request, 'login.html', {})

@login_required(login_url='login')
def home(request):
    
    form = addTask()

    if request.method == "POST":
        form = addTask(request.POST)
        if form.is_valid():
            form.save(commit=False).user = request.user
            form.save()
            
            return redirect('home')
        else:
            return redirect('login')

    opt = works.objects.filter( user=request.user )
    context = {
        'form':form,
        'opt':opt
    }
    return render(request, 'home.html', context)


def logoutPage(request):
    logout(request)
    messages.info(request, "You are successfully logged out")
    return redirect('login')

def delete(request, my_task):
    works.objects.get(id = my_task).delete()
    return redirect('home')

def update(request, up_task):
    obj = works.objects.get(id = up_task)
    
    form = addTask(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return redirect('home')
        

    return render(request, 'update.html', {'form':form})