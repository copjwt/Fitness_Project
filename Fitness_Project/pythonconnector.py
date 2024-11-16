import mysql.connector
from datetime import datetime
import re
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Copter482625#"
    database = "fitness"
)

mycursor = db.cursor()
mycursor.execute("CRATE TABLE User (UserID int(8) PRIMARY KEY AUTO INCREMENT)")
#mycursor.execute("INSERT INTO Person (name,age) VALUES (%s,%s)",("Cop",20))
#mycursor.execute("CREATE TABLE Test (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M','F','O')NOT NULL, ID int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
#db.commit()

# mycursor.execute("SELECT * FROM Person")
# for x in mycursor:
#     print(x)
