import json
import os
from dtools.enums import LoggingLevel, ConfigAttribute

DTOOLS_DIR = os.path.join(os.path.expanduser("~"), 'dtools')
CONFIG_PATH = os.path.join(DTOOLS_DIR, 'config.json')
LOGGING_LEVELS = None

if not os.path.exists(CONFIG_PATH):
    logging_levels = [LoggingLevel.EXCEPTION.value]
    with open(CONFIG_PATH, 'w') as f:
        json.dump({
            ConfigAttribute.LOGGING_LEVELS.value: logging_levels
        }, f)
    LOGGING_LEVELS = set(logging_levels)
else:
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)
    LOGGING_LEVELS = set(config[ConfigAttribute.LOGGING_LEVELS.value])
    possible_values = set([e.value for e in LoggingLevel])
    if LOGGING_LEVELS - possible_values:
        raise ValueError(f'Invalid {ConfigAttribute.LOGGING_LEVELS.value} {LOGGING_LEVELS - possible_values}')
