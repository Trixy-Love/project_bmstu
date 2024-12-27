import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm
from .forms import City1Form
from django.shortcuts import redirect
from django.http import HttpResponse
def index(request):
    appid = "64b27a9ca653a9ab3855bc2801d2edaf"
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    for city in cities:
        q = True
    res = requests.get(url.format(city.name)).json()
    if res.get("main"):
        city_info = {
            "city": city.name,
            "temp": str(round(float(res["main"]["temp"])))+"°",
            "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°",
            "icon": res["weather"][0]["icon"],
            "error": False
        }
    else:
        city_info={
            "city": city.name,
            "error":True
        }
    context = {"info":city_info, "form": form}
    City.objects.all().delete()
    values_for_update={"name":city,}
    bob, created = City.objects.update_or_create(id=2, defaults = values_for_update)  
    return render(request, "main1/index.html", context)
def user_settings(request):
    appid = "64b27a9ca653a9ab3855bc2801d2edaf"
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    if(request.method == "POST"):
        form = CityForm(request.POST)
        form.save()
    form = CityForm()
    cities = City.objects.all()
    for city in cities:
        q = True
    res = requests.get(url.format(city.name)).json()
    if res.get("main"):
        city_info = {
            "city": city.name,
            "temp": res["main"]["temp"],
            "icon": res["weather"][0]["icon"],
            "error": False
        }
    else:
        city_info={
            "city": city.name,
            "error":True
        }
    
    context = {"info":city_info, "form": form}
    City.objects.all().delete()
    return render(request, "main1/user_settings.html", context)

def weather_conditions(request):
    context={"pop_up":False}
    if request.method == 'POST':
        
        city_name = request.POST.get('city_name')
        print(city_name)
        appid = "64b27a9ca653a9ab3855bc2801d2edaf"
        url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
            
        
        res = requests.get(url.format(city_name)).json()
        if city_name == "Los Angeles":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": "California, USA",
                "problem1": "Floods",
                "problem2": "Heat waves",
                "problem3": "Forest fires",
                "problem4": "Smog",
                "solution1": "Air purification",
                "solution2": "Ecology-friendly cars",
                "solution3": "New green zones",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°",
                }
        if city_name == "Los Angeles":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": "California, USA",
                "problem1": "Floods",
                "problem2": "Heat waves",
                "problem3": "Forest fires",
                "problem4": "Smog",
                "solution1": "Air purification",
                "solution2": "Ecology-friendly cars",
                "solution3": "New green zones",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°",
                }
        context = {"infoC":city_infoC, "pop_up":True}
    return render(request, "main1/weather_conditions.html", context)
def climate_change_simulator(request):
    appid = "64b27a9ca653a9ab3855bc2801d2edaf"
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=" + appid
    
    form = City1Form()
    cities = City.objects.all()
    for city1 in cities:
        q = True
    res = requests.get(url.format(city1.name)).json()
    city_info = {
        "city": city1.name,
        "temp": res["main"]["temp"],
        "icon": res["weather"][0]["icon"],
        }
    context = {"info":city_info, "form": form}
    return render(request, "main1/climate_change_simulator.html", context)
def about(request):
    return render(request, "main1/about.html")
def what_to_wear(request):
    return render(request, "main1/what_to_wear.html")