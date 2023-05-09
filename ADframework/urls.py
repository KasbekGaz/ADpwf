"""
URL configuration for ADframework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TareaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.casa, name='casa'),
    path('registrar/', views.registro, name='registro'),
    path('inicio/', views.autenticar, name='inicio'),
    path('logout/', views.closesesion, name="CerrarSesion"),
    path('tareas/', views.tarea, name='vistatarea' ),
    path('tareas/crear/', views.nuevatarea, name="crearT"),
    path('tareas/<int:tarea_id>/', views.detalles_tarea, name='detalle_tarea')
    
]