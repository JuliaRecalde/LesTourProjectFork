from django.test import TestCase
from .models import Hoteles

#Test para modelos

class HotelesModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configuración de datos de prueba que no cambiarán durante todas las pruebas
        Hoteles.objects.create(
            nombre='Hotel Savoy',
            ciudad='Ciudad Encarnacion',
            barrio='Barrio Centro',
            direccion='Avenida Costanera',
            telefono=0994763030,
            email='info@hotelsavoy.com',
            pisos=5,
            habitaciones=100
        )

    def test_hotel(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(hotel.nombre, 'Hotel Ejemplo')

    def test_ciudad(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(hotel.ciudad, 'Ciudad Encarnacion')

    def test_barrio(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(hotel.barrio, 'Barrio Centro')

    def test_direccion(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(hotel.direccion, 'Avenida Costanera')

    def test_telefono(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(hotel.telefono, 0994763030)

    def test_email(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(hotel.email, 'info@hotelsavoy.com')

    def test_pisos(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(hotel.pisos, 5)

    def test_habitaciones(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(hotel.habitaciones, 100)

    def test_str_method(self):
        hotel = Hoteles.objects.get(id=1)
        self.assertEqual(str(hotel), 'Hotel Savoy')

