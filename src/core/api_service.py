import requests

from src.errors.custom_errors import *
from src.core.config import read_config

def get_response(url):
    response = requests.get(url)    
    if response.status_code == 401:
        raise InvalidApiKeyException
    elif response.status_code == 429:
        raise ApiLimitException
    elif response.status_code == 404:
        raise NotFoundException

    return response.json()

def getCoordinatesByLocation(city="London", country_code="UK", api_key=None):
    if api_key == None:
        return "You must set config."
    
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&appid={api_key}"
    
    response = get_response(url)

    return {
        "lat": response[0]["lat"],
        "lon": response[0]["lon"]
    }


def getLocationWeather():
    config_data = read_config()
    if config_data["city"] == None:
        coordinates = getCoordinatesByLocation()
        
    else:
        city = config_data["city"]
        country_code = config_data["country_code"]
        api_key = config_data["api_key"]
        coordinates = getCoordinatesByLocation(city, country_code, api_key)


    if type(coordinates) != dict: # if api_key == None
        return None

    lat = coordinates["lat"]
    lon = coordinates["lon"]

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = get_response(url)
    return response
