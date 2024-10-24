from django.urls import path
from .views import current_weather, weather_forecast

urlpatterns = [
    path('api/weather/current/<str:city>/', current_weather),
    path('api/weather/forecast/<str:city>/', weather_forecast),
]