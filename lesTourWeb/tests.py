from django.test import TestCase
from django.test import reverse
from lesTourWeb.views import hoteles, personal, usuarios, Home, SignUp, Reservation, SignIn
from .models import Reserva

from django.test import TestCase
from django.urls import reverse

class PruebasDeURL(TestCase):
    def test_hoteles_url(self):
        response = self.client.get(reverse('hoteles'))
        self.assertEqual(response.status_code, 200)

    def test_personal_url(self):
        response = self.client.get(reverse('personal'))
        self.assertEqual(response.status_code, 200)

    def test_usuarios_url(self):
        response = self.client.get(reverse('usuarios'))
        self.assertEqual(response.status_code, 200)

    def test_home_url(self):
        response = self.client.get(reverse('Home'))
        self.assertEqual(response.status_code, 200)

    def test_signup_url(self):
        response = self.client.get(reverse('SingUp'))
        self.assertEqual(response.status_code, 200)

    def test_signin_url(self):
        response = self.client.get(reverse('SingIn'))
        self.assertEqual(response.status_code, 200)

    def test_reservation_url(self):
        response = self.client.get(reverse('Reservation'))
        self.assertEqual(response.status_code, 200)

##test para el modelo Reserva
class ReservaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración de datos de prueba que no cambiarán durante todas las pruebas
        user = User.objects.create_user(username='testuser', password='testpass')
        Reserva.objects.create(
            id_user=user,
            checkin_datetime='2023-01-01 12:00:00',
            checkout_datetime='2023-01-02 12:00:00',
            total_cost=100,
            id_room=1,
            observation='Esta es una observación de prueba.'
        )
    def test_checkin_datetime(self):
        reserva = Reserva.objects.get(id=1)
        self.assertEqual(str(reserva.checkin_datetime), '2023-01-01 12:00:00')
