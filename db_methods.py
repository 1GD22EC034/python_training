from db_config input getDb
class DbMethods:
    def insertData(self,id,name,email):
        mybd=getdb()
        mycursor = mydb.cursor()
        sql="INSERT INTO user1 (id,name,email)VALUES (%s,%s)"
        val = (id, name, email)
        mycursor.execute(sql,val)
    
