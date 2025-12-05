import logging
from pathlib import Path

LOG_FILE = Path("data/app.log")

def setup_logging(level: str = "INFO", show_init_log: bool = True):
    """
    Initialize logging for the application.

    Parameters:
        level (str): Logging level ("DEBUG", "INFO", etc.)
        show_init_log (bool): Whether to print the initialization message.
    """