import mysql.connector

conn = mysql.connector.connect(host="localhost", database="practice", user="root", password="PASSWORD")

if conn.is_connected():
    print("Connection successfully established")

conn.close()
