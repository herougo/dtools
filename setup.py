from setuptools import setup, find_packages

setup(
    name='dtools',
    version='1.0',
    description='A simple, lightweight library you can pip install for the purpose of improving python debugging.',
    author='',
    author_email='',
    url='',
    packages=['dtools', 'dtools.scripts'],
    entry_points = {
        'console_scripts': [
            'dtools-add=dtools.scripts.add_decorators:main',
            'dtools-remove=dtools.scripts.remove_decorators:main'
        ]
    }
)