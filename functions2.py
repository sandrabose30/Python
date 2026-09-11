# lambda function is an anonymous function
# lambda arguments : expression
# in a single line
# simple functions can only use

# def square(n):
#     return n ** 2
# print(square(5))
#     ABOVE PROGRAM WHICH IS SAME BY LAMBDA FUNCTION

# z= lambda x : x**2
# print(z(5))
# s3 = lambda x,y,z : x+y+z
# print(s3(2,3,4))

# # area of a circle
# import math
# z= lambda r : 3.14 * r**2
# print(z(5))
# area of a triangle
# z=lambda b, h : (b*h)/2
# print(z(5,10))
# square root of a number
# z=lambda x:x**5
# print(z(25))
# full name of a person
# full= lambda fname, mname, lname : fname+' '+mname+' '+lname
# print(full('john','jane','mary'))
# average of 5 numbers
# avg=lambda a,b,c,d : (a+b+c+d)/4
# print(avg(1,5,9,10))
# check if a person is eligible
# check = lambda age : "eligible" if age>=18 else "not eligible"
# print(check(30))
# to vote or not
# vote = lambda age : "Can Vote" if age>=18 else "cannot vote"
# print(vote(16))

# higher order function - 2types
# when a function return an other function
# function takes a function as is argument

# Recursion (higher order function)
# To recur to go back
# when a function calls itself
#limit

# def hello():
#     print("Hello World")
#     return hello()
#         print("Hello World")
#         return hello()
#             print("Hello World")
#             return hello()
#                     print("Hello World")
#                     return hello()
# hello()
# eg recursive
# def counttozero(n):
#     print(n)
#     return counttozero(n)
#
# counttozero(10)
#
# def counttozero0(n):
#     print(n)
#     return counttozero0(n-1)
#
# counttozero0(10)

# def counttozeroo(n):
#     print(n)
#     if n == 0:
#         return
#     return counttozeroo(n)
#
# counttozeroo(5)

# def counttozeroo(n):
#     print(n)
#     if 5 == 0:
#         return
#     return counttozeroo(n)
#
# counttozeroo(5)

# def counttozeroo(n):
#     print(n)
#     if 5 == 0:
#         return
#     return counttozeroo(n-1)
#
# counttozeroo(5)

#sum by recursion

# def counttozeroo(n):
#     if n == 0:
#         return 0
#     return n + counttozeroo(n-1)
#
# print(counttozeroo(5))

# if n = 5, ==> 5+ counttozeroo(4)
# counttozero(4) ==> 4+counttozeroo(3) so on , at last 5+4+3+2+1+0

#factorial by recursion
# def counttozeroo(n):
#     if n == 1:
#         return 1
#     return n * counttozeroo(n-1)
#
# print(counttozeroo(4))

#task
# Fibonacci number series using recursion in github add
# def counttozeroo(n):
#     if n <=1:
#         return n
#     else:
#         return counttozeroo(n-1) + counttozeroo(n-2)
# num_terms = 10
# if num_terms <= 0:
#     print("Please enter a positive integer.")
# else:
#     print(f"Fibonacci series ({num_terms} terms):")
#     for i in range(num_terms):
#         print(counttozeroo(i), end=" ")
