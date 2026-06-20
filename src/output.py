from src.translate import translate_weather
from src.config import read_config
from win11toast import toast

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def prepareData(api_response, lang="EN"):
    temp = round(kelvin_to_celsius(api_response["list"][0]["main"]["temp"]), 1)
    feels_like = round(kelvin_to_celsius(api_response["list"][0]["main"]["feels_like"]), 1)
    humidity = api_response["list"][0]["main"]["humidity"]
    wind_speed = api_response["list"][0]["wind"]["speed"]

    if lang == "RU":
        description = translate_weather(api_response["list"][0]["weather"][0]["description"])
    else:
        description = api_response["list"][0]["weather"][0]["description"]

    return {
        "city": read_config()["city"],
        "temp": temp,
        "feels_like": feels_like,
        "humidity": humidity,
        "wind_speed": wind_speed,
        "description": description
    }

def weather_notification(response, lang):
    data = prepareData(response, lang)
    if lang == "RU":
        output_message = f"Погода {data["city"]} \n{data["description"]} \nТемпература: {data["temp"]}°С \nОщущается как: \
{data["feels_like"]}°С \nВлажность: {data["humidity"]}% \nСкорость ветра: {data["wind_speed"]}"
        
    else:
        output_message = f"Weather in {data["city"]} \n{data["description"].capitalize()} \nTemprature: {data["temp"]}°С \nFeels like: \
{data["feels_like"]}°С \nHumidity: {data["humidity"]}% \nWind speed: {data["wind_speed"]}"
        
    toast(output_message)
