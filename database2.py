import sqlite3

conn = sqlite3.connect("Mybook.db")
cursor = conn.cursor()

# # Create Author table
# cursor.execute(
#     '''
#     CREATE TABLE Author(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(20),
#     email VARCHAR(50),
#     phone INTEGER
#     )
#     '''
# )

# # Create Book table
# create.execute(
#     '''
#     CREATE TABLE Book(
#     Id INTEGER PRIMARY KEY AUTOINCREMENT,
#     Title VARCHAR(20),
#     Description TEXT,
#     Price INTEGER,
#     Author_id INTEGER,
#     FOREIGN KEY(Author_id) REFERENCES Author(Id)
#     )
#     '''
# )
# cursor.execute(
#     '''
#     INSERT INTO Author(name,email,phone)
#     VALUES("mohan","mohan@123.com",9852364178),
#     ("das","das@258.com",8596321475)
#     '''
# )
# conn.commit()

# cursor.execute(
#     '''
#     INSERT INTO Book(Title,Description,Price,Author_id)
#     VALUES("Changes","This book is not for everyone",234,1),
#     ("Super","Super Powers",500,2)
#     '''
# )
# conn.commit()

# Foreign Key – connecting two tables:
#
# FOREIGN KEY (author_id) REFERENCES Author(id)
