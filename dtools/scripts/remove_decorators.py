import argparse
from dtools.decorator_injection import remove_decorators_from_dir
import time

def main():
    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path', type=str)
    args = parser.parse_args()

    remove_decorators_from_dir(args.dir_path)
    print(f'Done after {time.time() - start_time}s!')


if __name__ == '__main__':
    main()