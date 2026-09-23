
#inheritance
# class person1:
#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def read(self):
#         print("person can read")
#
# class person2():
#     def __init__(self):
#         pass
#     def run(self):
#         print("person can run")
#     def jump(self):
#         print("person can jump")

# p2 = person2()
# p2.run()
# p2.jump()

#multi level inheritance

# class person1:
#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def read(self):
#         print("person can read")
#     def speak(self):#method overriding
#         print("person1 can speak")
#
# class person2(person1):
#     def __init__(self):
#         pass
#     def run(self):
#         print("person can run")
#     def jump(self):
#         print("person can jump")
#     def speak(self):#method overriding
#         print("person2 can speak")
#
# class person3(person2):
#     def __init__(self):
#         pass
#     def fly(self):
#         print("person can fly")
#     def swim(self):
#         print("person can swim")
#     def speak(self):#method overriding
#         print("person3 can speak")
#
# class person4(person3):
#     def __init__(self):
#         pass
#     def eat(self):
#         print("person can eat")
#     def drink(self):
#         print("person can drink")
#     def speak(self): #method overriding
#         print("person4 can speak")
#         super().speak()

# p4 = person4()
# p4.walk()
# p4.speak()

#method overriding - same method in parent class and
# child class output will overriding and got output of child class

# Multiple inheritance
#
# class person1:
#     def __init__(self):
#         pass
#     def walk(self):
#         print("person can walk")
#     def read(self):
#         print("person can read")
#     def speak(self):#method overriding
#         print("person1 can speak")
#
# class person2:
#     def __init__(self):
#         pass
#     def run(self):
#         print("person can run")
#     def jump(self):
#         print("person can jump")
#     def speak(self):#method overriding
#         print("person2 can speak")
#
# class person3:
#     def __init__(self):
#         pass
#     def fly(self):
#         print("person can fly")
#     def swim(self):
#         print("person can swim")
#     def speak(self):#method overriding
#         print("person3 can speak")
#
# class person4(person2, person3,person1): #MRO -method resolution order
#     def __init__(self):
#         pass
#     def eat(self):
#         print("person can eat")
#     def drink(self):
#         print("person can drink")
#
# p4 = person4()
# p4.speak()
