import os

import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def fetch_weather_data(city):
    params = {
        "q": city,
        "key": WEATHER_API_KEY,
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.json()


def parse_weather_data(data, city):
    temperature = data['current']['temp_c']
    description = data['current']['condition']['text']
    return f"The weather in {city} is {temperature}°C with {description}."


def get_weather(city):
    try:
        data = fetch_weather_data(city)
        return parse_weather_data(data, city)
    except requests.exceptions.RequestException as e:
        return f"Sorry, I couldn't fetch the weather for {city}. Please try again later. Error: {e}"
