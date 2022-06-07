import json
import os
from dtools.enums import LoggingLevel, ConfigAttribute

DTOOLS_DIR = os.path.join(os.path.expanduser("~"), 'dtools')
CONFIG_PATH = os.path.join(DTOOLS_DIR, 'config.json')
REPO_PATH = os.path.dirname(os.path.abspath(__file__))


def _check_logging_levels(logging_levels):
    possible_values = set([e.value for e in LoggingLevel])
    if logging_levels - possible_values:
        raise ValueError(f'Invalid {ConfigAttribute.LOGGING_LEVELS.value} {logging_levels - possible_values}')

def _create_new_config_entry():
    logging_levels = [LoggingLevel.EXCEPTION.value]
    return {
        ConfigAttribute.LOGGING_LEVELS.value: logging_levels,
        ConfigAttribute.LOG_FILE_PATH.value: 'log.txt'
    }


class _Config:
    def __init__(self):
        if not os.path.exists(CONFIG_PATH):
            self._create_new_config_json()
        else:
            with open(CONFIG_PATH, 'r') as f:
                self._config_json = json.load(f)

            if REPO_PATH not in self._config_json:
                self.add_repo_to_config()
            else:
                _check_logging_levels(self.logging_levels)

    def add_repo_to_config(self):
        self._config_json[REPO_PATH] = _create_new_config_entry()
        self.save()

    def _create_new_config_json(self):
        self._config_json = {
            REPO_PATH: _create_new_config_entry()
        }
        self.save()

    def save(self):
        with open(CONFIG_PATH, 'w') as f:
            json.dump(self._config_json, f, indent=4)

    def set_logging_levels(self, logging_levels):
        logging_levels = set(logging_levels)
        _check_logging_levels(logging_levels)
        self._config_json[REPO_PATH][ConfigAttribute.LOGGING_LEVELS.value] = list(logging_levels)
        self.save()

    @property
    def logging_levels(self):
        return set(self._config_json[REPO_PATH][ConfigAttribute.LOGGING_LEVELS.value])


CONFIG = _Config()
