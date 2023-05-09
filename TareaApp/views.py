# view.py en la carpeta de Tasks
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
#para poder usar el formulario
from .forms import TareaForm
#importamos el modelo 
from .models import Tarea



def casa(request):
    return render(request, 'casa.html')


def registro(request):
  if request.method == 'GET':
    return render(request, 'registrarse.html', {
        'form': UserCreationForm
     })
  else:
    if request.POST['password1'] == request.POST['password2']:
        try: 
          user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
          user.save()
          login(request, user)
          return redirect('vistatarea')
        except IntegrityError:
           return render(request, 'registrarse.html',{
              'form': UserCreationForm,
              'error': 'El Usuario Ya Existe'
           })
    return render(request, 'registrarse.html',{
       'form': UserCreationForm,
       'error': 'Contraseña no coinciden'
    })


#autenticar un usuario es decir iniciar sesion en su cuenta
def autenticar(request):# autenticar un usuario
    if request.method == 'GET':
        return render(request, 'sesionU.html', {
            'form': AuthenticationForm
        })
    
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None: #Si el usuario no existe
                return render(request, 'sesionU.html',{
                    'form': AuthenticationForm,
                    'error': 'Usuario o contraseña incorrecta'
                })
        else: #si SI existe lo reenvia a TASKS
            login(request, user)
            return redirect('vistatarea')   #cambiar cuando tareas este hecho
        
# Para cerrar sesion
@login_required
def closesesion(request):
    logout(request)
    return redirect('casa')

##La parte de las tareas vista nicamente

def tarea(request):
    tasks = Tarea.objects.filter(asignado_a = request.user)
    return render(request, 'Vtareas.html', {'tasks':tasks})


#para crear tareas con el formulario
def nuevatarea(request):
    if request.method == 'GET':
        return render(request, 'Ctareas.html',{
           'form': TareaForm(), 
        })
    else:
        try:
            form = TareaForm(request.POST)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.creado_por = request.user
            nueva_tarea.save()
            return redirect('vistatarea')
        except:
            return render(request,'Ctareas.html', {
                'form': TareaForm,
                'error': 'Algo salio mal verifique los campos. !!'
            })


#Detalles de la tarea:

def detalles_tarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk=tarea_id, asignado_a=request.user)
        form = TareaForm(instance=tarea)
        return render (request, 'detalles_T.html',{
            'tasks': tarea,
            'form': form
        })
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=tarea_id, asignado_a=request.user)
            form = TareaForm(request.POST, instance=tarea)
            form.save()
            return redirect('vistatarea')

        except ValueError:
            return render(request, 'tasks_detalles.html', {
            'task': tarea,
            'form': form,
            'error': 'Error al actuzalizar los datos. Intente de nuevo.'
            })