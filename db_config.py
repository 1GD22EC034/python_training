import mysql.connector
def getDb():
    mydb = mysql.connector.connector
        host="localhost",
        user="root",
        password="roottoor",
        databse="use_db"
    )
    return mydb