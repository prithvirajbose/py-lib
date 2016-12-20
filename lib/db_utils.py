"""
Debug utilities.
"""

from functools import wraps, update_wrapper

def func_info(f):
    """
    A generic trace function to trace the entry, exit
    and parameters for functions.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        _analyse_args(f, *args, **kwargs)
        return f(*args, **kwargs)
    return wrapper

def _analyse_args(f, *args, **kwargs):
    print('>>> trace: \'{0}\' called...'.format(f.__name__))

    arg_list = lambda args: 'None' if len(args) == 0 else args

    print('>>> trace: Arguments list: {0}'.format(arg_list(args)))
        
    if len(args) != 0:
        for arg in args:
            print('>>> trace: (arg_type, arg_val): ({0}, {1})'\
                  .format(type(arg), arg))

    kwarg_list = lambda kwargs: 'None' if len(kwargs) == 0 else kwargs
    print('>>> trace: Keyword arguments list: {0}'.format(kwarg_list(kwargs)))

    if len(kwargs) != 0:
        for k, v in kwargs.items():
            print('>>> trace: (kw_key, val_type, val): ({0}, {1}, {2})'\
                  .format(k, type(v), v))

    print('>>> trace: \'{0}\' returning...'.format(f.__name__))


def class_info(cls):
    """
    A generic trace function to trace the entry, exit
    and parameters for class methods.
    """
    class WrapperCls(object):
        def __init__(self, *args, **kwargs):
            self.__wrapper = cls(*args, **kwargs)
            # Wrapping the enclosing class with the target class.
            update_wrapper(self, self.__wrapper)

        def __getattr__(self, attrib):
            obj = getattr(self.__wrapper, attrib)
            if callable(obj):
                return func_info(obj)
            return obj

    return WrapperCls



