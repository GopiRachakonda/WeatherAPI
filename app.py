import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# Replace with your actual OpenWeatherMap API key
API_KEY = 'e7b47b9aa198aac8cd6f58f9cb42ddfe'  # Replace this with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    city = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')

        # Get the current weather data
        weather_url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
        weather_response = requests.get(weather_url)

        # Get the 5-day weather forecast data
        forecast_url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
        forecast_response = requests.get(forecast_url)

        # Check if the weather request was successful
        if weather_response.status_code == 200:
            weather_data = weather_response.json()
        else:
            weather_data = None
            # Display the error message returned from the API
            error_message = f"Error fetching weather data: {weather_response.json().get('message', 'Unknown error')}"

        # Check if the forecast request was successful
        if forecast_response.status_code == 200:
            forecast_data = forecast_response.json()
        else:
            forecast_data = None
            # Display the error message returned from the API
            error_message = f"Error fetching forecast data: {forecast_response.json().get('message', 'Unknown error')}"

    return render_template('index.html', weather_data=weather_data, forecast_data=forecast_data, city=city, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
