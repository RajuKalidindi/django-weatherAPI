# Django-WeatherAPI

A REST Weather API built using django and djangorestframework

## API Endpoint Overview

This API provides weather data for specific cities. It includes two main endpoints:

1.  Current Weather Data Endpoint:

        /api/weather/current/<city>/

    Method: GET
    Description: This endpoint retrieves the current weather data for a specified city. The response includes temperature, humidity, and wind speed.
    
    Parameters:
    
     - city (string): The name of the city for which you want to retrieve the current weather data. (Only three cities are supported: hyderabad, mumbai, delhi)

2.  5-Day Weather Forecast Endpoint:
   
        /api/weather/forecast/<city>/
    
    Method: GET
    Description: This endpoint provides a 5-day weather forecast for a specified city. The response includes daily weather data such as temperature and humidity.

    Parameters:
    
    - city (string): The name of the city for which you want to retrieve the weather forecast. (Only three cities are supported: hyderabad, mumbai, delhi)

Response Codes for the endpoints:

    200 OK: Successful retrieval of forecast data.
    404 Not Found: If the city is not supported or does not exist.

## Prerequisites

Before you begin, ensure you have the following installed:

-   **Python**: Download and install python from (https://www.python.org/downloads/)

## Installation Instructions

Follow these steps to set up and run the application locally:

1.  **Fork and Clone the Repository**

    First, fork the repository on GitHub, then clone it to your local machine using:

    ```bash
    git clone {repository-url}
    ```

    Replace {repository-url} with the URL of your forked repository.

2.  **Navigate into the Project Directory:**

    ```bash
    cd django-weatherAPI
    ```

3.  **Create Virtual Environment and Activate it:**

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

4.  **Install Django and Django REST Framework:**

    ```bash
    pip install django djangorestframework
    ```

5.  **Change Directory and Run Migrate**

    ```bash
    cd weather_api
    python manage.py migrate
    ```

6.  **Running the Server:**

    To start the server, run the following command:

        ```bash
        python manage.py runserver
        ```

 7. **Access the Application:**

    Open your web browser and navigate to 'http://127.0.0.1:8000/'. Append one of the provided endpoints with any of the three cities to see your application in action.
