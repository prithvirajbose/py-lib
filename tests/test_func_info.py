"""
    Shows application of higher order functions and
    closures in decorators.
"""

import sys
sys.path.insert(1, '../')

from lib.db_utils import func_info, ClassInfoMetaclass

@func_info
def print_names(names, **kwargs):
    pass

class Test(object, metaclass = ClassInfoMetaclass):
    """
    Test class for testing class decorator.
    """ 
    def __init__(self, dummy):
        self.dummy = dummy
    
    def test(self, a, *args, **kwargs):
        pass
    
if __name__ == '__main__':
    print_names(['Benny', 'Kenny', 'Oscar'], roll = 'students')

    ''' Alternative way to decorate manually and
        to show closures at work'''
    area = lambda l, b: l * b
    call = func_info(area)
    del area
    '''Even though we delete 'area' the lambda expression contained in
        'area' is bound to the func_info.'''
    print(call(3, 9))

    '''
    You can write like this, but think about readability as well!
        print func_info(lambda l, b: l * b)(2, 9)
    '''

    t = Test(100)
    print(t.dummy)
    t.test(10, host='localhost')
    t.test(10, 20, host='localhost')
    print(t.__doc__)
    