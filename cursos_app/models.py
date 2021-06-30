from __future__ import unicode_literals
from django.db import models
import datetime

class CursoManager(models.Manager):
    def validador_basico(self, postData):
        errors = {}

        if len(postData['nombre']) < 5:
            errors['nombre'] = "El nombre del curso no pude tener menos de 5 caracteres";

        if len(postData['descripcion']) < 15:
            errors['descripcion'] = "La descripción del curso no puede tener menos de 15 caracteres";
        
        return errors

class Descripcion(models.Model):
    det_descripcion =  models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.ForeignKey(Descripcion, related_name="descripcion_cursos", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CursoManager()

class Comentario(models.Model):
    nombre = models.CharField(max_length=255) #hace referencia al nombre de la persona que realizó el comentario
    apellido = models.CharField(max_length=255)
    det_comentario = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, related_name="comentarios", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

