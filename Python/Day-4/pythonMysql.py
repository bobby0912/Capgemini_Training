import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql"
)

c=db.cursor()

c.execute("show databases")

for i in c:
    print(i)

c=db.cursor()
db.close()