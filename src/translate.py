def translate_weather(description):
    match description:
        case "thunderstorm with light rain":
            return "Гроза с небольшим дождем"
        case "thunderstorm with rain":
            return "Гроза с дождем"
        case "thunderstorm with heavy rain":
            return "Гроза с сильным дождем"
        case "light thunderstorm":
            return "Слабая гроза"
        case "thunderstorm":
            return "Гроза"
        case "heavy thunderstorm":
            return "Сильная гроза"
        case "ragged thunderstorm":
            return "Порывистая гроза"
        case "thunderstorm with light drizzle":
            return "Гроза с небольшим моросящим дождем"
        case "thunderstorm with drizzle":
            return "Гроза с моросящим дождем"
        case "thunderstorm with heavy drizzle":
            return "Гроза с сильным моросящим дождем"
        case "light intensity drizzle":
            return "Слабый моросящий дождь"
        case "drizzle":
            return "Моросящий дождь"
        case "heavy intensity drizzle":
            return "Сильный моросящий дождь"
        case "light rain":
            return "Небольшой дождь"
        case "moderate rain":
            return "Умеренный дождь"
        case "heavy intensity rain":
            return "Сильный дождь"
        case "very heavy rain":
            return "Очень сильный дождь"
        case "extreme rain":
            return "Чрезвычайно сильный дождь"
        case "freezing rain":
            return "Ледяной дождь"
        case "light snow":
            return "Небольшой снег"
        case "snow":
            return "Снег"
        case "heavy snow":
            return "Сильный снегопад"
        case "sleet":
            return "Мокрый снег"
        case "shower sleet":
            return "Ливневый мокрый снег"
        case "light rain and snow":
            return "Небольшой дождь со снегом"
        case "rain and snow":
            return "Дождь со снегом"
        case "light shower snow":
            return "Небольшой ливневый снег"
        case "shower snow":
            return "Ливневый снег"
        case "heavy shower snow":
            return "Сильный ливневый снег"
        case "mist":
            return "Туман"
        case "smoke":
            return "Дымка"
        case "haze":
            return "Мгла"
        case "sand/dust whirls":
            return "Пыльные вихри"
        case "fog":
            return "Густой туман"
        case "clear sky":
            return "Ясное небо"
        case "few clouds":
            return "Малооблачно"
        case "scattered clouds":
            return "Рассеянные облака"
        case "broken clouds":
            return "Облачность"
        case "overcast clouds":
            return "Пасмурно"
        case "tornado":
            return "Торнадо"
        case "tropical storm":
            return "Тропический шторм"
        case "hurricane":
            return "Ураган"
        case "cold":
            return "Холодно"
        case "hot":
            return "Жарко"
        case "windy":
            return "Ветрено"
        case "hail":
            return "Град"
        case _:
            return "Неизвестное погодное явление"