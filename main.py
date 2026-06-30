import requests
import asyncio
from time import sleep

from src.ui.notifier import show_notification
from src.core.api import getLocationWeather
from src.core.config import read_config

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
        print("You must set config.")
        return None

    asyncio.run(show_notification(response, read_config()["lang"]))
    
if __name__ == "__main__":
    main()
