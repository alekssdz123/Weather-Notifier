import sys
import winreg
import pathlib


def get_windows_ui_theme() -> int:
    REGISTRY_PATH = "Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"

    if sys.platform != "win32":
        return 1

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REGISTRY_PATH) as key:
            theme, _ = winreg.QueryValueEx(key, "SystemUsesLightTheme")
            return theme
    except:
        return 1

# if light theme, use black icon, if theme is dark - use light theme
def select_icon() -> pathlib.Path:
    light_theme_on = get_windows_ui_theme()

    if light_theme_on:
        return pathlib.Path(__file__).parent.parent.parent.parent / "images" / "icon_black.png"
    return pathlib.Path(__file__).parent.parent.parent.parent / "images" / "icon_white.png"
