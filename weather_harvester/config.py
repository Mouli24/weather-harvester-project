# config.py
from configparser import ConfigParser
from pathlib import Path

def load_config(path="config/config.ini") -> dict:
    cfg_path = Path(path)
    if not cfg_path.exists():
        print("CONFIG FILE NOT FOUND, USING HARDCODED DEFAULTS")
        return {
            "city": "Delhi",
            "lat": 28.6,
            "lon": 77.2,
            "use_cache": True,
            "log_level": "INFO",
            "alert_temp": 35
        }
