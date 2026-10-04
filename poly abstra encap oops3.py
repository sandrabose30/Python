# polymorphism
# Polymorphism means:
#
# One thing can have many forms.
#
# In Python, polymorphism allows the same method or function name to behave differently depending on the object.
#
# Simple real-life example
#
# Think about the word "sound":
#
# Dog → bark
# Cat → meow
# Cow → moo
#
# They all have a sound() method, but each one behaves differently.

# class Dog:
#     def sound(self):
#         print("Dog barks")
#
#
# class Cat:
#     def sound(self):
#         print("Cat meows")
#
#
# dog = Dog()
# cat = Cat()
#
# dog.sound()
# cat.sound()
#
# Output:
#
# Dog barks
# Cat meows
#
# Here, both classes have the same method name: sound()
#
# But the method behaves differently for each object.
#
# That's polymorphism.
#
#
# What is Operator Overloading?
#
# Operator overloading means giving a special meaning to an operator such as:
# +   -   *   /   ==
#
# depending on the objects being used.



# poly = many
# morph = forms

# operator overloading
# method overloading
# method ovrriding

# operator overloading
# class Student:
#     def __init__(self, mark1,mark2):
#         self.mark1 = mark1
#         self.mark2 = mark2
#     def __add__(self, otr):
#         return "mohan"
#
# s1=Student(8,10)
# s2=Student(7,9)
# print(s1+s2) #error
# print(s2+s1) #overloaded mohan so return out mohan so not adding

# add by overloading
# class Student:
#     def __init__(self, mark1,mark2):
#         self.mark1 = mark1
#         self.mark2 = mark2
#     def __add__(self, otr):
#         t1 = self.mark1 + self.mark2
#         t2 = otr.mark1 + otr.mark2
#         return t1,t2
#
# s1=Student(8,10)
# s2=Student(7,9)
# print(s1+s2)

# subtract by overloading
# mult by overloading
# trudiv by overloading
# gt by overloading

# class Student:
#     def __init__(self, mark1,mark2):
#         self.mark1 = mark1
#         self.mark2 = mark2
#     def __add__(self, otr):
#         t1 = self.mark1 + self.mark2
#         t2 = otr.mark1 + otr.mark2
#         return t1,t2
#     def __sub__(self, otr):
#         t1 = self.mark1 - self.mark2
#         t2 = otr.mark1 - otr.mark2
#         return t1,t2
#     def __mul__(self, otr):
#         t1 = self.mark1 * self.mark2
#         t2 = otr.mark1 * otr.mark2
#         return t1,t2
#     def __truediv__(self, otr):
#         t1 = self.mark1 / self.mark2
#         t2 = otr.mark1 / otr.mark2
#     def __gt__(self, otr):
#         t1 = self.mark1 > self.mark2
#         t2 = otr.mark1 > otr.mark2
#         return t1,t2
#
# s1=Student(8,10)
# s2=Student(7,9)
# print(s1+s2)
# print(s1-s2)
# print(s1*s2)
# print(s1/s2)

#method overloading - by diff no of attributes with same method name we call
# but ih python not possible
# class A:
#     def __init__(self):
#         pass
#     def hello(self,a,b):
#         print(a,b)
#     def hello(self,a,b,c,d):
#         print(a,b,c,d)
# aa = A()
# # aa.hello(2,5)
# aa.hello(3,4,4,8)

# METHOD OVERRIDING
# class A:
#     def __init__(self):
#         pass
#     def hello(self):
#         print("A says hello")
# class B:
#     def hello(self):
#         print("B says hello")
# print(A.hello())
# print(B.hello())

#abstraction - data hiding method, through inheritancce to acheive abstraction
# base(inside base abstract method) and derived class ind
# Abstraction in Python OOP

#Abstraction means hiding unnecessary internal details and showing only what the user needs.

# Real-life example:
#
# Think about a car.
#
# When you drive a car, you use:
#
# start()
# accelerate()
# brake()
#
# You don't need to know exactly how the engine internally works.
#
# That is abstraction — you use the functionality without worrying about the internal implementation.
#
#Example

# from abc import ABC, abstractmethod
# class Animal:
#     def __init__(self):
#         pass
#     @abstractmethod
#     def makes_sound(self):
#         print("animal makes sound")
# class Dog(Animal):
#     def __init__(self):
#         pass
#     def makes_sound(self):
#         print("woff woff")
# d=Dog()
# d.makes_sound()
#
# abc → Python's built-in module for Abstract Base Classes
# ABC → class used to create an abstract class
# abstractmethod → decorator that makes a method compulsory for child classes

# Encapsulation
# Encapsulation in Python OOP
#
# Encapsulation means wrapping data (variables) and methods (functions)
# together inside a class and controlling how the data can be accessed.
#
# In simple words:
#
# Encapsulation = Protecting data inside a class.

# Main purpose of encapsulation:
# Data hiding + controlled access to data.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# student1 = Student("Hari", 20)
#
# print(student1.name)
# student1.age = 25

# Here, name and age are inside the class, so this is encapsulation
# (data + methods grouped inside a class). But the data is freely accessible.

# In order to control the Access, we need to use the Access modifiers


# Access modifiers
#
# Access modifiers control how class attributes and methods are intended to be accessed.

# Unlike Java or C++, Python does not strictly enforce public, protected,
# and private; it mainly uses naming conventions and name mangling.
#
# Modifier	 Syntax	                Meaning
#
# Public	     self.name	            "Everyone can use it."
# Protected	     self._name	            "This is mainly for the class and child classes."
# Private	     self.__name	        "This is meant to stay inside the class."

# 1. Public — self.name
#
# Public means anyone can access it.
#
# class Student:
#     def __init__(self):
#         self.name = "Hari"   # Public
#
#
# student = Student()
#
# print(student.name)
#
# You can access name:
#
# Inside the class
# In a child class
# Outside the class
#
# So:
# Public = Everyone can use it.

# 2. Protected — self._name
#
# Protected uses one underscore _.
#
# class Student:
#     def __init__(self):
#         self._name = "Hari"   # Protected
#
#
# student = Student()
#
# print(student._name)
#
# Output:Hari
#
# Notice something important: Python still allows you to access _name from outside.
#
# The _ is mainly a warning/convention saying:
#
# This is intended for the class and its child classes.
# Don't access it directly unless you know what youre doing.

# So:
# Protected = Mainly for the class and child classes.

# 3. Private — self.__name
#
# Private uses two underscores __.
#
# class Student:
#     def __init__(self):
#         self.__name = "Hari"   # Private
#
#     def show(self):
#         print(self.__name)
#
#
# student = Student()
#
# student.show()
#
# Output: Hari
#
# But if you try:
#
# print(student.__name)
#
# you get an error because Python's name mangling changes the internal name.
#
# The important idea is:
#
# Private = Intended to be accessed only inside the class.
#
# SIMPLE:
#
# name       → Public     → Everyone
# _name      → Protected  → Class + Children
# __name     → Private    → Class only
