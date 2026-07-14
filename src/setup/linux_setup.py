from src.setup.base_setup import BaseSetup

class LinuxSetup(BaseSetup):
    def __init__(self):
        super().__init__()

    def check_startup_file(self):
        print("Linux startup file creating is not supported yet.")
        return False

    def create_startup_file(self):
        print("Linux startup is not configured yet.")
        return False

    def install_requirements(self):
        print("Linux requirements automatic installation is not supported yet.")
        print("Please install requirements by yourself.")
        print("1. Create virtual environment:\npython3 -m venv .venv")
        print("2. Activate it:\nsource .venv/bin/activate")
        print("3. Install required packages:\npython3 -m pip install -r requirements.txt")

        return False