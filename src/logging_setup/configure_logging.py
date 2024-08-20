import json
from pathlib import Path
import logging

def configure_logging():
    # NOTE: Logging is currently blocking
    # Use a queue_handler off the main thread if this is an issue

    config_file = Path().cwd() / ".logging_configs/config.json"
    with config_file.open("r") as file:
        config = json.load(file)
    logging.config.dictConfig(config)