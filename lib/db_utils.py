"""
Debug utilities.
"""
def func_info(f):
    """
    A generic trace function to trace the entry, exit
    and parameters to a function.
    """
    def wrapper(*args, **kwargs):
        print '>>> trace: \'{0}\' called...'.format(f.__name__)
        
        arg_list = lambda args: 'None' if len(args) == 0 else args
        print '>>> trace: Arguments list: {0}'.format(arg_list(args))
        
        if len(args) != 0:
            for arg in args:
                print '>>> trace: (arg_type, arg_val): ({0}, {1})'\
                      .format(type(arg), arg)
        
        kwarg_list = lambda kwargs: 'None' if len(kwargs) == 0 else kwargs
        print '>>> trace: Keyword arguments list: {0}'.format(kwarg_list(kwargs))
        
        if len(kwargs) != 0:
            for k, v in kwargs.iteritems():
                print '>>> trace: (kw_key, val_type, val): ({0}, {1}, {2})'\
                      .format(k, type(v), v)

        res = f(*args, **kwargs)

        print '>>> trace: \'{0}\' returning...'.format(f.__name__)

        return res

    return wrapper
