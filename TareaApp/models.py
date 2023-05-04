from django.db import models
#para pdoer usar User
from django.contrib.auth.models import User
# Create your models here.



# vamos a crear el modelo de tareas
class Tarea(models.Model):
    titulo = models.CharField(max_length=200) #campo que almacena titulo de la tarea
    descripcion = models.TextField(blank=True) #campo de texto que almacena descripcion
    fecha_limite = models.DateTimeField() #campo de fecha y hora almacedada
    # 4 cosas que relacionan con usuario con tarea
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE) #tarea asignada a usuario con id 
    creado_por = models.ForeignKey(User, related_name='tareas_creadas', on_delete=models.CASCADE) #tarea creada por usuario
    creado_en = models.DateTimeField(auto_now_add=True) #fecha y hora en que se creo al tarea puede ser vista por admin unicamente.
    actualizado_en = models.DateTimeField(auto_now=True) #fecha y hora en que se actualizo la tarea.
    archivo_adjunto = models.FileField(upload_to='archivos/', null=True, blank=True)

    def __str__(self) -> str:
        return self.titulo + ' - Esta tarea es de: -' + self.creado_por.username
    

