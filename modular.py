# multiple paradigms
#
# structural programing
# functional programing
# modular programing
# object oriented programing
# procedural programing

# modular programing
# create a module for mostly function in one file and import whenever needed

# import modularconnect
# from modularconnect import * #all import
# from modularconnect import factorial, add
from modularconnect import name as name1
name = "mohan"
print(name)
print(name1)

# Modularity in Python is dividing a program into separate files (modules)
# and using import to reuse their code.

# import Modularity1
#
# print(Modularity1.add(5, 5))
# print(Modularity1.factorial(6))

# Modularity1.py
#   ↓
# contains functions
#   ↓
# import Modularity1
#   ↓
# use Modularity1.add()
# use Modularity1.factorial()

# from ... import
#
# from Modularity1 import add
#
# print(add(5, 5))
#
# from Modularity1 import factorial
#
# print(factorial(6))
#
# Instead of importing the complete module, we can import a specific function
#
# Importing Multiple Functions
#
# We can import more than one function:
#
# from Modularity1 import add, factorial
#
# print(add(5, 5))
# print(factorial(6))
#
# This imports only add and factorial.


# from Modularity1 import *
#
# c = [2, 3, 4, 5, 6, 9]
#
# print(add(5, 5))
# print(factorial(6))
#
# The * means “import everything” from that module.

# from Modularity1 import hello as h
#
# h()

# from Modularity1 import bye as b
#
# b()

# Why use as?
#
# Mainly to:
#
# Give a shorter name
# Avoid name conflicts
# Make code easier to write

# from md import add    =   # import one
# from md import *      =   # import everything
# from md import add as a = # import one with a new name
