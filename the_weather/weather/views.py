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

def index(request):
    #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=75ac73f19ddafd686ee6e9ef942f3f18'
    #coordurl = ''
    url = 'http://api.openweathermap.org/data/2.5/forecast?lat={0}&lon={1}&units=imperial&appid=75ac73f19ddafd686ee6e9ef942f3f18'
    #city = 'Dallas'

    forecastlist = []

    address = request.GET.get('address', 'Default') #retrieves user input from search bar

    # if address is None:
    #     return redirect('')

    geolocator = Nominatim(user_agent="weather")

    location = geolocator.geocode(address) #use geolocator to get coordinates from address

    # print(location.latitude, location.longitude)

    city_weather = requests.get(url.format(location.latitude, location.longitude)).json() #requests info from API as json

    #print(city_weather)
    #print(city_weather["cod"])

    # print(city_weather.list[0].main.temp)

    # Retrieve the CSRF token first
    #csrf_client.get(URL)  # sets cookie
    #csrftoken = csrf_client.cookies['csrftoken']

    for item in city_weather["list"]:
        if(datetime.utcfromtimestamp(int(item["dt"])).strftime('%H:%M') == "00:00"):
            forecastlist.append(forecastdata(item["main"]["temp_max"], item["main"]["temp_min"], datetime.utcfromtimestamp(int(item["dt"])).strftime('%Y-%m-%d'), item["weather"][0]["icon"]))

    print(forecastlist)

    for data in forecastlist:
        print(data.date)

    # weather = {
    #     'city' : city,
    #     'temperature' : city_weather['main']['temp'],
    #     'description' : city_weather['weather'][0]['description'],
    #     'icon' : city_weather['weather'][0]['icon']
    # }

    context = {'forecastlist' : forecastlist, 'address' : address}

    return render(request, 'weather/index.html', context)#, context) #returns the index.html template



