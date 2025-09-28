#!/usr/bin/env python3
import argparse
import requests
from datetime import datetime

def get_weather(api_key, city_name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

def main():
    parser = argparse.ArgumentParser(description="Get weather details of a city by name")
    parser.add_argument("--apikey", required=True, help="OpenWeatherMap API key")
    parser.add_argument("--city", required=True, help="City name (e.g., Berlin)")
    args = parser.parse_args()

    try:
        data = get_weather(args.apikey, args.city)

        city = data["name"]
        country = data["sys"]["country"]
        temp_min = data["main"]["temp_min"]
        temp_max = data["main"]["temp_max"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        windspeed = data["wind"]["speed"]
        clouds = data["clouds"]["all"]
        sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"]).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.utcfromtimestamp(data["sys"]["sunset"]).strftime('%Y-%m-%d %H:%M:%S')

        print(f"\nWeather details for {city}, {country}\n")
        print(f"Temperature : Min {temp_min}C / Max {temp_max}C")
        print(f"Humidity    : {humidity}%")
        print(f"Pressure    : {pressure} hPa")
        print(f"Windspeed   : {windspeed} m/s")
        print(f"Cloud Cover : {clouds}%")
        print(f"Sunrise     : {sunrise} UTC")
        print(f"Sunset      : {sunset} UTC\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
