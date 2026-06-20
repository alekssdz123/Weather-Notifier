import requests
from time import sleep

from src.output import weather_notification
from src.api import getLocationWeather

def check_internet():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        return True
    except:
        return False

def main():
    while check_internet() == False:
        sleep(1)
        check_internet()

    response = getLocationWeather()
    if response == None:
        print("You must set API key")
        return None

    weather_notification(response, lang="EN")
    
if __name__ == "__main__":
    main()