from src.setup.base_setup import BaseSetup

class LinuxSetup(BaseSetup):
    def __init__(self):
        super().__init__()

    def check_startup_file(self):
        return True

    def create_startup_file(self):
        print("Linux startup is not configured yet.")