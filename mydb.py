import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mango12.' 
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE hanzacrm')

print("All done!!")