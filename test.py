import sqlite3

connection= sqlite3.connect("data.db")

cursor= connection.cursor()

create_table="CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user=(1, 'jose', 'asdfg')
insert_query= "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

users= [
    (2, 'rolf', 'qwer'),
    (3, 'jack', 'zxcv')
]
cursor.executemany(insert_query, users)

select_query= "SELECT * FROM users"
result=cursor.execute(select_query)
for row in result:
    print (row)
connection.commit()
connection.close()
