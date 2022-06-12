# dtools
A simple, lightweight library you can pip install for the purpose of improving python debugging.

### Features

To log to a log file, insert the following in your code.

```python
import dtools; dtools.p(variable, another_variable)  # p for print
...
import dtools; dtools.pp(variable)  # pp for pretty print
...
import dtools; dtools.ex(None)  # log exception using sys.exc_info
```
You can also inject decorators into your code so you can log exceptions and function calls as they happen.
```python
import dtools

@dtools.sync_decorator
def my_func(*args, **kwargs):
    raise Exception()
```
When you run the above code, the exception will be logged if you have your logging level set properly (default is 'exception', where only newly-seen exceptions are logged).

You can inject these decorators into your repo with a script.
```bash
dtools-add /path/to/repo
dtools-remove /path/to/repo
```
You can set the logging levels of your dtools configuration with a script as well. Provide the logging levels in a comma-separated list.
```bash
dtools-set-logging-levels 'function,exception'
```
Options for exception levels include 'all', 'none', 'function', and 'exception'

### FAQ

Where is it logged?

- dtools creates `~/dtools` and saves a `config.json` file there which maps where dtools is stored to a dictionary. This dictionary stores where it logs as well as the logging level, which can be changed easily.

Why not use sys.setprofile instead of injecting decorators?

- Answer: According to https://stackoverflow.com/questions/59088671/hooking-every-function-call-in-python, it is not possible to distinguish exceptions from returning None. This is the best solution I can come up with. It's hacky, but it works.
