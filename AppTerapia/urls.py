from django.urls import path
from AppTerapia import views

from AppTerapia.views import saludo, pacientes, Minombre
from AppTerapia.views import listar_consultantes, listar_pacientes, listar_psicologos, probandoTemplate

urlpatterns = [
    path('saludo/', views.saludo, name="saludo"),
    path('pacientes/', views.pacientes ,name="pacientes"),
    path('Minombre/<nombre>', views.Minombre, name="Minombre"),
    path("VerHtml/", views.probandoTemplate, name="probandoTemplate"),
    path("lista-consultantes", views.listar_consultantes, name="listar_consultantes"),
    path("lista-pacientes", views.listar_pacientes, name="listar_pacientes"),
    path("lista-psicologos", views.listar_psicologos, name="listar_psicologos"),
]
