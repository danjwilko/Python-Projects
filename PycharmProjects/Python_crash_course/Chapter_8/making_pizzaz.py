# The line import tells Python to open the file - pizza.py and copy all the functions from it into this program.
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green pepper', 'extra cheese')

"""Importing specific functions."""
# You can also import specific function from a module. The general syntax:
# from module_name import function_name

# You can also import aa many functions as you want from a module by separating each function with a comma.
# from module_name import function_0, function_1, function_2

# This is what the pizza.py file would look like if we just imported the function we're going to use.
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'pepperoni', 'mushrooms', 'green pepper', 'extra cheese')

"""Using as to give a function an Alias"""

# The name of your function were importing may conflict with a existing name being used in the program or if the
# function name is realy long.

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'pepperoni', 'mushrooms', 'green pepper', 'extra cheese')

# The general syntax for providing and alias is:
# from module_name import function_name as fn

"""Using as to give a Module an alias"""

# We can also provide an alias for a module name. Using a shorter alias can make the code more concise.

import pizza as p

# Using the alias we have p.make_pizza() rather than pizza.make_pizza().
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'pepperoni', 'mushrooms', 'green pepper', 'extra cheese')

# The general syntax for this approach is:
# import module_name as mn

"""Importing all the functions in a module"""
# We can tell Python to import every function in a module by using the asterisk (*) operator.

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'pepperoni', 'mushrooms', 'green pepper', )

# Note its always best to try an umport only the functions you want, or import the entrire module and use dot notation.
# General syntax is:
# from module_name import.

"""Styling Functions"""

# Functions should have descriptive names and these names should use lowercase letters and underscores.
# Using descriptive names helps you and others understand what your code is trying to do. Module names should also
# Follow these conventions as well.

# Every function should have a comment that explains concisely what the function does.
# The comment should appear immediately after the function definition and use a docstring format.

# If you specify a deafult value for a parameter, no spaces should e on either side of the equals sign.

# def function_name(parameter_0, parameter_1='default value')

# The same conventions should be used for keyword arguments in function calls.

# function_name(value_0, parameter_1='value')
