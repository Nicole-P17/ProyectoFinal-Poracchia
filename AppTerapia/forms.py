from django import forms
from AppTerapia.models import Terapeuta

class PacienteFormulario(forms.Form):
    nombre= forms.CharField(required=True, max_length=40)
    edad = forms.IntegerField(required=True,)
    telefono = forms.IntegerField(required=True,)

class PsicologoFormulario(forms.ModelForm):
    class Meta:
        model = Terapeuta
        fields = ['nombre', 'edad', 'precioSesion', 'especializacion', 'matricula', 'telefono', 'mail']

class ConsultanteFormulario(forms.Form):
    nombre=forms.CharField(required=True, max_length=40)
    motivo = forms.CharField(required=True, max_length=100)
    telefono = forms.IntegerField(required=True, )