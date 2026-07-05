import pathlib
from desktop_notifier import DesktopNotifier
from src.service.translate_message import translations

async def show_error_notification(error, lang=None):
    if not lang:
        lang = "EN"
        
    notifier = DesktopNotifier()
    icon_path = pathlib.Path(__file__).parent.parent.parent / "images" / "logo.png"

    await notifier.send(
        title=translations[lang]["error"],
        message=translations[lang][error],
        icon=icon_path
    )