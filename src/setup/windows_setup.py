import os
from pathlib import Path

from src.setup.base_setup import BaseSetup

class WindowsSetup(BaseSetup):
    def __init__(self):
        super().__init__()

        self.startup_path = ( Path(os.environ["APPDATA"]) / r"Microsoft\Windows\Start Menu\Programs\Startup" / "run_weather_script.bat")

    def check_startup_file(self):
        return self.startup_path.exists()

    def create_startup_file(self):
        python_path = self.get_py_path()
        main_path = (self.base_dir / "main.py").resolve()

        content = (
            "@echo off\n"
            f'"{python_path}" "{main_path}"'
        )

        with open(self.startup_path, "w") as file:
            file.write(content)