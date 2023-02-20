from django.shortcuts import render
import requests
from geopy.geocoders import Nominatim
from datetime import datetime
from .forms import AddressForm

class forecastdata:
    def __init__(self, tempmax, tempmin, date, icon):
        self.tempmax = tempmax
        self.tempmin = tempmin
        self.date = date
        self.icon = icon

def get_address(request):
    address = request.GET.get('address', 'Default')
    return address

def get_coordinates(request):
    geolocator = Nominatim(user_agent="weather")

    location = geolocator.geocode(request) #use geolocator to get coordinates from address
    return location

def index(request):
    
    url = 'http://api.openweathermap.org/data/2.5/forecast?lat={0}&lon={1}&units=imperial&appid=75ac73f19ddafd686ee6e9ef942f3f18'
    
    forecastlist = []

    address = get_address(request)

    geolocator = Nominatim(user_agent="weather")

    location = get_coordinates(address) #use geolocator to get coordinates from address

    city_weather = requests.get(url.format(location.latitude, location.longitude)).json() #requests info from API as json

    # Retrieve the CSRF token first
    #csrf_client.get(URL)  # sets cookie
    #csrftoken = csrf_client.cookies['csrftoken']

    for item in city_weather["list"]:
        if(datetime.utcfromtimestamp(int(item["dt"])).strftime('%H:%M') == "00:00"):
            forecastlist.append(forecastdata(item["main"]["temp_max"], item["main"]["temp_min"], datetime.utcfromtimestamp(int(item["dt"])).strftime('%Y-%m-%d'), item["weather"][0]["icon"]))

    context = {'forecastlist' : forecastlist, 'address' : address}

    return render(request, 'weather/index.html', context)#, context) #returns the index.html template



