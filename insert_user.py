import mysql.connector


name = input("Enter your name: ")
age = int(input("Enter your age: "))
email = input("Enter your email: ")


conn = None

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="test"
    )

    cursor = conn.cursor()


    query = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"
    values = (name, age, email)
    cursor.execute(query, values)
    conn.commit()

    print(" Data inserted!")

except mysql.connector.Error as err:
    print(f" MySQL Error: {err}")

finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()            