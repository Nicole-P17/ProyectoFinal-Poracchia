from ctypes.wintypes import PSIZE
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from AppTerapia.forms import PsicologoFormulario, PacienteFormulario
from django.http import HttpResponse 
from AppTerapia.models import Paciente, Terapeuta, Consultante
# Create your views here.

def listar_consultantes (LoginRequiredMixin, request,):
    contexto = {
        "consultantes": Consultante.objects.all()

    }
    http_response = render(
    request=request,
    template_name = 'AppTerapia/listaConsultantes.html',
    context=contexto,
    )
    return http_response

def listar_pacientes (request, ):
    contexto = {
        "pacientes": Paciente.objects.all()
    }
    http_response = render(
    request=request,
    template_name = 'AppTerapia/listaPacientes.html',
    context=contexto,
    )
    return http_response

def listar_psicologos (request, ):
    contexto = {
        "psicologos": Terapeuta.objects.all()
    }
    http_response = render(
        request=request,
        template_name = 'AppTerapia/listaPsicologos.html',
        context=contexto,
    )
    return http_response

def crear_consultante (request, ):
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
        http_response = render(
            request=request,
            template_name = 'AppTerapia/formularioConsultantes.html',
        )
        return http_response

def crear_paciente (request, ):
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
        http_response = render(
            request=request,
            template_name = 'AppTerapia/formularioPacientes.html',
        )
        return http_response

def buscar_paciente(request, ):
    formulario = PacienteFormulario()

    if request.method == "POST":
        formulario = PacienteFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            edad = data['edad']
            telefono = data['telefono']

            paciente = Paciente(
                nombre = nombre,
                edad = edad,
                telefono = telefono,
            )
            paciente.save()

            url_exitosa = reverse('listar_pacientes')
            return redirect(url_exitosa)
        
    http_response = render (
        request=request,
        template_name='AppTerapia/formularioPacientes.html',
        context={'formulario': formulario},
    )
    return http_response
        

def eliminar_paciente(request, id, ):
    paciente = Paciente.objects.get(id=id)
    if request.method == "POST":
        paciente.delete()
        url_exitosa = reverse('listar_pacientes')
        return redirect(url_exitosa)


def editar_paciente(request, id, ):
    paciente = Paciente.objects.get(id=id)
    if request.method == "POST":
        formulario = PacienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            paciente.nombre = data['nombre']
            paciente.edad = data["edad"]
            paciente.telefono = data['telefono']
            paciente.save()

            url_exitosa = reverse('listar_pacientes')
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'nombre': paciente.nombre,
            'edad': paciente.edad,
            'telefono': paciente.telefono,
        }
        formulario = PacienteFormulario(initial=inicial)
    return render(
        request=request,
        template_name='AppTerapia/formularioPacientes.html',
        context={'formulario': formulario},
    )



def crear_psicologo(request, ):
    formulario = PsicologoFormulario()

    if request.method == "POST":
        formulario = PsicologoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data["nombre"]
            edad = data["edad"]
            precioSesion = data["precioSesion"]
            especializacion = data["especializacion"]
            matricula = data["matricula"]
            telefono = data["telefono"]
            mail = data["mail"]

            psicologo = Terapeuta(
                nombre=nombre, 
                edad=edad, 
                precioSesion=precioSesion, 
                especializacion=especializacion,
                matricula=matricula,
                telefono=telefono,
                mail=mail
            )
            psicologo.save()

            url_exitosa = reverse('listar_psicologos')
            return redirect(url_exitosa)

    http_response = render(
        request=request,
        template_name='AppTerapia/formularioPsicologos.html',
        context={'formulario': formulario},
    )
    return http_response


def consultantes(request):
    return HttpResponse("Consultantes")

def pacientes(request):
    return HttpResponse("Pacientes")

def psicologos(request):
    return HttpResponse("Psicologos")




#usar el puerto 8888 para el comando python manage.py runserver 8888

