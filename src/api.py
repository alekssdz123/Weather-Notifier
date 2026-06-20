import requests

from src.config import read_config

def get_response(url):
    response = requests.get(url).json()
    return response

def getCoordinatesByLocation(city="London", country_code="UK", api_key=None):
    if api_key == None:
        return "You must set config."
    
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&appid={api_key}"
    
    try:
        response = get_response(url)

        return {
            "lat": response[0]["lat"],
            "lon": response[0]["lon"]
        }
    
    except Exception as e:
        print(f"Failed to load data from openweather API. {e}")


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

if __name__ == "__main__":
    print(getLocationWeather())