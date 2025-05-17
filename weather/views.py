from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import CityForm
import random

# Mock weather database
MOCK_WEATHER = {
    "dhaka": {"temperature": 33, "description": "Hot and humid", "icon": "☀️"},
    "chattogram": {"temperature": 30, "description": "Partly cloudy", "icon": "⛅"},
    "sylhet": {"temperature": 28, "description": "Rainy", "icon": "🌧️"},
    "rajshahi": {"temperature": 35, "description": "Very hot", "icon": "🔥"},
}

def index(request):
    weather_data = {}
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city'].lower()
            weather_data = MOCK_WEATHER.get(city, {
                "temperature": random.randint(20, 36),
                "description": "Unknown city — showing random weather.",
                "icon": "❓"
            })
            weather_data['city'] = city.title()
    else:
        form = CityForm()
    return render(request, 'weather/index.html', {'form': form, 'weather_data': weather_data})
