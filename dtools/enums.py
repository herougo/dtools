from enum import Enum

class LoggingLevel(Enum):
    EXCEPTION = 'exception'
    FUNCTION = 'function'
    ALL = 'all'
    NONE = 'none'

class ConfigAttribute(Enum):
    LOGGING_LEVELS = 'logging_levels'
    LOG_FILE_PATH = 'log_file_path'