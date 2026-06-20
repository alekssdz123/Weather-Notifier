import requests

def get_response(url):
    response = requests.get(url).json()
    return response

def getCoordinatesByLocation(city="London", country_code="UK", api_key=None):
    if api_key == None:
        return "You must set API key"
    
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&appid={api_key}"
    response = get_response(url)

    return {
        "lat": response[0]["lat"],
        "lon": response[0]["lon"]
    }

def getLocationWeather():
    city = "Tukums" # Get later from config
    country_code = "LV" # Get later from config
    api_key = "b1e1a0d37b486e563a13ed0ec0dce85b" # Get later from config

    coordinates = getCoordinatesByLocation(city, country_code, api_key)

    if type(coordinates) != dict: # if api_key == None
        return None

    lat = coordinates["lat"]
    lon = coordinates["lon"]

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = get_response(url)
    return response