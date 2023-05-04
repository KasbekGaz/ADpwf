from django.contrib import admin
from .models import Tarea
# Register your models here.

admin.site.register(Tarea)
##esto es para que podamos modificar datos en la tabla de tareas en la pagina principal de admin

class TareaAdmin(admin.ModelAdmin):
    readonly_fields = ("creado_en",)