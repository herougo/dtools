from enum import Enum

class LoggingLevel(Enum):
    EXCEPTION = 'exception'
    ALL = 'all'
    NONE = 'none'

class ConfigAttribute(Enum):
    LOGGING_LEVELS = 'logging_levels'