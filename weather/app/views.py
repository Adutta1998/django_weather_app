from django.shortcuts import render,HttpResponse,redirect
from urllib import request
import json
from .models import WeatherData

# Create your views here.
def index(req):
    if req.GET.get('city'):
        d={}
        raw_data = request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={0}&APPID=fe2658af87ff250fe0a69fc5077a954a&units=metric'.format(req.GET.get('city')))
        data = json.load(raw_data)
        d["testdata"] = data
        print(d)
        return render(req,'app/weather.html',{"weather_data":data})
    else:
        cities = WeatherData.objects.all()
        data = []
        for city in cities:
            raw_data = request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={0}&APPID=fe2658af87ff250fe0a69fc5077a954a&units=metric'.format(city))
            data.append(json.load(raw_data))
        #print(data)
        return render(req,'app/weather.html',{'data':data})

def pin(request,city):
    data = WeatherData(city=city)
    data.save()
    return redirect(index)

def unpin(request,city):
    WeatherData.objects.get(city=city).delete()
    return redirect(index)