import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="",
  database="mike"
)

mycursor = mydb.cursor()

mydb.commit()

print(mycursor.rowcount, "record(s) affected")