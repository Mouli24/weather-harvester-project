# exporter.py

import csv
import json
from pathlib import Path
from rich.console import Console
from rich.table import Table

CACHE_FILE = Path("data/weather_cache.json")
console = Console()


def export_cache_to_csv(csv_file="weather_cache_export.csv"):
    """Exports the entire cached JSON into a CSV file."""
    if not CACHE_FILE.exists():
        print("❌ No cache file found.")
        return

    with open(CACHE_FILE, "r") as f:
        cache = json.load(f)
