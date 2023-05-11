from django.urls import path
from AppTerapia import views

from AppTerapia.views import saludo, pacientes, Minombre
from AppTerapia.views import listar_consultantes, listar_pacientes, listar_psicologos, probandoTemplate

urlpatterns = [
    path('saludo/', saludo),
    path('pacientes/', pacientes),
    path('Minombre/<nombre>', Minombre),
    path("VerHtml/", probandoTemplate),
    path("lista-consultantes", listar_consultantes),
    path("lista-pacientes", listar_pacientes),
    path("lista-psicologos", listar_psicologos),
]
