# view.py en la carpeta de Tasks
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.
def casa(request):
    return render(request, 'casa.html')
def registro(request):
  if request.method == 'GET':
    return render(request, 'registrarse.html', {
        'form': UserCreationForm
     })
  else:
    if request.POST['contraseña1'] == request.POST['contraseña2']:
        try: 
          user = User.objects.create_user(username=request.POST['username'], password=request.POST['contraseña1'])
          user.save()
          login(request, user)
          return redirect('casa.html')
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
                return render(request, 'signin.html',{
                    'form': AuthenticationForm,
                    'error': 'Usuario o contraseña incorrecta'
                })
        else: #si SI existe lo reenvia a TASKS
            login(request, user)
            return redirect('casa')   #cambiar cuando tareas este hecho
        
# Para cerrar sesion
@login_required
def closesesion(request):
    logout(request)
    return redirect('casa')

