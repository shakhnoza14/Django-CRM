import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="hilo",
    passwd="chacho123!"
)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE website")

print("All Done!")