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



#CITY LIST BUILDER 

def build_city_list(args, cfg) -> list[str]:
    cities = []

    # -c Delhi -c Pune
    if args.cities:
        if isinstance(args.cities, list):
            cities.extend(args.cities)

    # positional: weather-harvester Delhi
    if args.positional_city:
        cities.extend(args.positional_city)

    # --export-csv
    if args.export_csv:
        export_cache_to_csv()

    # default city
    if not cities:
        cities = [cfg["city"]]

    # validation
    valid = []
    for c in cities:
        if validate_city_name(c):
            valid.append(c)
        else:
            print(f"\n❌ Invalid city name: {c}")
            print("Allowed: letters, spaces, hyphens")
            exit(1)

    return valid

# PER CITY PROCESSING 

def process_city(city, base_lat, base_lon, use_cache, alert_temp, args):
    print(f"\n{Fore.BLUE}{Style.BRIGHT}====== {city.upper()} ======{Style.RESET_ALL}")
    logging.info(f"Processing city: {city}")

    lat, lon = get_coords_for_city(city, base_lat, base_lon)

    if args.map:
        open_map(lat, lon)

    weather = None
    previous_temp = None

    # Load cache
    if use_cache:
        cached, prev_temp = load_cache(city)
        if cached:
            print(f"{Fore.GREEN}Using Cached Weather{Style.RESET_ALL}")
            weather = cached
            previous_temp = prev_temp

    # Fetch fresh weather if cache is disabled or stale
    if weather is None:
        weather = fetch_weather(lat, lon)

        if not weather:
            print(f"{Fore.RED}❌ Failed to fetch weather for {city}.{Style.RESET_ALL}")
            logging.error(f"Weather fetch failed: {city}")
            return

        print(f"{Fore.CYAN}Fetched New Weather Data{Style.RESET_ALL}")
        save_cache(city, weather)

    #  WEATHER OUTPUT 
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}🌤 Weather Details:{Style.RESET_ALL}")
    print(f"• Temperature: {Fore.MAGENTA}{weather['temperature']}°C{Style.RESET_ALL}")
    print(f"• Wind Speed: {Fore.CYAN}{weather['windspeed']} km/h{Style.RESET_ALL}")
    print(f"• Wind Direction: {Fore.BLUE}{weather['winddirection']}°{Style.RESET_ALL}")
    print(f"• Weather Code: {weather['weathercode']}")
    print(f"• Time: {weather['time']}")

    #  TREND DETECTION 
    if previous_temp is not None:
        diff = weather["temperature"] - previous_temp
        if diff > 0:
            print(f"{Fore.YELLOW}📈 Temperature Rising (+{diff:.1f}°C)")
        elif diff < 0:
            print(f"{Fore.CYAN}📉 Temperature Dropping ({diff:.1f}°C)")
        else:
            print(f"{Fore.WHITE}➖ Temperature Stable")
    else:
        print(f"{Fore.WHITE}ℹ No previous temperature to compare.")

    #  ALERT SYSTEM 
    if check_alert(weather, alert_temp):
        print(f"{Fore.RED}{Style.BRIGHT}⚠ ALERT ACTIVE FOR {city}!{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}✓ No alert for {city}.{Style.RESET_ALL}")


# MAIN 

def main():
    args = get_args()
    cfg = load_config(args.config)

    setup_logging(args.log_level or cfg["log_level"])

    #  NEW FEATURE: CLEAR CACHE 
    if args.clear_cache:
        clear_cache()
        print("🧹 Cache cleared successfully!")
        return

    # CACHE CONTROL
    use_cache = not args.no_cache and cfg["use_cache"]

    alert_temp = args.alert_temp or cfg["alert_temp"]
    base_lat = args.lat or cfg["lat"]
    base_lon = args.lon or cfg["lon"]

    # Build list of cities
    cities = build_city_list(args, cfg)

    # Process all cities concurrently
    with ThreadPoolExecutor(max_workers=len(cities)) as executor:
        futures = [
            executor.submit(
                process_city,
                city,
                base_lat,
                base_lon,
                use_cache,
                alert_temp,
                args
            )
            for city in cities
        ]
        for _ in as_completed(futures):
            pass

    # Show cache contents
    if args.show_cache:
        print_cache_as_table()

    print(f"{Fore.GREEN}✓ All cities processed!{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
