from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import CityForm
import random

# Mock weather database
MOCK_WEATHER = {
    "mathura": {"cordinate":"77.69.27.5","temp": "302.319k", "pressure": 1002.81, "humidity": 65},
    "texas": {"cordinate":"34.2000.85.9","temp": "305.39k", "pressure": 900.81, "humidity": 45},
    "new york": {"cordinate":"246.200.39.4","temp": "275.98k", "pressure": 955.8, "humidity": 75},
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
