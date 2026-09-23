
# Q) plot the points on a cartesian plane which has 2 coordinates
# x and y do the following
# 1. define a class point. its instance should have 2
# attributes x and y default value must be zero

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def cartepoints(self):
#         print (f"Point(x={self.x}, y={self.y})")
# p1=Point()
# p2=Point(3,5)
# p1.cartepoints()
# p2.cartepoints()

# 2. define an instance method move()
# when called it will set x,y values to zero (ie it
# will set the points to origin(0,0)))
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def reset(self):
#         self.x = 0
#         self.y = 0
#
# p1=Point()
# print(p1.x,p1.y)
# p1.reset()

# 3.define an method move()
# this should change the values of x and y
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def reset(self):
#         self.x = 0
#         self.y = 0
#     def move(self, a,b):
#         self.x = a
#         self.y = b
#
# p1=Point()
# print(p1.x,p1.y)
# p1.reset()
# p1.move(5,6)
# print(p1.x,p1.y)

# 4. use this move method to update reset() method
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#     def reset(self):
#         self.x = 0
#         self.y = 0
#     def move(self, a,b):
#         self.x = a
#         self.y = b
#     def resetmove(self):
#         self.move(0, 0)
#
# p1=Point()
# print(p1.x,p1.y)
# p1.reset()
# p1.move(5,6)
# print(p1.x,p1.y)
# p1.resetmove()
# print(p1.x,p1.y)

# 5. define 2 methods xmove and ymove this should move the values of x and y separately
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def cartepoints(self):
        print(f"Point(x={self.x}, y={self.y})")
    def reset(self):
        self.x = 0
        self.y = 0
    def move(self, a,b):
        self.x = a
        self.y = b
    def resetmove(self):
        self.move(0, 0)
    def xmove(self, a):
        self.x = a
    def ymove(self, b):
        self.y = b

p1=Point()
print(p1.x,p1.y)
p1.reset()
p1.move(5,6)
print(p1.x,p1.y)
p1.resetmove()
print(p1.x,p1.y)
p1.xmove(50)
p1.cartepoints()
p1.ymove(99)
p1.cartepoints()