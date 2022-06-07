from dtools.enums import LoggingLevel
from dtools.config import LOGGING_LEVELS


def meets_logging_level(specific_logging_levels):
    if not isinstance(specific_logging_levels, set):
        specific_logging_levels = {specific_logging_levels}
    if LoggingLevel.NONE.value in LOGGING_LEVELS:
        return False
    return (LoggingLevel.ALL.value in LOGGING_LEVELS or
            LoggingLevel.ALL.value in specific_logging_levels or
            (LOGGING_LEVELS & specific_logging_levels))

