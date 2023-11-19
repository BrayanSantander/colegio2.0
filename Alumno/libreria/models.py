from django.db import models


class curso(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=True,verbose_name="nombre")
    seccion=models.CharField(max_length=100,null=True,verbose_name="seccion")
    sala = models.CharField(max_length=100,null=True, verbose_name="sala")
    cantidadEvaluaciones = models.IntegerField(verbose_name="cantidadEvaluacion",null=True)
    cantidadHoras = models.IntegerField(verbose_name="cantidadHoras",null=True)
    horario = models.CharField(max_length=100,null=True,verbose_name="horario")
    
class alumno(models.Model):
    id=models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12,null=True)
    nombre = models.CharField(max_length=100,null=True,verbose_name="nombre")
    edad = models.IntegerField(null=True,verbose_name="edad")
    asignaturas = models.CharField(max_length=100,null=True,verbose_name="asignaturas")
    celular = models.IntegerField(verbose_name="celular")
    apoderado= models.CharField(max_length=100,null=True,verbose_name="apoderado")
    curso = models.ForeignKey(curso, null=True, blank=True, on_delete= models.CASCADE)
    

