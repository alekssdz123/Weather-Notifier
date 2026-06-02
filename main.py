import requests
from time import sleep
from win11toast import toast

from translate import translate_weather

city = 'Tukums'
url = "https://api.openweathermap.org/data/2.5/forecast?lat=56.9669&lon=23.1534&appid=b1e1a0d37b486e563a13ed0ec0dce85b"


def get_response(url):
    response = requests.get(url).json()
    return response


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def check_internet():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        return True
    except:
        return False


if __name__ == "__main__":
    while check_internet() == False:
        sleep(1)
        check_internet()
    response = get_response(url)

    temp = round(kelvin_to_celsius(response["list"][0]["main"]["temp"]), 1)
    feels_like = round(kelvin_to_celsius(response["list"][0]["main"]["feels_like"]), 1)
    humidity = response["list"][0]["main"]["humidity"]
    wind_speed = response["list"][0]["wind"]["speed"]
    description = translate_weather(response["list"][0]["weather"][0]["description"])

    toast(f'Погода {city}', f'{description} \nТемпература: {temp}°С \nОщущается как: {feels_like}°С \nВлажность: {humidity}% \nСкорость ветра: {wind_speed}')
