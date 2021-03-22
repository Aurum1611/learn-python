import mysql.connector as myconntr

conn = myconntr.connect(host='localhost', database='practice', user='root', password='PASSWORD')

if conn.is_connected():
    print("Connection established successfully")

cursor = conn.cursor()

try:
    cursor.execute("insert into emp values(789,'Jeff Bezos',1000000);")
    conn.commit()
    print("Employee added")
except:
    conn.rollback()
    print("Employee not added")

cursor.close()
conn.close()
