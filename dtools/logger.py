import logging
import os

def create_info_logger(name, file_path):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    ch = logging.FileHandler(file_path)
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)
    return logger

LOGGER_DIR = os.path.join(os.path.expanduser("~"), 'dtools')
LOGGER_PATH = os.path.join(LOGGER_DIR, 'log.txt')

if not os.path.exists(LOGGER_DIR):
    os.makedirs(LOGGER_DIR)

LOGGER = create_info_logger('dtools', LOGGER_PATH)