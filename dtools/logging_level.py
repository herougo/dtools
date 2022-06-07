from dtools.enums import LoggingLevel
from dtools.config import CONFIG


def meets_logging_level(specific_logging_levels):
    if not isinstance(specific_logging_levels, set):
        specific_logging_levels = {specific_logging_levels}
    if LoggingLevel.NONE.value in CONFIG.logging_levels:
        return False
    return (LoggingLevel.ALL.value in CONFIG.logging_levels or
            LoggingLevel.ALL.value in specific_logging_levels or
            (CONFIG.logging_levels & specific_logging_levels))

