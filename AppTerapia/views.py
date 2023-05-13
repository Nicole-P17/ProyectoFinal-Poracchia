from django.shortcuts import render, redirect
from django.http import HttpResponse 
# Create your views here.

def listar_consultantes (request):
    contexto = {
        "consultantes": [
            {"nombre":"martin", "apellido":"navarro"},
            {"nombre":"valentina", "apellido":"sousa"},
            {"nombre":"maria", "apellido":"cifuentes"},
            {"nombre":"matias", "apellido":"figueroa"},
        ]
    }
    http_responde = render(
    request=request,
    template_name = 'AppTerapia/listaConsultantes.html',
    context=contexto,
    )
    return http_responde

def listar_pacientes (request):
    contexto = {
        "pacientes": [
            {"nombre":"pablo", "apellido":"lopez"},
            {"nombre":"julian", "apellido":"sanchez"},
            {"nombre":"florencia", "apellido":"rojas"},
            {"nombre":"sofia", "apellido":"martinez"},
        ]
    }
    http_responde = render(
    request=request,
    template_name = 'AppTerapia/listaPacientes.html',
    context=contexto,
    )
    return http_responde

def listar_psicologos (request):
    contexto = {
        "psicologos": [
            {"nombre":"rosa", "apellido":"gonzalez"},
            {"nombre":"mora", "apellido":"gomez"},
            {"nombre":"bautista", "apellido":"diaz"},
            {"nombre":"gonzalo", "apellido":"fernandez"},
        ]
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

