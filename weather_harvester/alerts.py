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
# ----------------------------
# MAIN ALERT FUNCTION
# ----------------------------
def check_alert(weather: dict, alert_temp: float):
    if not weather or "temperature" not in weather:
        logging.warning("Missing weather data for alert check")
        return False

    temp = weather["temperature"]
    wind = weather.get("windspeed", 0)
    code = weather.get("weathercode", None)

    condition = interpret_weather_code(code)

    print(f"\n{Fore.CYAN}Weather Condition: {condition}")

    alert_triggered = False

    # ------------------ TEMP ALERT ------------------
    if temp >= alert_temp:
        print(f"{Fore.RED}🔥 TEMPERATURE ALERT: {temp}°C >= {alert_temp}°C")
        play_alert_sound()
        turtle_clean_skull_alert()
        alert_triggered = True

    