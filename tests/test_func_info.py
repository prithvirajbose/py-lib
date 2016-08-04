"""
    Shows applicatio of higher order functions and
    closures in decorators.
"""

import sys
sys.path.insert(0, '../')

from lib.db_utils import func_info

@func_info # Using the decorator syntax
def print_names(names, **kwargs):
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
    print call(3, 9)

    '''
    You can write like this, but think about readability as well!
        print func_info(lambda l, b: l * b)(2, 9)
    '''
