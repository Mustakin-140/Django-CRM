import mysql.connector
dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)
# prepare a cursor object
cursorObject=dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE seu")
print("Done!")