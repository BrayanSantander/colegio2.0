from django import forms
from .models import *


class AlumnoForm(forms.ModelForm):
    class Meta:
        model=alumno
        fields ='__all__'
        
class CursoForm(forms.ModelForm):
    class Meta:
        model=curso
        fields ='__all__'