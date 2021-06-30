from django.shortcuts import redirect, render, HttpResponse
from cursos_app.models import Descripcion, Comentario, Curso
from time import gmtime, strftime, localtime
from datetime import datetime
from django.contrib import messages

def index(request):
    context = {
                'cursos' : Curso.objects.all(),
                }
    return render(request, 'cursos.html', context)


def nuevo_curso(request):
    if request.method == 'GET':
        return redirect(f'/')
    
    if request.method == 'POST':
        print(request.POST)
        # pasar los datos al método que escribimos y guardar la respuesta en una variable llamada errors
        errors = Curso.objects.validador_basico(request.POST)

        if len(errors) > 0:
            # si el diccionario de errores contiene algo, recorra cada par clave-valor y cree un mensaje flash
            for key, value in errors.items():
                messages.error(request, value);
            # redirigir al usuario al formulario para corregir los errores

        else:
            # si el objeto de errores está vacío, eso significa que no hubo errores.
            new_curso = Curso.objects.create(
                                            nombre = request.POST['nombre'],
                                            descripcion = Descripcion.objects.create(det_descripcion = request.POST['descripcion']) 
                                            )

            messages.success(request, f"El Curso { new_curso.nombre } fue agregado con exito.")
            # redirigir a la ruta de exito
        
        return redirect(f'/')     


def ver_curso(request,id_curso):
    context = {
                'curso' : Curso.objects.get(id=id_curso),
                'comentarios' : Comentario.objects.filter(curso=id_curso)
                }
    return render(request, 'detalle_curso.html', context)
    



def editar_curso(request, id_curso):
    context = {
                'curso' : Curso.objects.get(id=id_curso),
                }
    
    if request.method == 'GET':
        return render(request, 'editar_curso.html', context)
        
    if request.method == 'POST':
        curso = Curso.objects.get(id=id_curso)

        curso.nombre = request.POST['nombre']
        curso.descripcion.det_descripcion = request.POST['descripcion'] 
        curso.save()

        return redirect(f'/curso/{curso.id}/editar')     


def eliminar_curso(request):

    return

#===================== COMENTARIOS ==========================
def nuevo_comentario(request, id_curso):
    new_comentario = Comentario.objects.create(
                                            nombre = request.POST['nombre'],
                                            apellido = request.POST['apellido'],
                                            det_comentario = request.POST['comentario'],
                                            curso = Curso.objects.get(id=id_curso), 
                                            )

    return redirect(f'/curso/{new_comentario.curso.id}')