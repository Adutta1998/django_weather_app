from django.shortcuts import render,HttpResponse
from urllib import request
import json

# Create your views here.
def index(req):
    if req.GET.get('city'):
        raw_data = request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={0}&APPID=fe2658af87ff250fe0a69fc5077a954a&units=metric'.format(req.GET.get('city')))
        data = json.load(raw_data)
        return render(req,'app/weather.html',{"weather_data":data})
    else:
        return render(req,'app/weather.html')
