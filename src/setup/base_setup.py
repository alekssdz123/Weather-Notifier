import subprocess
import platform
import sys

from pathlib import Path

from src.core.config import CONFIG_PATH
from src.core.config import update_config
from src.core.config import create_config
from src.updater.updater import check_new_release
from src.updater.updater import get_last_release
from src.updater.updater import update

class BaseSetup:

    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.requirements_file = self.base_dir / "requirements.txt"

    def check_python_version(self):
        version = sys.version_info

        if version < (3, 12):
            print("Python 3.12 or newer is required.")
            return False

        return True

    def check_requirements(self):
        try:
            import desktop_notifier
            import requests
            return True

        except ImportError:
            return False

    def install_requirements(self):
        raise NotImplementedError

    def get_py_path(self):
        return sys.executable

    def check_startup_file(self):
        raise NotImplementedError

    def create_startup_file(self):
        raise NotImplementedError

    def check_config(self):
        return Path(CONFIG_PATH).is_file()

    def input_config_data(self):
        print(
            "Set config "
            "(If you want to leave it as it is, leave the blank empty)"
        )

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

    def set_config(self):
        data = self.input_config_data()
        update_config(data)

    def install(self):
        if not self.check_requirements():
            if not self.install_requirements():
                return

        print("Requirements installed")

        if not self.check_startup_file():
            if not self.create_startup_file():
                return

        print("Startup file created")

        if not self.check_config():
            if not create_config(CONFIG_PATH):
                return

        print("Config.json created")
    

    def delete_startup_file(self):
        raise NotImplementedError

    def delete_config_file(self):
        raise NotImplementedError

    def uninstall(self):
        if self.check_startup_file():
            self.delete_startup_file()

        if self.check_config():
            self.delete_config_file()


    def setup_cli(self):

        print("Welcome in weather script setup!")

        if not self.check_python_version():
            print("Exit.")
            return

        while True:
            try:
                print(
                    "Options:\n"
                    "1. Install\n"
                    "2. Set config\n"
                    "3. Update\n"
                    "4. Uninstall\n"
                    "5. Exit\n"
                )

                option = input("Select your option: ")
                match option.lower().replace(" ", ""):

                    case "1" | "install":
                        self.install()
                        print("\nEverything installed.\n")

                    case "2" | "setconfig":
                        try:
                            self.set_config()
                            print("\nConfig changed successfully.\n")

                        except FileNotFoundError:
                            print("Configuration file not found.")

                        except PermissionError:
                            print("Unable to write configuration file.")
                    
                    case "3" | "update":
                        last_release = check_new_release()
                        if not last_release:
                            print("\nLast release installed.")
                            print("Nothing to update.\n")
                            continue
                        print(f"\nVersion {get_last_release()["tag_name"]} avaible.")
                        print("Install it? (y/n): ", end="")

                        if input().lower().replace(" ", "") == "y":
                            update()
                            break

                    case "4" | "uninstall":
                        if platform.system() == "Linux": # TEST IT LATER
                            print("Uninstallation is not tested on linux yet.")

                        print("Confirm uninstallation (y/n): ", end="")
                        if input().lower().replace(" ", "") == "y":
                            self.uninstall()
                            print("Weather notifier uninstalled.")
                            break
                        print("Uninstallation canceled.")

                    case "5" | "exit":
                        print("Exit.")
                        break

                    case _:
                        print("Invalid option.")

            except Exception as e:
                print(f"ERROR: {e}")