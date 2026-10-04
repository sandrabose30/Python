# relational database
# table store
# sql - structured query language
# eg. mysql,
# A database is a place where we store data in an organized way so that
# we can save, retrieve, update, and delete information.

#For example, instead of storing student information like this:
#
# name1 = "Hari"
# age1 = 21
# course1 = "Python"
#
# We can use like this:
#
# ID	Name	Age	Course

# 1	Hari	21	Python
# 2	Arun	22	Cyber Security
# 3	Rahul	20	Python
#
# Instead of keeping this information only in Python variables, we can store it permanently in a database.

# The database allows us to:
#
# Create data
# Read/Retrieve data
# Update data
# Delete data
#
# These are commonly called CRUD operations:

# Create → Read → Update → Delete


import sqlite3

# conn = sqlite3.connect('connectdb.db') #to connect to the db
# cursor = conn.cursor() #to interact with db

# CREATE
# cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS Student(
#     Id INTEGER,
#     Name VARCHAR(20),
#     Address TEXT
#     )
#     '''
# )
# cursor.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS Employee(
#     EmployeeId INTEGER,
#     Name VARCHAR(20),
#     Address TEXT,
#     Description TEXT
#     )
#     '''
# )

# INSERT INTO
# cursor.execute(
#     '''
#     INSERT INTO Student(Id,Name,Address)
#     VALUES(001,"Abhijith","Kuthattukulam"),
#     (002,"Subash","Kannur"),
#     (003,"Anjali","Perumbavoor")
#     '''
# )
# conn.commit()

conn = sqlite3.connect('task1.db') #to connect to the db
cursor = conn.cursor() #to interact with

# PRIMARY KEY AUTOINCREMENT
# conn.execute(
#     '''
#     CREATE TABLE IF NOT EXISTS Tasks(
#     Id INTEGER PRIMARY KEY AUTOINCREMENT,
#     TaskName VARCHAR(200),
#     TaskDescription TEXT
#     )
#     '''
# )
# conn.close()
#
def addtask():
    conn = sqlite3.connect('task1.db')
    cursor = conn.cursor()
    name = input("Enter your Task Name: ")
    Description = input("Enter your Task Description: ")
    cursor.execute(
        '''
        INSERT INTO Tasks(TaskName,TaskDescription)
        VALUES (?,?)"
        ''', (name, Description)
    )
    conn.commit()
    print("Task Added")
    conn.close()

# def main():
#     print("Welcome to the Task Management System")
#     while True:
#         ch = int(input("Enter your Choice: \n1.Add"))
#         if ch == 1:
#             addtask()
#         else:
#             print("Invalid Choice")
# main()


# # View tasks
# def viewtasks():
#     conn = sqlite3.connect("task1.db")
#     cursor = conn.cursor()
#
#     cursor.execute('''
#         SELECT * FROM tasks
#     ''')
#
#     data = cursor.fetchall() #Retrieve a list of data from the last query
#
#     print("\nTasks found ☑")
#
#     for i in data:
#         print(f"{i[0]} task --- {i[1]} task description --- {i[2]}")
#
#     conn.close()
#
# # Search task
# def searchtask():
#     conn = sqlite3.connect("task1.db")
#     cursor = conn.cursor()
#
#     t_id = int(input("Enter your task id: "))
#
#     cursor.execute(
#         "SELECT * FROM tasks WHERE id = ?",
#         (t_id,)
#     )
#
#     task = cursor.fetchone()
#
#     if task:
#         print("Task found ☑")
#         print(f"{task[0]} --- {task[1]} --- {task[2]}")
#     else:
#         print("No such task 😕")
#
#     conn.close()
#
# def edittask():
#     conn = sqlite3.connect("task1.db")
#     cursor = conn.cursor()
#
#     t_id = int(input("Enter task id: "))
#     name = input("Enter new task name: ")
#     des = input("Enter new description: ")
#
#     cursor.execute(
#         '''
#         UPDATE tasks
#         SET name = ?, description = ?
#         WHERE id = ?
#         ''',
#         (name, des, t_id)
#     )
#
#     conn.commit()
#
#     print("Task updated")
#
#     conn.close()
#
# def deletetask():
#     conn = sqlite3.connect("task1.db")
#     cursor = conn.cursor()
#
#     t_id = int(input("enter task id:-"))
#
#     ch = input("Are you sure you want to delete this task y/n:-")
#
#     if ch == "y":
#         cursor.execute(
#             "DELETE FROM tasks WHERE id = ?",
#             (t_id,)
#         )
#         conn.commit()
#
#         print("Task deleted !!!!!!!!!!!!!")
#     else:
#         print("Task not deleted !!!!!!!!!!!!")
#
#
# # Main function
# def main():
#     print("Welcome to task management system")
#
#     while True:
#         ch = int(input(
#             "Enter your choice\n"
#             "1. Add Task\n"
#             "2. View Tasks\n"
#             "3. Search Task\n"
#             "4. Update Task\n"
#             "5. Delete Task\n"
#             "6. Quit\n"
#         ))
#
#         if ch == 1:
#             addtask()
#
#         elif ch == 2:
#             viewtasks()
#
#         elif ch == 3:
#             searchtask()
#
#         elif ch == 4:
#             edittask()
#
#         elif ch == 5:
#             deletetask()
#
#         elif ch == 6:
#             print("Goodbye!")
#             break
#
#         else:
#             print("Invalid option")
#
#
# main()
