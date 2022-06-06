from dtools.utils import iter_file_paths_recursively

_DEF_PREFIX = 'def '
_ASYNC_DEF_PREFIX = 'async def '


def async_decorator(f):
    async def wrapper(*args, **kwargs):
        try:
            return await f(*args, **kwargs)
        except Exception as ex:
            raise ex
    return wrapper

def sync_decorator(f):
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as ex:
            raise ex
    return wrapper

def add_decorators_to_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    lines = text.split('\n')
    new_lines = ['import dtools  # DELETE ME']
    n_decorators = 0

    for i, line in enumerate(lines):
        line_strip = line.strip()
        if line_strip.startswith(_DEF_PREFIX):
            n_spaces = line.find(_DEF_PREFIX)
            new_lines.append(' ' * n_spaces + '@dtools.sync_decorator  # DELETE ME')
            n_decorators += 1
        elif line_strip.startswith(_ASYNC_DEF_PREFIX):
            n_spaces = line.find(_ASYNC_DEF_PREFIX)
            new_lines.append(' ' * n_spaces + '@dtools.async_decorator  # DELETE ME')
            n_decorators += 1
        new_lines.append(line)

    with open(file_path, 'w') as f:
        f.write('\n'.join(new_lines))

    return n_decorators

def add_decorators_to_dir(dir_path):
    for file_path in iter_file_paths_recursively(dir_path):
        if file_path.endswith('.py'):
            n_decorators = add_decorators_to_file(file_path)
            print(f'Added decorators {n_decorators} to {file_path}')