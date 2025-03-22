import requests

url = "https://api.openweathermap.org/data/2.5/forecast?lat=56.9669&lon=23.1534&appid=b1e1a0d37b486e563a13ed0ec0dce85b"

def get_response(url):
    response = requests.get(url).json()
    return response


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

response = get_response(url)

temp = round(kelvin_to_celsius(response["list"][0]["main"]["temp"]), 1)
feels_like = round(kelvin_to_celsius(response["list"][0]["main"]["feels_like"]), 1)
humidity = response["list"][0]["main"]["humidity"]
wind_speed = response["list"][0]["wind"]["speed"]
description = response["list"][0]["weather"][0]["description"]







print(response)
print(temp)
print(feels_like)
print(humidity)
print(wind_speed)
print(description)