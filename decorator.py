# A decorator is a function that adds extra functionality to another function
# without changing its original code.

# example:
#
# Original function = gift
# Decorator = wrapping
# The gift is still there, but something extra has been added around it.


# def decorator(fun):
#     def wrapper():
#         print("Good morning")
#         fun()
#     return wrapper
#
#
# @decorator
# def hello():
#     print("Hello Hari")
#
# @decorator
# def goodbye():
#     print("Good bye")
#
#
# hello()

# Create a decorator that calculates and displays
# the execution time of a function using the time module.

# import time
#
# def totaltime(fun):
#     def wrapper():
#         start = time.time()
#         fun()
#         end = time.time()
#         print("Total time:", end - start)
#     return wrapper
#
#
# @totaltime
# def numbers():
#     for i in range(1, 5):
#         print(i)
#         time.sleep(1)
#
# numbers()

# import time
#
# score = 0
#
# print("You have 10 seconds!")
# start = time.time()
#
# print("\nWhat is name of ironman?")
# print("a. Steve Rogers")
# print("b. Tony Stark")
# print("c. Nick Fury")
#
# answer = input("Enter option: ")
#
# end = time.time()
#
# if end - start <= 10:
#     if answer == "b":
#         score += 1
#         print("Correct!")
#     else:
#         print("Wrong!")
# else:
#     print("Time's up!")
#
# print("Score =", score)
