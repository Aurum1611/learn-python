import mysql.connector as connector

conn = connector.connect(host='localhost', database='practice', user='root', password='Youkoso@1699')

if conn.is_connected():
    print("Connection is successfully established")

    cursor = conn.cursor()

    cursor.execute("select * from emp order by id asc;")
    '''
    row=cursor.fetchone()
    while row is not None:
        print(row)
        row=cursor.fetchone()
    '''

    rows = cursor.fetchall()
    print("Total number of rows is", cursor.rowcount)
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
else:
    print("Connection failed")
