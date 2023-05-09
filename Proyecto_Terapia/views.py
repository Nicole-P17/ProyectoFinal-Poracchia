from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def saludo(request):
    return HttpResponse("Hola")

def pacientes(request):
    return HttpResponse("Pacientes")

def Minombre(self,nombre):
    documentosDeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentosDeTexto)

#usar el puerto 8888 para el comando python manage.py runserver 8888

def probandoTemplate(request):
    nom="Nicole"
    ap="Poracchia"

    contexto = {"nombre":nom, "apellido":ap}
    http_responde = render(
    request=request,
    template_name = 'AppTerapia/base.html',
    context=contexto,
    )
    return http_responde