import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        
        password="12345678",      
        database="raj_cse"     
    )
    print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

mycursor = mydb.cursor


