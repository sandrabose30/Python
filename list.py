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
