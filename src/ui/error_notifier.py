import pathlib
from desktop_notifier import DesktopNotifier
from src.service.translate_message import translations
from src.ui.helper.icon_helper import select_icon

async def show_error_notification(error, lang=None):
    if not lang:
        lang = "EN"
        
    notifier = DesktopNotifier()
    icon_path = select_icon()

    await notifier.send(
        title=translations[lang]["error"],
        message=translations[lang][error],
        icon=icon_path
    )