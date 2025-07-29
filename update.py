import sqlite3
conn = sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("update user set name ='anjali' where id=1")
conn.commit()
conn.close()