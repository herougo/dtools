import json
import os
from dtools.enums import LoggingLevel, ConfigAttribute

DTOOLS_DIR = os.path.join(os.path.expanduser("~"), 'dtools')
CONFIG_PATH = os.path.join(DTOOLS_DIR, 'config.json')
LOGGING_LEVELS = None
REPO_PATH = os.path.dirname(os.path.abspath(__file__))


if not os.path.exists(CONFIG_PATH):
    logging_levels = [LoggingLevel.EXCEPTION.value]
    with open(CONFIG_PATH, 'w') as f:
        json.dump({
            REPO_PATH: {
                ConfigAttribute.LOGGING_LEVELS.value: logging_levels
            }
        }, f, indent=4)
    LOGGING_LEVELS = set(logging_levels)
else:
    with open(CONFIG_PATH, 'r') as f:
        config = json.load(f)

    if REPO_PATH not in config:
        logging_levels = [LoggingLevel.EXCEPTION.value]
        with open(CONFIG_PATH, 'w') as f:
            config[REPO_PATH] = {
                ConfigAttribute.LOGGING_LEVELS.value: logging_levels
            }
            json.dump(config, f, indent=4)
        LOGGING_LEVELS = set(logging_levels)
    else:
        LOGGING_LEVELS = set(config[REPO_PATH][ConfigAttribute.LOGGING_LEVELS.value])
        possible_values = set([e.value for e in LoggingLevel])
        if LOGGING_LEVELS - possible_values:
            raise ValueError(f'Invalid {ConfigAttribute.LOGGING_LEVELS.value} {LOGGING_LEVELS - possible_values}')
