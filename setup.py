import subprocess
import sys
import os
from pathlib import Path
from time import sleep

from src.core.config import CONFIG_PATH
from src.core.config import update_config
from src.core.config import create_config

STARTUP_PATH = Path(os.environ["APPDATA"]) / r"Microsoft\Windows\Start Menu\Programs\Startup\run_weather_script.bat"

def check_python_version():
    version = sys.version_info

    if version < (3, 12):
        print("Python 3.12 or newer is required.")
        return False
    return True

def check_requirements():
    try:
        import desktop_notifier
        import requests
        return True
    except ImportError as e:
        print(f"Installing required packages.")
        return False

def install_requirements():
    requirements_file = "requirements.txt"
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])

def get_py_path():
    python_path = sys.executable
    return python_path

def check_startup_file():
    return Path(STARTUP_PATH).is_file()

def create_startup_file():
    py_path = get_py_path()
    absoulte_mainpy_path = Path("main.py").resolve()
    file_content = f'start "{py_path}" "{absoulte_mainpy_path}"'

    with open(STARTUP_PATH, "w") as file:
        file.write(file_content)

def check_config():
    return Path(CONFIG_PATH).is_file()

def input_config_data():
    print("Set config (If you want to leave it as it is, leave the blank empty)")
    city = input("City: ")
    country_code = input("Country code (LV, US etc.): ")
    lang = input("Language (RU/EN): ")
    api_key = input("API key: ")

    return {
        "city": city.lower().capitalize().replace(" ", ""),
        "country_code": country_code.upper().replace(" ", ""),
        "api_key": api_key.replace(" ", ""),
        "lang": lang.upper().replace(" ", "")
    }

def set_config():
    data = input_config_data()
    update_config(data)

def install():
    if not check_requirements():
        install_requirements()
    print("Requirements installed")
    if not check_startup_file():
        create_startup_file()
    print("Startup file created")
    if not check_config():
        create_config()
    print("Config.json created")

def setup_cli():
    print("Welcome in weather script setup!")
    if not check_python_version():
        print("Exit.")
        return
    
    while True:
        try:
            print("Options:")
            print("1. Install\t2. Set config\t3.Exit\n")
            option = input("Select your option: ")

            match option.lower().replace(" ", ""):
                case "1" | "install":
                    install()
                    print("\nEverything installed.\n")
                case "2" | "setconfig":
                    try:
                        set_config()
                        print("\nConfig changed successfully.\n")
                    except Exception as e:
                        print(f"Failed to change config {e}\n")
                case "3" | "exit":
                    print("Exit.")
                    break
                case _:
                    print("\nInvalid option.\n")
                    continue
        except Exception as e:
            print(f"ERROR. {e}")
        

if __name__ == "__main__":
    setup_cli()