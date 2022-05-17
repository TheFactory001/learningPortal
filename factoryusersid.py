import pymysql

db = pymysql.connect(
    host="factorydatabase.cx7bcz8zyphb.ca-central-1.rds.amazonaws.com",
    user="admin",
    password="th3f4ctory",
    database="project",
    port=3306)

mycursor = db.cursor()


#mycursor.execute("CREATE TABLE factoryUsers (userID int PRIMARY KEY NOT NULL AUTO_INCREMENT, username VARCHAR(50), email VARCHAR(50), password VARCHAR(50), country VARCHAR(50))")
#mycursor.execute("INSERT INTO factoryUsers (username, email, password, country) VALUES (%s,%s,%s,%s)",("FEMI", "obeolufemi@gmail.com", "Ultimat3", "Nigeria"))
# db.commit()


mycursor.execute("SELECT * FROM factoryUsers")

for x in mycursor:
    print(x)
