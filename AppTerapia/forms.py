from django import forms

class PacienteFormulario(forms.Form):
    nombre= forms.CharField(required=True, max_length=40)
    edad = forms.IntegerField(required=True,)
    telefono = forms.IntegerField(required=True,)

class PsicologoFormulario(forms.Form):
    nombre= forms.CharField(required=True, max_length=40)
    edad = forms.IntegerField(required=True,)
    precioSesion = forms.IntegerField(required=True, )
    especializacion= forms.CharField(required=True, max_length=100)
    matricula = forms.IntegerField(required=True, )
    mail = forms.EmailField(required=True, )

class ConsultanteFormulario(forms.Form):
    nombre=forms.CharField(required=True, max_length=40)
    motivo = forms.CharField(required=True, max_length=100)
    telefono = forms.IntegerField(required=True, )