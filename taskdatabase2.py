import sqlite3
conn = sqlite3.connect('Mytasks.db')
cursor = conn.cursor()
#
# def dbint():
#     conn = sqlite3.connect("mytasks.db")
#     cursor = conn.cursor()
#     pass
#
#
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS User(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Username VARCHAR(255) UNIQUE,
    Password TEXT
    )
    '''
)
conn.execute(
    '''
    CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tname VARCHAR(255),
    tdesc TEXT,
    user_id INTEGER,
    FOREIGN KEY(user_id) REFERENCES User(Id)
    )
    '''
)
def register():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    cursor.execute(
        '''
        INSERT INTO User(Username,Password)
        VALUES(?,?)
        ''',(username,password)
    )
    conn.commit()
    print("User Registered")
def login():
    conn = sqlite3.connect('Mytasks.db')
    cursor = conn.cursor()
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    cursor.execute(
        '''
        SELECT id FROM User WHERE Username = ? AND Password = ?
        ''',(username,password)
    )
    User = cursor.fetchone()
    if User:
        print(User)
    else:
        print("Invalid Credentials")


# # if username and password
#
#
# def addtask(user_id):
#     conn = sqlite3.connect("mytasks.db")
#     cursor = conn.cursor()
#     name = input("enter taskname:")
#     des = input("enter des:")
#     cursor.execute('''
#         INSERT INTO tasks(tname,tdes,user_id)
#         VALUES(?,?,?)
#         ''', (name, des, user_id))
#     conn.commit()
#     print("TASK ADDEd 🤗")
#     conn.close()
#
#
# def viewtasks(user_id):
#     conn = sqlite3.connect("mytasks.db")
#     cursor = conn.cursor()
#     cursor.execute('''
#             SELECT * FROM tasks where user_id = ?
#         ''', (user_id,))
#     data = cursor.fetchall()  # retrives a list of data from the last executed querry
#     print("Tasks found  ☑️")
#     for i in data:
#         print(f"{i[0]}.task ---{i[1]} task description --- {i[2]}")
#
#
# def searchtask(user_id):
#     conn = sqlite3.connect("mytasks.db")
#     cursor = conn.cursor()
#     t_id = int(input("enter your task id :"))
#     cursor.execute(
#         "SELECT * FROM tasks WHERE id = ? and user_is = ?"
#         , (t_id, user_id)
#     )
#     task = cursor.fetchone()
#     if task:
#         print("Task found ✔️")
#         print(f"---{task[0]}---{task[1]}----{task[2]}-----")
#     else:
#         print("no such task😔")
#
#
# def edittask(user_id):
#     conn = sqlite3.connect("mytasks.db")
#     cursor = conn.cursor()
#     t_id = int(input("enter task id:-"))
#     name = input("enter new task name:-")
#     des = input("enter new des :-")
#     cursor.execute('''
#         UPDATE tasks SET tname = ? , tdes = ? WHERE id = ? AND user_id = ?
#         ''', (name, des, t_id, user_id))
#     conn.commit()
#     print("task updated")
#
#
# def deletetask(user_id):
#     conn = sqlite3.connect("mytasks.db")
#     cursor = conn.cursor()
#     t_id = int(input("enter task id:-"))
#
#     ch = input("Are you sure youn want to delete this task y/n:-")
#     if ch == "y":
#         cursor.execute(
#             '''DELETE FROM tasks WHERE id = ? and user_id = ?''', (t_id, user_id)
#         )
#         conn.commit()
#         print("Task deleted !!!!!!!!!!!!!!!!")
#     else:
#         print("Task not deleted !!!!!!!!!1")
#
#
# def sub(user_id):
#     print("wElcome to task management system")
#     while True:
#         ch = int(input(
#             "Eneter your choice\n1.Add TASk\n2.View tasks\n3.search task\n4.Edit tasks\n5.Delete task\n6.Exit\nenter choice:---"))
#         if ch == 1:
#             addtask(user_id)
#         elif ch == 2:
#             viewtasks(user_id)
#         elif ch == 3:
#             searchtask(user_id)
#         elif ch == 4:
#             edittask(user_id)
#         elif ch == 5:
#             deletetask(user_id)
#         elif ch == 6:
#             break
#         else:
#             print("invalid option")
#
#
# # main()
#
#
# def main():
#     print("Welcome to task management system")
#     while True:
#         ch = int(input("1.Login\n2.Register\n3.Exit"))
#         if ch == 1:
#             user_id = login()
#             if user_id:
#                 sub(user_id)
#         elif ch == 2:
#             register()
#         elif ch == 3:
#             break
#         else:
#             print("invalid choice")
#
#
# main()
