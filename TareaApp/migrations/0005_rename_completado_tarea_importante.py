# Generated by Django 4.2 on 2023-05-09 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TareaApp', '0004_rename_completado_tarea_completado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='completado',
            new_name='importante',
        ),
    ]
