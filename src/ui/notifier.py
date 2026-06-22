from win11toast import toast

from src.service.weather_service import prepareData

def format_message(response, lang):
    data = prepareData(response, lang)
    if lang == "RU":
        output_message = f"Погода {data["city"]} \n{data["description"]} \nТемпература: {data["temp"]}°С \nОщущается как: \
{data["feels_like"]}°С \nВлажность: {data["humidity"]}% \nСкорость ветра: {data["wind_speed"]}"
        
    else:
        output_message = f"Weather in {data["city"]} \n{data["description"].capitalize()} \nTemprature: {data["temp"]}°С \nFeels like: \
{data["feels_like"]}°С \nHumidity: {data["humidity"]}% \nWind speed: {data["wind_speed"]}"
    
    return output_message


def show_notification(response, lang):
    message = format_message(response, lang)
    toast(message)
