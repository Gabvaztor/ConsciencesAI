import Config.GlobalDecorators as gd

def msg_printer(**kwargs):
    """
    Args:
        var:
        *args:
        **kwargs:
    """
    print("ads ->" , kwargs["DEBUG"])
import sys
modname = globals()['__name__']
module = sys.modules
gd.DecoratorClass().start_wrapper_decoration(module[modname])
msg_printer()  # prints 'Message'
