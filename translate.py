def translate_weather(description):
    match description:
        case "thunderstorm with light rain":
            return "гроза с небольшим дождем"
        case "thunderstorm with rain":
            return "гроза с дождем"
        case "thunderstorm with heavy rain":
            return "гроза с сильным дождем"
        case "light thunderstorm":
            return "слабая гроза"
        case "thunderstorm":
            return "гроза"
        case "heavy thunderstorm":
            return "сильная гроза"
        case "ragged thunderstorm":
            return "порывистая гроза"
        case "thunderstorm with light drizzle":
            return "гроза с небольшим моросящим дождем"
        case "thunderstorm with drizzle":
            return "гроза с моросящим дождем"
        case "thunderstorm with heavy drizzle":
            return "гроза с сильным моросящим дождем"
        case "light intensity drizzle":
            return "слабый моросящий дождь"
        case "drizzle":
            return "моросящий дождь"
        case "heavy intensity drizzle":
            return "сильный моросящий дождь"
        case "light rain":
            return "небольшой дождь"
        case "moderate rain":
            return "умеренный дождь"
        case "heavy intensity rain":
            return "сильный дождь"
        case "very heavy rain":
            return "очень сильный дождь"
        case "extreme rain":
            return "чрезвычайно сильный дождь"
        case "freezing rain":
            return "ледяной дождь"
        case "light snow":
            return "небольшой снег"
        case "snow":
            return "снег"
        case "heavy snow":
            return "сильный снегопад"
        case "sleet":
            return "мокрый снег"
        case "shower sleet":
            return "ливневый мокрый снег"
        case "light rain and snow":
            return "небольшой дождь со снегом"
        case "rain and snow":
            return "дождь со снегом"
        case "light shower snow":
            return "небольшой ливневый снег"
        case "shower snow":
            return "ливневый снег"
        case "heavy shower snow":
            return "сильный ливневый снег"
        case "mist":
            return "туман"
        case "smoke":
            return "дымка"
        case "haze":
            return "мгла"
        case "sand/dust whirls":
            return "пыльные вихри"
        case "fog":
            return "густой туман"
        case "clear sky":
            return "ясное небо"
        case "few clouds":
            return "малооблачно"
        case "scattered clouds":
            return "рассеянные облака"
        case "broken clouds":
            return "облачность"
        case "overcast clouds":
            return "пасмурно"
        case "tornado":
            return "торнадо"
        case "tropical storm":
            return "тропический шторм"
        case "hurricane":
            return "ураган"
        case "cold":
            return "холодно"
        case "hot":
            return "жарко"
        case "windy":
            return "ветрено"
        case "hail":
            return "град"
        case _:
            return "неизвестное погодное явление"