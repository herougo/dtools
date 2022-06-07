import logging
import os
from dtools.config import DTOOLS_DIR

def create_info_logger(name, file_path):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    ch = logging.FileHandler(file_path)
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)
    return logger


LOGGER_PATH = os.path.join(DTOOLS_DIR, 'log.txt')

if not os.path.exists(DTOOLS_DIR):
    os.makedirs(DTOOLS_DIR)

LOGGER = create_info_logger('dtools', LOGGER_PATH)