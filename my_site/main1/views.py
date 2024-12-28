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
            "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°",
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
            "temp": str(round(float(res["main"]["temp"])))+"°C",
            "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
            "icon": res["weather"][0]["icon"],
            "error": False,
            "wind":str(res["wind"]["speed"]) + "m/s",
            "degree": str(res["wind"]["deg"]) + "°",
            "pressure":str(res["main"]["pressure"]) + "mm Hg",
            "humidity":str(res["main"]["humidity"])+"%",
            "descriprion":str(res["weather"][0]["description"]),
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
                "problem1": "Загрязнение воздуха",
                "problem2": "Нехватка воды",
                "problem3": "Утилизация отходов",
                "problem4": "Смог и лесные пожары",
                "solution1": "Очистка воздуха",
                "solution2": "Электрические автомобили",
                "solution3": "Установка водосберегающих устройств",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Moscow":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Сокращение зелёных зон",
                "problem2": "Шумовое загрязнение",
                "problem3": "Загрязнение воздуха",
                "problem4": "Вопросы утилизации отходов",
                "solution1": "Сажайте больше деревьев и цветов",
                "solution2": "Используйте звуконепроницаемые материалы",
                "solution3": "Пользуйтесь общественным транспортом",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Baghdad":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Загрязнение воздуха",
                "problem2": "Нехватка воды",
                "problem3": "Неэффективная утилизация отходов",
                "problem4": "Обезлесение и деградация земель",
                "solution1": "Поощряйте использование велосипедов",
                "solution2": "Собирайте дождевую воду для орошения",
                "solution3": "Запуск общественных субботников",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Prague":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Загрязнение воздуха выхлопами",
                "problem2": "Вопросы обращения с отходами",
                "problem3": "Утрата биоразнообразия",
                "problem4": "Увеличить усилия по разделению отходов",
                "solution1": "Использование общественного транспорта",
                "solution2": "Внедрять программы утилизации отходов",
                "solution3": "Создавайте зеленые крыши и стены",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Warsaw":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Загрязнение воздуха выбросами фабрик",
                "problem2": "Эффект городского теплового острова",
                "problem3": "Нехватка зеленых зон",
                "problem4": "Нехватка воды",
                "solution1": "Усилить регулирование выбросов",
                "solution2": "Активизировать инициативы по посадке деревьев",
                "solution3": "Создавайте больше парков и скверов",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Vladivostok":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Загрязнение воздуха выхлопами",
                "problem2": "Загрязнение морской среды",
                "problem3": "Обезлесение, утрата среды обитания",
                "problem4": "Поощрять сортировку отходов",
                "solution1": "Использование общественного транспорта",
                "solution2": "Соблюдать законы утилизации отходов",
                "solution3": "Восстановление лесов",
                "feels_like": "Ощущается как:" + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Niamey":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Нехватка воды",
                "problem2": "Утилизация городских отходов",
                "problem3": "Обезлесение и деградация земель",
                "problem4": "Утрата биоразнообразия",
                "solution1": "Пропагандировать сохранение водных ресурсов",
                "solution2": "Поощрять устойчивое землепользование",
                "solution3": "Совершенствование программ утилизации отходов",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Shanghai":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Загрязнение воздуха выбросами",
                "problem2": "Загрязнение воды в реках и озерах",
                "problem3": "Проблемы управления отходами",
                "problem4": "Загрязнение воздуха трафиком",
                "solution1": "Экологически-чистый общественный транспорт",
                "solution2": "Внедрить более строгие правила в отношении выбросов",
                "solution3": "Увеличьте усилия по переработке и разделению отходов",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "London":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Загрязнение воздуха выхлопами",
                "problem2": "Накопление пластиковых отходов",
                "problem3": "Эффект городского теплового острова",
                "problem4": "Воздействие человека на природу",
                "solution1": "Продвигать общественный транспорт",
                "solution2": "Запуск общегородских кампаний по переработке отходов",
                "solution3": "Создавайте больше зеленых городских пространств",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        if city_name == "Nuuk":
            city_infoC = {
                "cityC": city_name,
                "tempC": str(res["main"]["temp"]) + "°C",
                "iconC": res["weather"][0]["icon"],
                "countryC": res["sys"]["country"],
                "problem1": "Таяние льдов",
                "problem2": "Утилизация отходов",
                "problem3": "Воздействие человека на природу",
                "problem4": "Внедрять программы утилизации отходов",
                "solution1": "Использование возобновляемых источников энергии",
                "solution2": "Совершенствование систем сбора отходов",
                "solution3": "Поддерживать усилия по сохранению дикой природы",
                "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°C",
                }
        context = {"infoC":city_infoC, "pop_up":True}
    return render(request, "main1/climate_change_simulator.html", context)
def about(request):
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
            "feels_like": "Ощущается как: " + str(round(res["main"]["feels_like"])) + "°",
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
    return render(request, "main1/about.html", context)
def what_to_wear(request):
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
            "feels_like": "Ощущается как:" + str(round(res["main"]["feels_like"])) + "°",
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
    return render(request, "main1/what_to_wear.html", context)