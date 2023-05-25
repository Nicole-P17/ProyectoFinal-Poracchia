from django import forms
from AppTerapia.models import Terapeuta, Paciente

class PacienteFormulario(forms.Form):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'telefono']


class PsicologoFormulario(forms.ModelForm):
    class Meta:
        model = Terapeuta
        fields = ['nombre', 'edad', 'precioSesion', 'especializacion', 'matricula', 'telefono', 'mail']

class ConsultanteFormulario(forms.Form):
    nombre=forms.CharField(required=True, max_length=40)
    motivo = forms.CharField(required=True, max_length=100)
    telefono = forms.IntegerField(required=True, )