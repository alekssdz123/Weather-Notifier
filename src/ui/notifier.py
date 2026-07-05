import pathlib
from desktop_notifier import DesktopNotifier

from src.service.weather_service import prepareData
from src.service.translate_message import translations

def format_message(response, lang):
    data = prepareData(response, lang)
    tr = translations[lang]

    return {
        "title": f"{tr['title']} {data['city']}",
        "message": (
            f"{data['description'].capitalize()}, {data['temp']}°C\n"
            f"{tr['feels_like']} {data['feels_like']}°C\n"
            f"{tr['humidity']} {data['humidity']}% | "
            f"{tr['wind']} {data['wind_speed']} m/s"
        ),
    }

async def show_notification(response, lang="EN"):
    notifier = DesktopNotifier()
    output = format_message(response, lang)
    icon_path = pathlib.Path(__file__).parent.parent.parent / "images" / "logo.png"
    
    await notifier.send(
        title=output["title"],
        message=output["message"],
        icon=icon_path
    )