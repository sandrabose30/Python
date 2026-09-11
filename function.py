# functions
# reusability, block of code which is executed when it is
# DRY Principle
# def functionname(<parameters>):
#     code to be executed

# def hello():
#     print("Hello Good Morning")
# a=hello()
# print(a)

# hello()
# hello()
# mohan = print
# mohan("print")

# python inbuilt function
# print()
# list.append()
# list.remove()
# len()

# arguments
# value to be passed to a function
# parameters values mapped in the function
# def add(a,b):
#     print(a+b)
# Types - 1. Positional arguments
# add(8,6)
# 2. Keyword argument
# add(b=5,a=6)
# while set a default value
# def addd(a=0,b=0):
#     print(a+b)
# addd(10,5)
# addd(a=6,b=3)

# return statements
# after return statement function terminated
# def add(a,b):
#     return a+b
# add(1,3)
# print(add(1,3))

#Create a basic Calculator using function

# print("Welcome to Basic Calculator")
#
# def addition(a,b):
#     return a + b
# def subtraction(a,b):
#     return a - b
# def multiplication(a,b):
#     return a * b
# def division(a,b):
#     return a / b
#
# print(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit")
# operation = int(input("What operation do you want to do? : "))
#
# if operation == 1:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     print(addition(a,b))
# elif operation == 2:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     print(subtraction(a,b))
# elif operation == 3:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     print(multiplication(a,b))
# elif operation == 4:
#     a=int(input("Enter the first number: "))
#     b=int(input("Enter the second number: "))
#     print(division(a,b))
# elif operation == 5:
#     print("Exit")
# else:
#     print("Invalid operation")

# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
#
# def main():
#     print("Welcome to Simple Calculator")
#     while True:
#         print("What do you want to do?")
#         choice=int(input("Enter your choice\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5.Exit\n Choice==> "))
#         x=int(input("Enter a number: "))
#         y=int(input("Enter another number: "))
#         if choice==1:
#             print(f"sum:{add(x,y)}")
#         elif choice==2:
#             print(f"difference is :{subtract(x,y)}")
#         elif choice==3:
#             print(f"product is :{multiply(x,y)}")
#         elif choice==4:
#             print(f"result is:{divide(x,y)}")
#         elif choice==5:
#             break
#         else:
#             print("Invalid choice")
# main()
#
# HW
# factorial of a number
# def factorial(n):
#     if n < 0:
#         return "Factorial is not defined for negative numbers."
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(6))

# age calculator
# from datetime import date
# def calculate_age(birth_date):
#     """
#     Calculates age in years given a birth_date
#     as a 'YYYY-MM-DD' string or a datetime.date object.
#     """
#     if isinstance(birth_date, str):
#         birth_date = date.fromisoformat(birth_date)
#
#     today = date.today()
#
#     # Calculate initial year difference
#     age = today.year - birth_date.year
#
#     # Adjust if the birthday hasn't happened yet this year
#     if (today.month, today.day) < (birth_date.month, birth_date.day):
#         age -= 1
#
#     return age
#
# print(calculate_age("2001-05-15"))

# bmi calculator

# def calculate_bmi(weight_kg, height_m):
#     """
#     Calculates BMI given weight in kilograms and height in meters.
#     """
#     if height_m <= 0 or weight_kg <= 0:
#         return "Weight and height must be greater than zero."
#
#     # BMI formula: weight (kg) / [height (m)]^2
#     bmi = weight_kg / (height_m ** 2)
#
#     # Determine WHO weight category
#     if bmi < 18.5:
#         category = "Underweight"
#     elif 18.5 <= bmi < 25:
#         category = "Normal weight"
#     elif 25 <= bmi < 30:
#         category = "Overweight"
#     else:
#         category = "Obesity"
#
#     return round(bmi, 2), category
#
#
# bmi_value, status = calculate_bmi(70, 1.75)
# print(f"BMI: {bmi_value} ({status})")


def calculate_bmi(weight_lbs, height_in):
    if height_in <= 0 or weight_lbs <= 0:
        return "Weight and height must be greater than zero."

    bmi = (weight_lbs / (height_in ** 2)) * 703
    return round(bmi, 2)

