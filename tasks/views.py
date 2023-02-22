from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import Tasks
from .forms import Task_maker
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home (request) :
 return render (request, 'home.html')

def signup (request):
    if request.method == 'GET':
        return render (request, 'signup.html', {"form": UserCreationForm } )
    else: 
        if request.POST['password1'] == request.POST['password2'] :
          try:
                user=User.objects.create_user(username=request.POST["username"], password=request.POST["password1"] )
                user.save()
                login(request,user) #esto es para guardar en las cookies
                return redirect('tareas')
          except IntegrityError :
                return render (request, 'signup.html', {"form": UserCreationForm, 'error': "el usuario ya existe" } )    
          
        else:
            if request.POST['password1'] != None :
                return render (request, 'signup.html', {"form": UserCreationForm, 'error':'password doesn`t match' } )
            else:
                return render (request, 'signup.html', {"form": UserCreationForm, 'error':'es necesario llenar los campos' } )
            


@login_required         
def tasks (request):
    tasks= Tasks.objects.filter(user=request.user,  date_done__isnull = True ) 
    return render (request, 'tasks.html', {"tareitas": tasks,  } )

@login_required
def completed (request):
    tasks= Tasks.objects.filter(user=request.user,  date_done__isnull = False).order_by('date_done') 
    return render (request, 'tasks.html', {"tareitas": tasks} )

@login_required
def log_out (request):
    logout(request)
    return redirect('index')



def signin (request):
    if request.method == 'GET':
        return render (request, 'signin.html' , {
            "form": AuthenticationForm
        } )
    else :
        user=authenticate(request, username = request.POST['username'], password = request.POST['password'])
         
        if user is None: 
            return render (request, 'signin.html' , {
            "form": AuthenticationForm,
            "error": 'no existe ese username o el password',
            } )
        else:
            login(request, user)     
            return redirect('tareas')  


@login_required        
def createtasks(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': Task_maker() })
    else: 
        try:
            print(request.POST)
            task=Task_maker(request.POST)     
            new_task = task.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tareas')
        except ValueError :
            return render(request, 'create_task.html', {'form': Task_maker(), 'error':'chala la pachala. Te falta logearte'})

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':    
        task= get_object_or_404( Tasks, pk=task_id, user = request.user)
        form = Task_maker(instance=task)
        return render(request, 'task_detail.html', { "task": task, 'form': form })
    else:
        try:    
            task= get_object_or_404( Tasks, pk=task_id, user = request.user)
            form = Task_maker(request.POST, instance=task)
            form.save()
            return redirect('tareas')
        except ValueError:
            el_error = 'error actualizando'
            return render(request, 'task_detail.html', { "task": task, 'form': form , 'error': el_error })

@login_required        
def task_complete(request, id):
    task= get_object_or_404( Tasks, pk= id, user = request.user)
    if request.method == 'POST':
        task.date_done = timezone.now()
        task.save()
        return redirect('tareas')
    
@login_required
def task_delete(request, id):
    task= get_object_or_404( Tasks, pk= id, user = request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tareas')
    
