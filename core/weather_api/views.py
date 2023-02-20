from django.shortcuts import render
from requests import get
from datetime import datetime

def weather_api(city):
    api_key = '55fd39fdac93f85b83d7441bc2158375'
    api_src = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    res = get(api_src).json()
    # data accessing
    weather_data = {}
    area = res.get('name')
    weather_data['area'] = area
    weather = res.get('weather')[0].get('main')
    weather_data['weather'] = weather
    temperature = res.get('main').get('temp')
    weather_data['temperature'] = temperature
    sunrise = res.get('sys').get('sunrise')
    sunrise_time = datetime.utcfromtimestamp(sunrise).strftime('%I:%M:%S %p')
    weather_data['sunrise_time'] = sunrise_time
    sunset = res.get('sys').get('sunset')
    sunset_time = datetime.utcfromtimestamp(sunset).strftime('%I:%M:%S %p')
    weather_data['sunset_time'] = sunset_time
    return weather_data

def open_weather(request):
    if request.method == "GET" and 'city' in request.GET:
        user_input_data = request.GET.get('city')
        weather_data = weather_api(user_input_data)
        contex = {'weather_data': weather_data}
    else:
        contex = {}
    return render(request, 'weather.html', contex)
