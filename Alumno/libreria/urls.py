from django.urls import path
from . import views



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('estudiante', views.estudiantes, name='estudiante'),
    path('cursos', views.cursos, name='curso'),
    path('estudiante/crear', views.crear, name='crear'),
    path('estudiante/crearCurso', views.crearCurso, name='crearCurso'),
    path('estudiante/crearCurso2', views.crearCurso2, name='crearCurso2'),
    path('estudiante/editar', views.editar, name='editar'),
    path('estudiante/editarCurso/<int:id>', views.editarCurso, name='editarCurso'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('eliminarCurso/<int:id>', views.eliminarCurso, name='eliminarCurso'),
    path('estudiante/editar/<int:id>', views.editar, name='editar'),

]


