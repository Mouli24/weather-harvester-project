from weather_harvester.cli import get_args
from weather_harvester.config import load_config
from weather_harvester.fetcher import fetch_weather, get_coords_for_city
from weather_harvester.cache import load_cache, save_cache, clear_cache
from weather_harvester.logging_system import setup_logging
from weather_harvester.alerts import check_alert
from weather_harvester.exporter import export_cache_to_csv, print_cache_as_table
#  MAP UTILITY 

def open_map(lat, lon):
    url = f"https://www.google.com/maps?q={lat},{lon}"
    print(f"🗺 Opening map: {url}")
    webbrowser.open(url)


#  CITY VALIDATION 

def validate_city_name(city: str) -> bool:
    return bool(re.match(r"^[A-Za-z\s\-]+$", city))


