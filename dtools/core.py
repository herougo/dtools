import pdb
import os
import sys
import inspect
import traceback
from pprint import pformat
from dtools.logger import LOGGER


FUNCTION_NAMES = {
    'pp', 'p', '_maybe_print', 'ex'
}

def _get_last_non_dtools_function_on_stack(function_names=None):
    if function_names is None:
        function_names = FUNCTION_NAMES
    inspect_index = 1
    stack = inspect.stack()
    while stack[inspect_index].function in function_names:
        inspect_index += 1
    return stack[inspect_index].function


def pp(*args):
    fn_name = _get_last_non_dtools_function_on_stack()
    LOGGER.info('FUNCTION PRINT: ' + fn_name)
    for arg in args:
        text = pformat(arg)
        LOGGER.info(text)

def p(*args):
    fn_name = _get_last_non_dtools_function_on_stack()
    LOGGER.info('FUNCTION PRINT: ' + fn_name)
    for arg in args:
        LOGGER.info(str(arg))

def _maybe_print(variables, pretty_print):
    if variables:
        if pretty_print:
            pp(variables)
        else:
            p(variables)

def ex(local_variables=None, pretty_print=True):
    _maybe_print(local_variables, pretty_print)
    info = sys.exc_info()
    traceback.print_exception(*info)


''' Not used
def set_trace(local_variables=None, pretty_print=True):
    _maybe_print(local_variables, pretty_print)
    print('Press r to return from the dtools function call')
    pdb.set_trace()

def _old_ex():
    info = sys.exc_info()
    fname = os.path.split(info[2].tb_frame.f_code.co_filename)[1]
    print(info[0], info[1], fname, info[2].tb_lineno)
    traceback.print_tb(info[2])

def ex_and_set_trace(local_variables=None, pretty_print=True):
    _maybe_print(local_variables, pretty_print)
    ex()
    print('Press r to return from the dtools function call')
    pdb.set_trace()
'''