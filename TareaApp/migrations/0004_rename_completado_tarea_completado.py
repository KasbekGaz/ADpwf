# Generated by Django 4.2 on 2023-05-08 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TareaApp', '0003_tarea_completado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='Completado',
            new_name='completado',
        ),
    ]
