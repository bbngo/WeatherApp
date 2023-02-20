from django.test import SimpleTestCase
from django.urls import reverse, resolve
from weather.views import get_address, get_coordinates, forecastdata

class TestViews(SimpleTestCase):
    
    def test_index_url(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_address)
        # self.assertEquals(resolve(url).func, get_coordinates)
        # self.assertEquals(resolve(url).func, forecastdata)