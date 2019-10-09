import Config.GlobalDecorators as gd

def msg_printer(**kwargs):
    print("debug ->" , kwargs["DEBUG"])


def msg_printer2():
    print("debug ->" , )

import sys
modname = globals()['__name__']
print(modname)
print(gd.__name__)
module = sys.modules
gd.DecoratorClass().start_wrapper_decoration(module[modname])
msg_printer()  # prints 'Message'
msg_printer2()