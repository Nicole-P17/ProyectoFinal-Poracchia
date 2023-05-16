from django.shortcuts import render, redirect
from django.urls import reverse
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

def crear_consultante (request):
    if request.method == "POST":
        data = request.POST
        nombre = data ["nombre"]
        motivo = data["motivo"]
        telefono = data["telefono"]
        consultante = Consultante(nombre=nombre, 
                                  motivo=motivo, 
                                  telefono=telefono)
        consultante.save()

        url_exitosa = reverse("listar_consultantes")
        return redirect(url_exitosa)
    
    else:
        http_responde = render(
        request=request,
        template_name = 'AppTerapia/formularioConsultantes.html',
        )
        return http_responde

def crear_paciente (request):
    if request.method == "POST":
        data = request.POST
        nombre = data["nombre"]
        edad = data["edad"]
        telefono = data["telefono"]
        paciente = Paciente(nombre=nombre, 
                            edad=edad, 
                            telefono=telefono)
        paciente.save()

        url_exitosa = reverse("listar_pacientes")
        return redirect(url_exitosa)
    
    else:
        http_responde = render(
        request=request,
        template_name = 'AppTerapia/formularioPacientes.html',
        )
        return http_responde

def crear_psicologo (request):
    if request.method == "POST":
        data = request.POST
        nombre = data["nombre"]
        edad = data["edad"]
        precioSesion = data["precioSesion"]
        especializacion = data["especializacion"]
        matricula = data["matricula"]
        mail = data["mail"]
        terapeuta = Terapeuta(nombre=nombre, 
                              edad=edad, 
                              precioSesion=precioSesion, 
                              especializacion=especializacion, 
                              matricula=matricula, 
                              mail=mail)
        terapeuta.save()

        url_exitosa = reverse("listar_psicologos")
        return redirect(url_exitosa)
    
    else:
        http_responde = render(
        request=request,
        template_name = 'AppTerapia/formularioPsicologos.html',
        )
        return http_responde


def consultantes(request):
    return HttpResponse("Consultantes")

def pacientes(request):
    return HttpResponse("Pacientes")

def psicologos(request):
    return HttpResponse("Psicologos")




#usar el puerto 8888 para el comando python manage.py runserver 8888

