from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('curso/<int:id_curso>', views.ver_curso, name='ver_curso'),	  
    path('curso/nuevo',views.nuevo_curso, name='nuevo_curso'),	#para visualizar el detalle del curso y sus comentarios 
    path('curso/<int:id_curso>/editar', views.editar_curso, name='editar_curso'),
    path('curso/<int:id_curso>/eliminar', views.eliminar_curso, name='eliminar_curso'),
    path('curso/<int:id_curso>/nuevo_comentario', views.nuevo_comentario, name='nuevo_comentario'),
    
]
