# 🌦 Weather Harvester CLI Tool

A powerful, multi-feature command-line weather monitoring system built in Python. This tool fetches real-time weather data, displays it beautifully in the terminal, shows GUI maps, sends desktop notifications, handles alerts, exports data, and caches city weather intelligently.

## 📦 Installation

### Basic Installation

Install the package from PyPI:

```bash
pip install weather-harvester
```

### Full Installation (Recommended)

For complete functionality including rich CLI interface, map visualization, and desktop notifications:

```bash
pip install weather-harvester
pip install rich 
pip install folium
pip install plyer
```

**Optional Dependencies:**
- `rich` - Beautiful and colorful CLI interface
- `folium` - Interactive map visualization
- `plyer` - Desktop notifications for alerts

## 🚀 Quick Start

After installation, use the `weather-harvester` command:

```bash
weather-harvester -c London
```

## ✨ Features

- 🌍 **Multi-city support** - Fetch weather for multiple cities simultaneously
- ⚡ **Fast concurrent fetching** - Uses ThreadPoolExecutor for ultra-fast performance
- 💾 **Smart caching** - Cache weather data with TTL logic
- 🚨 **Temperature alerts** - Get notified when temperature exceeds thresholds
- 📊 **Data export** - Export cached data to CSV
- 🗺️ **Map integration** - Open city locations in Google Maps
- 📈 **Temperature trends** - Track temperature changes over time
- 🎨 **Beautiful CLI** - Colorful terminal output with colorama
- 📝 **Logging support** - Configurable logging levels

## 📖 Usage Examples

### Basic Commands

**Fetch weather for a single city:**
```bash
weather-harvester -c Delhi
```

**Fetch weather for multiple cities:**
```bash
weather-harvester -c Delhi -c Mumbai -c Kolkata
```

**Using comma-separated cities:**
```bash
weather-harvester --cities "Delhi,Mumbai,Kolkata"
```

### Cache Commands

**Use cached data (if available):**
```bash
weather-harvester --use-cache -c London
```
**Not using  cached data:**
```bash
weather-harvester --no-cache -c Delhi
```
**for clearing cached data:**
```bash
weather-harvester --clear-cache
```

**Show all cached weather data:**
```bash
weather-harvester --show-cache
```

**Export cache to CSV:**
```bash
weather-harvester --export-csv
```

### Alert Commands

**Set temperature alert threshold:**
```bash
weather-harvester -c Dubai --alert-temp 40
```

**Set low temperature alert:**
```bash
weather-harvester -c Moscow --alert-low 0
```

### Map & Coordinates

**Open city location in Google Maps:**
```bash
weather-harvester -c Paris --map
```

**Use custom coordinates:**
```bash
weather-harvester --lat 28.6139 --lon 77.2090
```

### Logging

**Set logging level:**
```bash
weather-harvester -c Tokyo --log-level DEBUG
weather-harvester -c Berlin --log-level INFO
weather-harvester -c Sydney --log-level WARNING
weather-harvester -c Toronto --log-level ERROR
```

### Configuration

**Use custom config file:**
```bash
weather-harvester --config /path/to/config.ini
```

## 🏗️ Architecture

```
┌──────────────────────┐
│     main.py          │
│  (App Controller)    │
└─────────┬────────────┘
          │
┌─────────┼─────────────────────┐
│         │                     │
▼         ▼                     ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│  cli.py  │  │config.py │  │logging_  │
│ Parses   │  │ Loads    │  │system.py │
│arguments │  │config.ini│  │Sets logs │
└────┬─────┘  └─────┬────┘  └─────┬────┘
     │              │             │
     ▼              ▼             ▼
┌──────────┐  ┌────────────┐  ┌─────────────┐
│ fetcher  │  │ cache.py   │  │ alerts.py   │
│ Fetches  │◄─►│ load/save  │  │temp alerts  │
│ API data │  │ TTL logic  │  │color+sound  │
└────┬─────┘  └─────┬──────┘  └───────┬─────┘
     │              │                 │
     └──────────────┴─────────────────┘
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    ┌────────────┐    ┌──────────────┐
    │ data/      │    │ tests/       │
    │cache files │    │unit tests    │
    └────────────┘    └──────────────┘
```

## 🛠️ Development Setup

If you want to contribute or run from source:

**Clone the repository:**
```bash
git clone <repository-url>
cd weather_harvester
```

**Create and activate virtual environment:**
```bash
python -m venv venv

# On Mac/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

**Install in development mode:**
```bash
pip install -e .
```

**Run tests:**
```bash
python -m unittest discover tests
```

## 📋 Requirements

**Core Requirements:**
- Python 3.7+
- colorama (automatically installed with package)

**Optional Requirements (for full features):**
- `rich` - Enhanced CLI interface with better formatting
- `folium` - Map visualization support
- `plyer` - Desktop notification alerts

**Install all optional dependencies:**
```bash
pip install rich folium plyer
```

## 🔗 Links

- PyPI: https://pypi.org/project/weather-harvester/
- Issues: Report bugs and request features

## 📄 License

This project is open source and available for use.

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.
