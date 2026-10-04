#datatypes
#LIST (which is a collection of data)

# list = [1, "meeny", 5555555, [1,2,5]]
# * Ordered
# * list can have any element in any size
# * indexed
# print(list[1])
# print(list[2])
# print(list[5])
# a=[21,25,100,70,23,45,52]
# print(a[3:6])

# a =["apple", "banana","mango","grape", "watermelon", "pappaya"]
# print(a[2:5])
# print(a[::2])
# print(a[:2])
# print(a[-1])
# print(a[-2:])
# print(a[4])
# print(a[-4])
# print(a[:3])
# print(a[::-1])

# * Mutable - increase size , shrink, values change
# a=[1,5,6,10]
# a[2]=11
# * nested

#reverse the name
# name = "SANDRA"
# print(name[::-1])
#
# list = ["orange", "apple", "banana", "GRAPE", "orange", "watermelon"]
# print(list) #1.print all items in the list
# print(list[0:4]) #2. orange, apple , banana, GRAPE
# print(list[-1]) #3.watermelon
# print(list[-2:]) #4. orange, watermelon
# print(list[::-1]) #5.reverse the list

#inbuilt methods
# 1.Append methods - append() - add one value to the list
# 2. extend() - add iterable values to the list
# 3. insert() - add elements at specified position to the list
# 4. remove() - remove elements by value
# 5. pop() - remove elements by index value

# list= [10,20,30,40,50]
# list.append('hello')
# list.append([100,200])
# print(list)
#
# list= [10,20,30,40,50]
# list.extend('hello')
# list.extend([100,200])
# list.extend([300,400,500,"mohan", 600])
# print(list)

# list= [10,20,30,40,50]
# list.insert(2, "hello")
# print(list)
# list.insert(3,200)
# print(list)
# list.insert(4,"mohan")
# print(list)

# list= [10,20,30,40,50]
# list.remove(30)
# print(list)

# list= [10,20,30,40,50]
# list.pop()
# print(list)
# list.pop(2)
# print(list)

# List comprehension is a short and simple way to create a list using a for loop.

# b = [i for i in range(1, 101)]
# print(b)

#1. range(1, 101)

# This generates numbers from 1 to 100.

# 2. for i in range(1, 101)
# So i becomes:
#
# 1
# 2
# 3
# ...
# 100

# 3. [i ...]
# The i before for tells Python what to put into the list.
#
# So:
# [i for i in range(1, 101)]

# means:
# "Take every i from 1 to 100 and put it into a list."

# numbers = [i for i in range(1, 6)]
#
# print(numbers)
#
# c = [i for i in range(1, 1001) if i % 2 == 0]
# print(c)

# We can also perform calculations
#
# For example, create squares:
#
# squares = [i * i for i in range(1, 6)]
#
# print(squares)
#
# 1. Create a list of squares of numbers from the first 100 numbers
#
# squares = [i * i for i in range(1, 101)]
#
# print(squares)
#
# 2. From a list of 100 numbers, create a list of numbers divisible by 5 and 3
#
# numbers = [i for i in range(1, 101)]
#
# result = [i for i in numbers if i % 5 == 0 and i % 3 == 0]
#
# print(result)
#
# 3. Create a list of numbers that have the digit 6 in them from a range of 1000 numbers
#
# numbers = [i for i in range(1, 1001) if "6" in str(i)]
#
# print(numbers)

# Easy pattern to remember:
# [what_you_want for i in range(...) if condition]

