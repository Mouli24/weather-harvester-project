import argparse

def get_args(arg_list=None):
    parser = argparse.ArgumentParser(description="Weather Harvester CLI")

    #  POSITIONAL CITY 
    parser.add_argument(
        "positional_city",
        nargs="*",
        help="City name(s) provided without flags"
    )

    # CITY FLAGS
    parser.add_argument(
        "-c", "--city",
        dest="cities",
        action="append",
        help="City name (can be used multiple times: -c Delhi -c Pune)"
    )

    parser.add_argument("--no-cache",
    action="store_true",
    help="Force fetch fresh weather (ignore cache)")

    parser.add_argument(
        "-C", "--cities",
        type=str,
        help="Comma-separated list of cities: --cities Delhi,Mumbai"
    )
    parser.add_argument("--clear-cache", 
    action="store_true",
    help="Delete all cached weather data")


    #  COORDINATES 
    parser.add_argument(
        "--lat",
        type=float,
        help="Latitude override (used if city has no predefined coordinates)"
    )

    parser.add_argument(
        "--lon",
        type=float,
        help="Longitude override (used if city has no predefined coordinates)"
    )

    #  CACHE OPTIONS 
    parser.add_argument(
        "--use-cache",
        action="store_true",
        help="Use cached weather data if available"
    )

    parser.add_argument(
        "--show-cache",
        action="store_true",
        help="Display cached weather data as a table"
    )
    parser.add_argument(
        "--export-csv",
        action="store_true",
        help="Export cached weather data to CSV"
    )

    