from src.service.translate_description import translate_weather
from src.core.config import read_config

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def translate_description(description, lang):
    if lang == "RU":
        return translate_weather(description)
    else:
        return description

def prepareData(api_response, lang="EN"):
    temp = round(kelvin_to_celsius(api_response["list"][0]["main"]["temp"]), 1)
    feels_like = round(kelvin_to_celsius(api_response["list"][0]["main"]["feels_like"]), 1)
    humidity = api_response["list"][0]["main"]["humidity"]
    wind_speed = api_response["list"][0]["wind"]["speed"]
    description = translate_description(api_response["list"][0]["weather"][0]["description"], lang)

    return {
        "city": read_config()["city"],
        "temp": temp,
        "feels_like": feels_like,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "description": description
    }

