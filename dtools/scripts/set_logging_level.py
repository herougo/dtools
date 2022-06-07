import argparse
from dtools.enums import LoggingLevel
from dtools.config import CONFIG

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('levels', type=str)
    args = parser.parse_args()
    logging_levels = set(args.levels.strip().split(','))
    avail_logging_levels = set([e.value for e in LoggingLevel])
    logging_levels_diff = logging_levels - avail_logging_levels
    if logging_levels_diff:
        raise ValueError(f'Invalid logging levels provided: {logging_levels_diff}')
    CONFIG.set_logging_levels(logging_levels)
    print(f'Done!')


if __name__ == '__main__':
    main()