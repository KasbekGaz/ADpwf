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
# para la hora y fecha de ahora
from django.utils import timezone



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

##La parte de las tareas vista unicamente
@login_required
def tarea(request):
    tasks = Tarea.objects.filter(asignado_a = request.user, Fcompletado__isnull=True)
    return render(request, 'Vtareas.html', {'tasks':tasks})
## Parte de vista en tarea de completado
@login_required
def tareas_c(request):
    tasks = Tarea.objects.filter(asignado_a=request.user, Fcompletado__isnull = False).order_by('-Fcompletado')
    return render(request, 'Vtareas.html', {'tasks':tasks})


#### AQUI EMPIEZA EL CRUD  ####
#para crear tareas con el formulario
@login_required
def nuevatarea(request):
    if request.method == 'GET':
        return render(request, 'Ctareas.html', {
            'form': TareaForm(),
        })
    else:
        try:
            form = TareaForm(request.POST, request.FILES)
            if form.is_valid():
                nueva_tarea = form.save(commit=False)
                nueva_tarea.creado_por = request.user
                nueva_tarea.save()
                return redirect('vistatarea')
        except:
            return render(request, 'Ctareas.html', {
                'form': TareaForm,
                'error': 'Algo salió mal, verifica los campos.'
            })


#############
# def nuevatarea(request):
#     if request.method == 'GET':
#         return render(request, 'Ctareas.html',{
#            'form': TareaForm(), 
#         })
#     else:
#         try:
#             form = TareaForm(request.POST, request.FILES)
#             nueva_tarea = form.save(commit=False)
#             nueva_tarea.creado_por = request.user
#             nueva_tarea.save()
#             return redirect('vistatarea')
#         except:
#             return render(request,'Ctareas.html', {
#                 'form': TareaForm,
#                 'error': 'Algo salio mal verifique los campos. !!'
#             })


#Detalles de la tarea:
@login_required
def detalles_tarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk=tarea_id, asignado_a=request.user)
        form = TareaForm(instance=tarea)
        return render (request, 'detalles_T.html',{
            'task': tarea,
            'form': form
        })
    else:
        try:
            tarea = get_object_or_404(Tarea, pk=tarea_id, asignado_a=request.user)
            form = TareaForm(request.POST, request.FILES, instance=tarea)
            #form.save()
            #return redirect('vistatarea')
            if form.is_valid():
                tarea = form.save(commit=False)
                tarea.archivo_adjunto = request.FILES.get('archivo_adjunto')  # Manejar el archivo adjunto
                tarea.save()
                return redirect('vistatarea')
        except ValueError:
            return render(request, 'detalles_T.html', {
            'task': tarea,
            'form': form,
            'error': 'Error al actuzalizar los datos. Intente de nuevo.'
            })


    #Completar una tarea con la fecha
@login_required
def completar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, asignado_a=request.user)
    if request.method == 'POST':
        tarea.Fcompletado = timezone.now()
        tarea.save()
        return redirect('vistatarea')
    
    # Eliminar la tarea
@login_required
def delete_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, asignado_a=request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('vistatarea')