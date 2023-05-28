from django.contrib import admin
from django.urls import path, include
from AppTerapia import views


from AppTerapia.views import listar_consultantes, listar_pacientes, listar_psicologos, pacientes
from AppTerapia.views import crear_consultante, crear_paciente, crear_psicologo, buscar_paciente
from AppTerapia.views import eliminar_paciente, editar_paciente

urlpatterns = [
    path("lista-consultantes/", views.listar_consultantes, name="listar_consultantes"),
    path("lista-pacientes/", views.listar_pacientes, name="listar_pacientes"),
    path("lista-psicologos/", views.listar_psicologos, name="listar_psicologos"),

    path("crear-consultante/", crear_consultante, name="crear_consultante"),
    path("crear-paciente/", crear_paciente, name="crear_paciente"),
    path("crear-psicologo/", crear_psicologo, name="crear_psicologo"),

    path("buscar-paciente/", buscar_paciente, name="buscar_paciente"),
    path("eliminar-paciente/<int:id>/", eliminar_paciente, name="eliminar_paciente"),
    path("editar-paciente/<int:id>/", editar_paciente, name="editar_paciente"),

]