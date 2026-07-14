import platform

from src.setup.windows_setup import WindowsSetup
from src.setup.linux_setup import LinuxSetup

def get_os():
    return platform.system()

def create_setup():
    system = get_os()
    match system:
        case "Windows":
            setup = WindowsSetup()
        case "Linux":
            setup = LinuxSetup()
        case _:
            print("OS not supported yet")
            return
    return setup

if __name__ == "__main__":
    setup = create_setup()
    if setup:
        setup.setup_cli()