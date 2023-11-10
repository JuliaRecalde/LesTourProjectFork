from django.test import TestCase
from django.test import reverse
from lesTourWeb.views import hoteles, personal, usuarios

class PruebasDeURL(TestCase):
    def Unit_Test1(self):
        response = self.client.get(reverse('hoteles'))
        self.assertEqual(response.status_code, 200)
        
    def Unit_Test2(self):
        response = self.client.get(reverse('personal'))
        self.assertEqual(response.status_code, 200)
        
    def Unit_Test3(self):
            response = self.client.get(reverse('usuarios'))
            self.assertEqual(response.status_code, 200)