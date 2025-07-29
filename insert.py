import sqlite3
conn = sqlite.connect("mydata.db")
cursor=conn.cursor()
cursor.execute("INSERT INTO users (name,age)VALUES (?,?)",("alice",25))