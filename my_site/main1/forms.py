from .models import City
from django.forms import ModelForm, TextInput
from .models import City1
from django import forms

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["name"]
        widjets = {"name": TextInput(attrs={
            "class":"form-control",
            "name": "city",
            "id":"city",
            "placeholder":"Введите город"
        })}
class City1Form(ModelForm):
    class Meta:
        model = City1
        fields = ["name"]
        widjets = {"name": TextInput(attrs={
            "class":"form-control",
            "name": "city",
            "id":"city",
            "placeholder":"Введите город"
        })}
