import logging
import platform
from colorama import Fore, Style, init
from weather_harvester.turtle_alert import turtle_clean_skull_alert

init(autoreset=True)

# ----------------------------
# WEATHER CODE INTERPRETER
# ----------------------------
def interpret_weather_code(code: int) -> str:
    if code == 0:
        return "Clear sky"
    elif code in (1, 2, 3):
        return "Cloudy"
    elif 51 <= code <= 55:
        return "Light drizzle"
    elif 56 <= code <= 57:
        return "Freezing drizzle"
    elif 61 <= code <= 65:
        return "Rain"
    elif 66 <= code <= 67:
        return "Freezing rain"
    elif 80 <= code <= 82:
        return "Rain showers"
    elif 95 <= code <= 99:
        return "Thunderstorm"
    return "Unknown"

