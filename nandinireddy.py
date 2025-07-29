import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="roottoor",
database="raj_cse"
)
print("Connected database successsfully.")