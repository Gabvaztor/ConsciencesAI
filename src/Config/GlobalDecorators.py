"""
#3FXIAp5K
"""
import time
from Config.GlobalSettings import DEBUG_MODE

import types
import functools

class DecoratorClass(object):

    def __decorate_all_in_module(self, module, decorator):
        for name in dir(module):
            obj = getattr(module, name)
            if isinstance(obj, types.FunctionType):
                setattr(module, name, decorator(obj))

    def __global_decorator(self):
        def msg_decorator(function):
            @functools.wraps(function)
            def inner_dec(*args, **kwargs):
                start = time.time()
                try:
                    return function(*args, DEBUG=DEBUG_MODE, **kwargs)
                finally:
                    method_str = str(function)
                    print("Running time method: \"" + str(method_str[10:-23]) + "\"",
                          str(time.strftime("%Hh%Mm%Ss", time.gmtime((time.time() - start)))))
            inner_dec.__name__ = function.__name__
            inner_dec.__doc__ = function.__doc__
            return inner_dec

        return msg_decorator

    def __my_decorator(self, f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(f)
            return f(*args, **kwargs)
        return wrapper

    def start_wrapper_decoration(self, module):
        self.__decorate_all_in_module(module=module, decorator=self.__global_decorator())