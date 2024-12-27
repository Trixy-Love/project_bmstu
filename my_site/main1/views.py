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
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution",
                "problem2": "Water scarcity",
                "problem3": "Waste management",
                "problem4": "Smog and forest fires",
                "solution1": "Air purification",
                "solution2": "Ecology-friendly cars",
                "solution3": "Install water-saving devices",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Moscow":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Green spaces reduction",
                "problem2": "Noise pollution",
                "problem3": "Air pollution",
                "problem4": "Waste management issues",
                "solution1": "Plant more trees and flowers",
                "solution2": "Use soundproof materials",
                "solution3": "Use public transport",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Baghdad":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution ",
                "problem2": "Water scarcity",
                "problem3": "Inefficient waste disposal",
                "problem4": "Deforestation and land degradation",
                "solution1": "Encourage carpooling and biking ",
                "solution2": "Harvest rainwater for irrigation",
                "solution3": "Launch community clean-up events ",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Prague":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from traffic  ",
                "problem2": "Waste management issues ",
                "problem3": "Loss of biodiversity in urban areas",
                "problem4": "Increase waste separation efforts ",
                "solution1": "Promote public transport use ",
                "solution2": "Implement recycling programs",
                "solution3": "Create green roofs and walls",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Warsaw":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from industrial emissions",
                "problem2": "Urban heat island effect",
                "problem3": "Insufficient green spaces",
                "problem4": "Water scarcity",
                "solution1": "Enhance emission regulations",
                "solution2": "Increase tree planting initiatives",
                "solution3": "Develop more parks and gardens",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Vladivostok":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from vehicle emissions",
                "problem2": "Marine pollution from shipping activities",
                "problem3": "Deforestation and habitat loss",
                "problem4": "Encourage sustainable land use",
                "solution1": "Promote public transport usage",
                "solution2": "Implement strict waste disposal laws",
                "solution3": "Initiate reforestation projects",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Niamey":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Water scarcity and pollution",
                "problem2": "Urban waste management issues",
                "problem3": "Deforestation and land degradation",
                "problem4": "Loss of biodiversity in urban areas",
                "solution1": "Promote water conservation practices",
                "solution2": "Encourage sustainable land use",
                "solution3": "Improve waste recycling programs",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Shanghai":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from industrial emissions",
                "problem2": "Water pollution in rivers and lakes",
                "problem3": "Waste management challenges",
                "problem4": "Air pollution from traffic",
                "solution1": "Expand green public transport options",
                "solution2": "Implement stricter emission regulations",
                "solution3": "Increase recycling and waste separation efforts",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "London":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from traffic",
                "problem2": "Plastic waste accumulation",
                "problem3": "Urban heat island effect",
                "problem4": "Impact of climate change on wildlife",
                "solution1": "Promote electric public transport",
                "solution2": "Launch city-wide recycling campaigns",
                "solution3": "Create more green urban spaces",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Nuuk":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Melting ice and rising sea levels",
                "problem2": "Waste management in remote areas",
                "problem3": "Impact of climate change on wildlife",
                "problem4": "Implement recycling programs",
                "solution1": "Promote renewable energy sources",
                "solution2": "Improve waste collection systems",
                "solution3": "Support wildlife conservation efforts",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        context = {"infoC":city_infoC, "pop_up":True}
    return render(request, "main1/weather_conditions.html", context)
def climate_change_simulator(request):
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
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution",
                "problem2": "Water scarcity",
                "problem3": "Waste management",
                "problem4": "Smog and forest fires",
                "solution1": "Air purification",
                "solution2": "Ecology-friendly cars",
                "solution3": "Install water-saving devices",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Moscow":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Green spaces reduction",
                "problem2": "Noise pollution",
                "problem3": "Air pollution",
                "problem4": "Waste management issues",
                "solution1": "Plant more trees and flowers",
                "solution2": "Use soundproof materials",
                "solution3": "Use public transport",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Baghdad":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution ",
                "problem2": "Water scarcity",
                "problem3": "Inefficient waste disposal",
                "problem4": "Deforestation and land degradation",
                "solution1": "Encourage carpooling and biking ",
                "solution2": "Harvest rainwater for irrigation",
                "solution3": "Launch community clean-up events ",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Prague":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from traffic  ",
                "problem2": "Waste management issues ",
                "problem3": "Loss of biodiversity in urban areas",
                "problem4": "Increase waste separation efforts ",
                "solution1": "Promote public transport use ",
                "solution2": "Implement recycling programs",
                "solution3": "Create green roofs and walls",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Warsaw":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from industrial emissions",
                "problem2": "Urban heat island effect",
                "problem3": "Insufficient green spaces",
                "problem4": "Water scarcity",
                "solution1": "Enhance emission regulations",
                "solution2": "Increase tree planting initiatives",
                "solution3": "Develop more parks and gardens",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Vladivostok":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from vehicle emissions",
                "problem2": "Marine pollution from shipping activities",
                "problem3": "Deforestation and habitat loss",
                "problem4": "Encourage sustainable land use",
                "solution1": "Promote public transport usage",
                "solution2": "Implement strict waste disposal laws",
                "solution3": "Initiate reforestation projects",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Niamey":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Water scarcity and pollution",
                "problem2": "Urban waste management issues",
                "problem3": "Deforestation and land degradation",
                "problem4": "Loss of biodiversity in urban areas",
                "solution1": "Promote water conservation practices",
                "solution2": "Encourage sustainable land use",
                "solution3": "Improve waste recycling programs",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Shanghai":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from industrial emissions",
                "problem2": "Water pollution in rivers and lakes",
                "problem3": "Waste management challenges",
                "problem4": "Air pollution from traffic",
                "solution1": "Expand green public transport options",
                "solution2": "Implement stricter emission regulations",
                "solution3": "Increase recycling and waste separation efforts",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "London":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Air pollution from traffic",
                "problem2": "Plastic waste accumulation",
                "problem3": "Urban heat island effect",
                "problem4": "Impact of climate change on wildlife",
                "solution1": "Promote electric public transport",
                "solution2": "Launch city-wide recycling campaigns",
                "solution3": "Create more green urban spaces",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Nuuk":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Melting ice and rising sea levels",
                "problem2": "Waste management in remote areas",
                "problem3": "Impact of climate change on wildlife",
                "problem4": "Implement recycling programs",
                "solution1": "Promote renewable energy sources",
                "solution2": "Improve waste collection systems",
                "solution3": "Support wildlife conservation efforts",
                "feels_like": "Feels like: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        context = {"infoC":city_infoC, "pop_up":True}
    return render(request, "main1/climate_change_simulator.html", context)
def about(request):
    return render(request, "main1/about.html")
def what_to_wear(request):
    return render(request, "main1/what_to_wear.html")