import os
import sys
import subprocess

from pathlib import Path

from src.setup.base_setup import BaseSetup
from src.core.config import CONFIG_PATH

class WindowsSetup(BaseSetup):
    def __init__(self):
        super().__init__()

        self.startup_path = ( Path(os.environ["APPDATA"]) / r"Microsoft\Windows\Start Menu\Programs\Startup" / "run_weather_script.lnk")

    def check_startup_file(self):
        return self.startup_path.exists()
    
    def install_requirements(self):
        print("Installing required packages.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r",  str(self.requirements_file)])
        return True

    def create_startup_file(self):
        python_path = self.get_py_path()

        if Path(python_path).name == "python.exe":
            python_path = python_path.split("python.exe")
            python_path[1] = "pythonw.exe"
            python_path = python_path[0] + python_path[1]

        main_path = (self.base_dir / "main.py").resolve()

        script = f"""
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut('"{self.startup_path}"')
$Shortcut.TargetPath = '"{python_path}"'
$Shortcut.Arguments = '"{main_path}"'
$Shortcut.WorkingDirectory = '"{self.base_dir}"'
$Shortcut.Save()
        """

        result = subprocess.run(["powershell", "-NoProfile", "-Command", script])
        
        if result.returncode != 0:
            print(result.stderr)
            return False

        return True
    
    def delete_startup_file(self):
        os.remove(self.startup_path)

    def delete_config_file(self):
        os.remove(CONFIG_PATH)