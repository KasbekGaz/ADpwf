# Generated by Django 4.2 on 2023-05-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TareaApp', '0005_rename_completado_tarea_importante'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='Fcompletado',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]