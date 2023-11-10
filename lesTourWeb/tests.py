from django.test import TestCase
from django.test import reverse
from lesTourWeb.views import hoteles, personal, usuarios, Home, SignUp, Reservation, SignIn

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

##test para el modelo Usuarios
