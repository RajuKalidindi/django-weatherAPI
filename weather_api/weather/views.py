from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .dummy_data import get_dummy_weather_data

# Get current weather data for a specific city
@api_view(['GET'])
def current_weather(request, city):
    try:
        city = city.lower()
        weather_data = get_dummy_weather_data()
        if city in weather_data:
            current_data = weather_data[city]['current']
            return Response(current_data, status=status.HTTP_200_OK)
        return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(
            {"error": f"An error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Get 5-day weather forecast for a specific city
@api_view(['GET'])
def weather_forecast(request, city):
    try:
        city = city.lower()
        weather_data = get_dummy_weather_data()
        if city in weather_data:
            forecast_data = weather_data[city]["forecast"]
            return Response(forecast_data, status=status.HTTP_200_OK)
        return Response({"error": "City not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(
            {"error": f"An error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )