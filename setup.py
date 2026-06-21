from time import sleep
from src.config import update_config

def get_py_path():
    python_path = None
    
    print("\nPython path")
    print("To know where your python is located, you should print `where python` in CMD")
    
    while True:
        python_path = input("Enter python path: ")
        python_path = python_path.replace(" ", "")
        
        if python_path.split("\\")[-1] == "python.exe":
            break

        print("Invalid python.exe path.")

    return python_path

def create_bat_file():
    pass

def input_config_data():
    print("Set city (If you want to leave it as it is, leave the blank empty)")
    city = input("Enter city name: ")

    print("Set country code (for example LV, US, EN, etc.) (If you want to leave it as it is, leave the blank empty)")
    country_code = input("Enter country code: ")

    print("Set language (RU/EN) (If you want to leave it as it is, leave the blank empty)")
    lang = input("Enter language: ")

    print("Set API key (If you want to leave it as it is, leave the blank empty)")
    api_key = input("Enter API key: ")

    return {
        "city": city.lower().capitalize().replace(" ", ""),
        "country_code": country_code.upper().replace(" ", ""),
        "api_key": api_key.replace(" ", ""),
        "lang": lang.upper().replace(" ", "")
    }

def set_config():
    data = input_config_data()
    update_config(data)

def cli(): # implement change config / installer here
    pass

if __name__ == "__main__":
    print(get_py_path())