import requests
import asyncio
from time import sleep
from json import JSONDecodeError

from src.ui.notifier import show_notification
from src.core.api_service import getLocationWeather
from src.core.config import read_config
from src.ui.error_notifier import show_error_notification
from src.errors.custom_errors import *


def check_internet():
    try:
        response = requests.get('https://www.google.com', timeout=5)
        return True
    except:
        return False

def main():    
    try:
        lang = read_config()["lang"]
        for x in range(10):
            if not check_internet():
                sleep(1)
                continue
            break
        else:
            raise NoInternetException

        response = getLocationWeather()
        if response == None:
            raise ConfigNotSetExceiption

        asyncio.run(show_notification(response, lang))

    except NoInternetException:
        asyncio.run(show_error_notification("no_internet", lang))
    except ApiError:
        asyncio.run(show_error_notification("api_unavailable", lang))
    except ConfigNotSetExceiption:
        asyncio.run(show_error_notification("config_required", lang))
    except InvalidApiKeyException:
        asyncio.run(show_error_notification("invalid_api_key", lang))
    except ApiLimitException:
        asyncio.run(show_error_notification("", lang))
    except FileNotFoundError:
        asyncio.run(show_error_notification("no_config"))
    except JSONDecodeError:
        asyncio.run(show_error_notification("invalid_config"))
    except Exception:
        asyncio.run(show_error_notification("unexpected"))

    
if __name__ == "__main__":
    main()
