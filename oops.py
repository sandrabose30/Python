# object oriented programing

# object
# attributes - defines an object - variable
# behaviours - what an object - function
# methods - functions inside the class

# class
# blueprint to create object

# class Car: #car class
#     def start(): #start behavior
#         print("car can start")
#     def stop():
#         print("car can stop")

# car1 = Car #car1 object
# car1.start()
# car1.stop()
# car2 = Car #car2 object
# car3 = Car #car3 object

# class Bike:
#     def start():
#         print("bike can start")
#     def stop():
#         print("bike can stop")

# b1 = Bike
# b1.start()
# b1.stop()

# Constructor - __init__()

# class Car:
#     def __init__(self,name,color):
#         #class vechit object create cheunnath appo init automatacally
#         # called then which object called to identify which object used self used
#         self.name = name
#         self.color = color
#     def start(self):
#         print(f"{self.name} is running")
#     def stop(self):
#         print(f"{self.name} is stopped")

# class Pen:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def write(self):
#         print(f"{self.name} is in the {self.color} color")
#
# pen1=Pen("Lexii", "blue")
# pen1.write()
#
# pen2=Pen("Doms", "red")
# pen2.write()

#create a class student
# with 6 attributes name,m1,m2,m3,m4,m5
# methods sum_of_marks, average of marks, display

class Student():
    def __init__(self, name, mark1,mark2,mark3,mark4,mark5):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.mark4 = mark4
        self.mark5 = mark5
    def sum_of_marks(self):
        return (self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5)
    def average_of_marks(self):
        return (self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5) / 5
    def display(self):
        print(f"{self.name} with each subject marks : {self.mark1}, {self.mark2}, {self.mark3}, {self.mark4}, {self.mark5} has a total sum of marks: {self.sum_of_marks()}, with an average marks: {self.average_of_marks()}")

student1 = Student("John",50,20,89,79,65)
student1.display()
print(student1.sum_of_marks())
print(student1.average_of_marks())

