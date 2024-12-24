from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path('user_settings', views.user_settings ),
    path('weather_conditions', views.weather_conditions ),
    path('climate_change_simulator', views.climate_change_simulator ),
    path('about', views.about ),
    path('what_to_wear', views.what_to_wear ),
]
