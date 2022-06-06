import os

def iter_file_paths_recursively(directory):
    result = []
    for paths, subdirs, files in os.walk(directory):
        for file in files:
            yield os.path.join(paths, file)
    return result