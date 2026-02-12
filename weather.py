from requests import get as GET
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("WEATHER_TOKEN")


def get_weather_data(city_name: str) -> str:
    URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {
        "q": city_name,
        "appid": TOKEN,
        "lang": "ru",
        "units": "metric",
    }

    response = GET(url=URL, params=PARAMS)

    data = response.json() # JSON -> Python

    temp = data.get("main").get("temp")             # 9.25 C
    temp_min = data.get("main").get("temp_min")     # 7.25 C
    temp_max = data.get("main").get("temp_max")     # 10.25 C
    pressure = data.get("main").get("pressure")     # 1008 Pa
    humidity = data.get("main").get("humidity")     # 75 %

    text = f"{'-' * 50}\n"

    text += f"🌆 Bugun {city_name.capitalize()} dagi havo haqida"

    text += f"\n\n🌡️  Harorat: {temp} °C"
    text += f"\n🥶 Minimal harorat: {temp_min} °C"
    text += f"\n🥵 Maksimal harorat: {temp_max} °C"

    text += f"\n\n💧 Namlik: {humidity} %"
    text += f"\n⬇️  Bosim: {pressure} Pa"

    text += f"\n{'-' * 50}"

    return text
