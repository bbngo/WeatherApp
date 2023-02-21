from django.test import SimpleTestCase
from django.urls import reverse, resolve
from weather.views import get_address, get_coordinates, forecastdata

class ViewsTest(SimpleTestCase):
    
    def test_index_url(self):
        response = self.client.get('', follow=True)
        self.assertRedirects(response, '/login/')
        response = self.client.post('', follow=True)
        self.assertRedirects(response, '/login/')