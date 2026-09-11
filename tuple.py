#TUPLE - collection of data
# tuple()
# * Ordered
# * tuple can have any element in any size
# * indexed
# * duplicate values can add
# * immutable - ones created it doesnt allow change properties
# * not a dynamic - cant append, extend, pop, insert , remove
# tuple=(1,2,3,4,5,'hello')
# print(tuple)
# print(tuple[-1])
from re import search

# 1. print tuple elements
# fruits=("apple","banana","orange")
# print(fruits)
# 2. count total elements
# t=(10,20,30,40,50)
# print(len(t))
# 3.find maximum elements
# t=(12,45,23,67,34)
# max_element=max(t)
# print(max_element)
# 4.sum of tuple elements
# t=(5,10,15,20)
# sum=sum(t)
# print(sum)
# 5.search an element
t=(10,20,30,40)
x=int(input("enter the searching number:"))
if x in t:
    print(x)
else:
    print("Not found")

