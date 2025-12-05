
import json
from pathlib import Path
from datetime import datetime, timedelta
import logging
import tempfile

logger = logging.getLogger(__name__)

CACHE_DIR = Path("data")
CACHE_DIR.mkdir(exist_ok=True)

CACHE_FILE = CACHE_DIR / "weather_cache.json"
TTL_MINUTES = 30   # Cache expires after 30 minutes



# INTERNAL HELPERS


def _load_all():
    """Load full cache dictionary safely."""

    if not CACHE_FILE.exists():
        return {}

    try:
        with CACHE_FILE.open("r") as f:
            return json.load(f)

    except json.JSONDecodeError:
        logger.error("⚠ Cache file corrupted — resetting weather_cache.json")
        try:
            CACHE_FILE.unlink()
        except Exception:
            pass
        return {}

    except Exception as e:
        logger.error(f"Unexpected error loading cache: {e}")
        return {}


def _save_all(cache_dict: dict):
    """Atomically write the entire cache dictionary."""

    try:
        with tempfile.NamedTemporaryFile(
            "w", delete=False, dir=CACHE_DIR, suffix=".tmp"
        ) as tmp:
            json.dump(cache_dict, tmp, indent=2)
            temp_name = tmp.name

        # atomic replace
        Path(temp_name).replace(CACHE_FILE)
        logger.info("Cache file updated safely.")

    except Exception as e:
        logger.error(f"⚠ Failed to write cache file: {e}")


# -------------------------------------------------------
# PUBLIC API FUNCTIONS
# -------------------------------------------------------

def load_cache(city: str):
    """
    RETURNS:
        (valid_payload, previous_temperature)

    IF expired:
        returns (None, stale_payload)
    """

    cache = _load_all()

    if city not in cache:
        return None, None

    entry = cache[city]

    # Extract stored data
    payload = entry.get("payload")
    previous_temp = entry.get("previous")
    timestamp = entry.get("timestamp")

    # Parse timestamp safely
    try:
        ts = datetime.fromisoformat(timestamp)
    except Exception:
        logger.error(f"Invalid timestamp for '{city}', ignoring this cache.")
        return None, payload   # stale only

    # Check TTL expiry
    if datetime.now() - ts > timedelta(minutes=TTL_MINUTES):
        logger.warning(f"Cache expired for '{city}'. Returning stale data only.")
        return None, payload

    # Valid cache entry
    return payload, previous_temp


def save_cache(city: str, payload: dict):
    """
    Save weather data for a city:
        - Full payload (temperature, windspeed, weathercode...)
        - Previous temperature
        - Timestamp
    """

    cache = _load_all()

    # Extract previous temperature (for trend comparison)
    previous_temp = (
        cache.get(city, {})
             .get("payload", {})
             .get("temperature")
    )

    cache[city] = {
        "timestamp": datetime.now().isoformat(),
        "payload": payload,
        "previous": previous_temp
    }

    _save_all(cache)

def clear_cache():
    """Delete the entire weather_cache.json file."""
    try:
        if CACHE_FILE.exists():
            CACHE_FILE.unlink()
            logger.info("Cache file cleared successfully.")
        else:
            logger.info("No cache file found.")
    except Exception as e:
        logger.error(f"Failed to clear cache: {e}")




