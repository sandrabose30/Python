# list = [1,2,3,4,5]
# string = "hello"
# tuple = (1,2,3,4,5)
# for i in list:
#     print(i)
#     break # terminate from the current loop.
# for i in string:
#     print(i)
#     break
# for i in tuple:
#     print(i)
#     continue #skip the current loop and next iteration
# for i in list:
#     if i==3:
#         continue
#     print(i)
from collections import OrderedDict

#print numbers from 1 to 20 and skip multiple of 5
# for i in range(1,19):
#     if i % 5 == 0:
#         continue
#     print(i)
# for i in range(10,0,-1): #10 to 0 vare 1 vech decrement
#     print(i)
# for i in range(0,10,2):
#     print(i)

# for i in range(1,11):
#     print(i)

# 1.print numbers from 1 to 100
# for i in range(1,101):
#     print(i)
# 2.find sum of first 10numbers
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)
# 3.print odd and even numbers from 1 to 20 numbers
# for i in range(1,21):
#    if i % 2 == 0:
#       print(i," is even")
#    else:
#       print(i," is odd")
# 1. print all elements in a list
# num= [10,20,30,40,50]
# for num in num:
#    print(num)
# 2. find the sum of list elements
# numbers= [10,20,30,40]
# sum=0
# for num in numbers:
#    sum=sum+num
# print(sum)
# 3.find the largest element
# numbers= [10,20,30,40]
# max_value=0
# for num in numbers:
#    if num>max_value:
#       max_value=num
# print("Largest number is ",max_value)
# 4.count even numbers
# numbers= [1,2,3,4,5,6]
# count=0
# for num in numbers:
#    if num % 2 == 0:
#       count=count+1
# print(count)
# 5.print list in reverse
# numbers=[10,20,30,40,50]
# for num in reversed(numbers):
#    print(num)
# or
# numbers=[10,20,30,40,50]
# reverse_num = []
# for num in numbers:
#    reverse_num = [num]+reverse_num
# for number in reverse_num:
#    print(number)

# 1.Add digits of a number
#    Eg: input 12345
#    output 15
# num=int(input("Enter a number: "))
# num=12345
# sum=0
# for i in str(num):
#     sum=sum+int(i)
# print(sum)
# # 2.Reverse of a number
# num = int(input("Enter a number: "))
# reverse =""
# for i in str(num):
#     reverse = i + reverse
# print(reverse)
#
# # 3.Find the Fibanocci series up to 100.
# a, b = 0, 1
#
# print("Fibonacci series up to 100:")
# print(a, end=" ")
# for _ in range(100):
#     c = a + b
#     if c > 100:
#         break
#     print(c, end=" ")
#     a = b
#     b = c
# 4.Find Factorial of a number
# number = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(f"Factorial of {number} is {factorial}")

# 5.check whether a number is Prime or not
num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break