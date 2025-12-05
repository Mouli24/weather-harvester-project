import logging
import platform
from colorama import Fore, Style, init
from weather_harvester.turtle_alert import turtle_clean_skull_alert

init(autoreset=True)

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

    

    # ------------------ RAIN ALERT ------------------
    if condition in ["Rain", "Rain showers", "Freezing rain", "Light drizzle"]:
        print(f"{Fore.BLUE}🌧 It is raining: {condition}")
        alert_triggered = True

    if condition in ["Rain showers", "Freezing rain", "Thunderstorm"]:
        print(f"{Fore.RED}⚠ HEAVY RAIN ALERT!")
        play_alert_sound()
        alert_triggered = True

    # ------------------ WIND ALERTS ------------------
    if wind > 40:
        print(f"{Fore.RED}🌀 SEVERE WIND ALERT: {wind} km/h")
        play_alert_sound()
        turtle_clean_skull_alert()
        alert_triggered = True
    elif wind > 25:
        print(f"{Fore.MAGENTA}⚠ STRONG WIND: {wind} km/h")
        play_alert_sound()
        alert_triggered = True
    elif wind > 5:
        print(f"{Fore.CYAN}💨 Windy: {wind} km/h")
        play_alert_sound()
        alert_triggered = True

    logging.info(f"Alert Check | Temp={temp} | Wind={wind} | Condition={condition}")
    return alert_triggered


def play_alert_sound():
    os_name = platform.system()

    try:
        if os_name == "Windows":
            import winsound
            for _ in range(5):
                winsound.Beep(1500, 150)
                winsound.Beep(900, 150)
        else:
            print("\a")

    except Exception as e:
        logging.error(f"Sound error: {e}")


def detect_trend(prev_temp, new_temp):
    if prev_temp is None:
        return "no-data"
    if new_temp > prev_temp:
        return "rising"
    elif new_temp < prev_temp:
        return "dropping"
    return "stable"