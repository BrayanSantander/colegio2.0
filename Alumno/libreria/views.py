from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import AlumnoForm
from .forms import CursoForm


def inicio(request):
    return render(request, "paginas/inicio.html")
def nosotros(request):
    return render(request, "paginas/nosotros.html")


def estudiantes(request):
    estudiantes = alumno.objects.all()
    return render(request, "estudiante/index.html", {"estudiantes":estudiantes})


def cursos(request):
    cursos = curso.objects.all()
    return render(request, "estudiante/crearCurso.html", {"cursos": cursos})

def crear(request):
    formulario = AlumnoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("estudiante")
    return render (request, "estudiante/crear.html", {"formulario":formulario})

def crearCurso(request):
    formulario = CursoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("crearCurso")
    return render (request, "estudiante/crearCurso.html", {"formulario":formulario})

def crearCurso2(request):
    formulario = CursoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("estudiante")
    return render (request, "estudiante/crearCurso2.html", {"formulario":formulario})


def editar(request,id):
    estudiantes = alumno.objects.get(id=id)
    formulario = AlumnoForm(request.POST or None, request.FILES or None, instance=estudiantes)
    if formulario.is_valid()and request.POST:
        formulario.save()
        return redirect("estudiante")
    return render (request, "estudiante/editar.html", {"formulario":formulario})

def editarCurso(request,id):
    cursos = curso.objects.get(id=id)
    formulario = CursoForm(request.POST or None, request.FILES or None, instance=cursos)
    if formulario.is_valid()and request.POST:
        formulario.save()
        return redirect("curso")
    return render (request, "estudiante/editarCurso.html", {"formulario":formulario})


def eliminar(request,id):
    estudiantes = alumno.objects.get(id=id)
    estudiantes.delete()
    return redirect("estudiante")


def eliminarCurso(request,id):
    cursos = curso.objects.get(id=id)
    cursos.delete()
    return redirect("curso")