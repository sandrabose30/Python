# A generator is a function that gives you values one by one
# instead of giving all values at once.
#
# A generator uses the keyword yield.

# def numbers():
#     yield 1
#     yield 2
#     yield 3
#
# for i in numbers():
#     print(i)

# You can also get the values one at a time using next().

# def numbers():
#     yield 10
#     yield 20
#     yield 30
#
# x = numbers()
#
# print(next(x))
# print(next(x))
# print(next(x))

# Why use generators?
#
# Imagine you need numbers from 1 to 1,000,000.
#
# Instead of creating all the numbers at once, a generator can give you:
#
# 1
# 2
# 3
# 4
# ...
#
# one at a time.

# import sys
#
# a = []
#
# for i in range(1, 1000001):
#     a.append(i)
#
# def million():
#     for i in range(1, 1000001):
#         yield i
#
# b = million()
#
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))


# sys is a built-in Python module.
#
# It provides information and functions related to the Python interpreter and system.

# getsizeof() tells us approximately how much memory an object itself occupies in bytes.

# import sys
#
# x = 10
#
# print(sys.getsizeof(x))
#
# It gives the size of the integer object in bytes.
