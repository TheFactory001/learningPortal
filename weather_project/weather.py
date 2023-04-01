lagos_result = {
    "coord": {"lon": 3.75, "lat": 6.5833},
    "weather": [
        {"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d"}
    ],
    "base": "stations",
    "main": {
        "temp": 304.33,
        "feels_like": 307.39,
        "temp_min": 304.33,
        "temp_max": 304.33,
        "pressure": 1007,
        "humidity": 56,
        "sea_level": 1007,
        "grnd_level": 1007
    },
    "visibility": 10000,
    "wind": {"speed": 2.49, "deg": 189, "gust": 1.97},
    "clouds": {"all": 94},
    "dt": 1679496335,
    "sys": {"type": 1, "id": 1185, "country": "NG", "sunrise": 1679464104, "sunset": 1679507733},
    "timezone": 3600,
    "id": 2332453,
    "name": "Lagos",
    "cod": 200
}


def get_weather_details(weather_json):
    weather_description = weather_json["weather"][0]["description"]
    return weather_description


print(get_weather_details(lagos_result))


def create_url(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    key_link_text = "appid="
    API_KEY = "a1d832c101f04481e98ece5a0a6cb290"
    city_link_text = "&q="
    full_link = base_url+key_link_text+API_KEY+city_link_text+city
    return full_link


print(create_url("Lagos"))
