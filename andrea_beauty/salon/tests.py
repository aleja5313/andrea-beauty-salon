from django.test import TestCase
from django.urls import reverse
from .models import Cliente, Servicio, Cita
from .forms import ClienteForm, ServicioForm

class ClienteModelTest(TestCase):

    def test_creacion_cliente(self):

        cliente = Cliente.objects.create(

            nombre='Andrea',

            telefono='3001234567',

            email='andrea@gmail.com'
        )

        self.assertEqual(
            cliente.nombre,
            'Andrea'
        )

class ServicioModelTest(TestCase):

    def test_creacion_servicio(self):

        servicio = Servicio.objects.create(

            nombre='Corte',

            descripcion='Corte profesional',

            precio=50000,

            duracion=60
        )

        self.assertEqual(
            servicio.precio,
            50000
        )

class ClienteFormTest(TestCase):

    def test_telefono_invalido(self):

        form = ClienteForm(data={

            'nombre': 'Andrea',

            'telefono': 'abc123',

            'email': 'andrea@gmail.com'
        })

        self.assertFalse(form.is_valid())

class ServicioFormTest(TestCase):

    def test_precio_negativo(self):

        form = ServicioForm(data={

            'nombre': 'Corte',

            'descripcion': 'Servicio',

            'precio': -100,

            'duracion': 30
        })

        self.assertFalse(form.is_valid())

class DashboardViewTest(TestCase):

    def test_dashboard_response(self):

        response = self.client.get(
            reverse('salon:dashboard')
        )

        self.assertEqual(
            response.status_code,
            200
        )

class ClientesViewTest(TestCase):

    def test_clientes_response(self):

        response = self.client.get(
            reverse('salon:clientes')
        )

        self.assertEqual(
            response.status_code,
            200
        )