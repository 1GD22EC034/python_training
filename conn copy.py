import mysql.connector
def insert_data(id,name,email):


    mydb = mysql.connector.connect(
        host="localhost",
        user="root",        
        password="12345678",      
        database="raj_cse" 
    )    

    print("Connection successfully")
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (id,name,email)"
    "VALUES (%,%s,%s)"
    val = [id,name,email]
    mycursor.execute("select * from user1")
    result = mycursor.fetchall()
    for row in result:
        print(row)
    mydb.commit()
    mycursor.close()
    mydb.close()
    print(mycursor,row ,count, "record inserted.")
id = input("enter the id")
name = input("enter the name")
email = input("enter the email")   
insert_data(id,name,email)

