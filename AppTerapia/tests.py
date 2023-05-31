from django.test import TestCase

from django.db import IntegrityError
from AppTerapia.models import Paciente


class PacienteTests(TestCase):
    """En esta clase van todas las pruebas del modelo Paciente."""

    def test_creacion_paciente(self):
        # caso uso esperado
        paciente = Paciente(nombre="Nombre:", )
        paciente.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Paciente.objects.count(), 1)
        self.assertEqual(Paciente.nombre, "Nombre")
        self.assertEqual(Paciente.edad, 18)

    def test_paciente_str(self):
        paciente = Paciente(nombre="Julian", edad=18)
        paciente.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(paciente.__str__(), "Julian | 18") 