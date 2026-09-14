# Scope: Area in which it is recognised
# Priority in scope (order)
# Local value (L): Names defined inside the current function or method. It has the highest priority.
# Enclosing (E): Names in the local scope of any enclosing or outer functions (nested functions).
# Global (G): Names defined at the top level of a module or script file.
# Built-in (B): Names reserved by Python automatically (like print, len, int). It has the lowest priority.

# name="hari"
#
# def getname():
#     name="Mohan" # enclosing value
#     def nickname(): # local scope
#         name = "rosna"
#         print(name)
#     nickname()
# getname()
# print(name)

# Arguments and keyword arguments
# def addz(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# print(addz(3,2,5,88,6))
#
# def addz(a,b,*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# print(addz(3,55,99,6,33,552,5,88,6))

# def addz(**kwargs):
#     print(kwargs)
#
# print(addz(3,55,99,6,33,552,5,88,6))

# def fullname(*args,**kwargs):
#     name=""
#     sum = 0
#     for i in kwargs:
#         print(kwargs[i])
#         name = name + kwargs[i] + ' '
#     print(name)
#     for i in args:
#         sum = sum + i
#     print(sum)
# fullname(3,4,5,8,6,2,5,88,5,22,55,88,55,fname="robert", mname="rob")




