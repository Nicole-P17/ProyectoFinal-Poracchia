from django.shortcuts import render, redirect
from django.http import HttpResponse 
from AppTerapia.models import Paciente, Terapeuta, Consultante
# Create your views here.

def listar_consultantes (request):
    contexto = {
        "consultantes": Consultante.objects.all()

    }
    http_responde = render(
    request=request,
    template_name = 'AppTerapia/listaConsultantes.html',
    context=contexto,
    )
    return http_responde

def listar_pacientes (request):
    contexto = {
        "pacientes": Paciente.objects.all()
    }
    http_responde = render(
    request=request,
    template_name = 'AppTerapia/listaPacientes.html',
    context=contexto,
    )
    return http_responde

def listar_psicologos (request):
    contexto = {
        "psicologos": Terapeuta.objects.all()
    }
    http_responde = render(
    request=request,
    template_name = 'AppTerapia/listaPsicologos.html',
    context=contexto,
    )
    return http_responde



def consultantes(request):
    return HttpResponse("Consultantes")

def pacientes(request):
    return HttpResponse("Pacientes")

def psicologos(request):
    return HttpResponse("Psicologos")




#usar el puerto 8888 para el comando python manage.py runserver 8888

