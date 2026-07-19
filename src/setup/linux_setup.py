import os
from pathlib import Path

from src.setup.base_setup import BaseSetup
from src.core.config import CONFIG_PATH

class LinuxSetup(BaseSetup):
    def __init__(self):
        super().__init__()

        self.startup_path = Path.home() / ".config/autostart/weather-notifier.desktop"

    def check_startup_file(self):
        return self.startup_path.exists()

    def create_startup_file(self):
        py_path = self.get_py_path()
        main_path = (self.base_dir / "main.py").resolve()
        self.startup_path.parent.mkdir(parents=True, exist_ok=True)

        content = (
            "[Desktop Entry]\n"
            "Type=Application\n"
            "Name=Weather Notifier\n"
            "Comment=Weather notifier\n"
            f"Path={self.base_dir}"
            f"Exec=\"{py_path}\" \"{main_path}\"\n"
            "Terminal=false\n"
            "StartupNotify=false\n"
            "X-GNOME-Autostart-enabled=true\n"
        )

        with open(self.startup_path, "w") as file:
            file.write(content)
        
        return True

    def install_requirements(self):
        print("Linux requirements automatic installation is not supported yet.")
        print("Please install requirements by yourself.")
        print("1. Create virtual environment:\npython3 -m venv .venv")
        print("2. Activate it:\nsource .venv/bin/activate")
        print("3. Install required packages:\npython3 -m pip install -r requirements.txt")

        return False
    
    def delete_startup_file(self):
        os.remove(self.startup_path)

    def delete_config_file(self):
        os.remove(CONFIG_PATH)