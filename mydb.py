import mysql.connector
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Maed',

)
cursorObject= dataBase.cursor()

cursorObject.execute("CREATE DATABASE maedeh")

print("All Done!")