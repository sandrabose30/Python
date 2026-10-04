# text based file
# open() - to open (function)
# to access a file
# file1 =open("toreadcontent.txt","r")
# print(file1) # object
# print(file1.read())
# file1.close()

# overwrite

# file1 =open("toreadcontent.txt","w")
# file1.write("Iam fine") #overwrite access while add "w"
# # file1.close()
#
# add lines

# file1 =open("toreadcontent.txt","a")
# file1.write("\nhi bro") #append access while add "a"
# file1.close()
# file1 =open("toreadcontent.txt","a")
# for i in range(1,20):
#     file1.write("\nhumm") #append access while add "a"
# file1.close()


# With function

# with open("Doom.txt","r") as file:
#     print(file.read())
#
# with open("Doom.txt","w") as file:
#     file.write("Hello World")
#
# with open("Doom.txt","a") as file:
#     file.write("\nHello Doom")

# import os
#
# os.mkdir("Alter")
# os.rename("Alter","Alter ego")
# os.remove("Alter ego")

# IMP = \\ consider as \

# path = "C:\\Users\\harig\\OneDrive\\Desktop\\EGO.txt"
#
# if os.path.exists(path):
#     if os.path.isdir(path):
#         print("Folder exists")
#     elif os.path.isfile(path):
#         print("File exists")

# 1. os.path.isdir()
#
# Checks whether the given path is a directory.
#
# 2. os.path.isfile()
#
# Checks whether the given path is a file.

# exceptional handling

# try:
#     a= 5
#     b= 3
#     print(a / b)
#
# except Exception as e:
#     print(e)

# try:
#     a= int(input("Enter a number: "))
#     b= 10
#     print(a/b)
#
# except ValueError:
#     print("Check your value")
# except TypeError:
#     print("Check your type")
# except ZeroDivisionError:
#     print("Division Error")
# finally:    #not must
#     print("This will be printed")


# Raise error

# class myerror(Exception):
#     pass
#
# age = 10
#
# if age >= 18:
#     raise myerror("Age should be less than 18")




