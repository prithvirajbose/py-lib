# py-lib
Reusable libraries for Python. Tested on 2.7.12 and 3.5.2.  

# Contents
- **db_utils.py**: Module containing function and class information decorator that prints the arguments (positional, variable, keywords) along with their types and values.

- **func_info**
A trace function to trace the entry, exit and parameters for functions. 
Use this to trace functions.

	'''python
		@func_info
		def function_to_trace(*args, **kwargs):
			...
'''

- **ClassInfoMetaclass**: 
A metaclass to trace the entry, exit and parameters for class methods.
Use this to trace class methods.

    '''python  
		#for 2.7.x  
		class ClassToTrace(object):  
			__metaclass__ = ClassInfoMetaclass  	
			...  
	'''

    '''python  
		#for 3.5.x  
		class ClassToTrace(object, metaclass = ClassInfoMetaclass):  
			...  
	'''  
 
 
 