import mysql.connector as myconn


def delete(uid):
    conn = myconn.connect(host='localhost', database='practice', user='root', password='PASSWORD')

    cursor = conn.cursor()

    try:
        cursor.execute("delete from emp where id=%d" % uid)
        conn.commit()
        print("Employee removed")
    except:
        conn.rollback()
        print("Error removing employee")
    finally:
        cursor.close()
        conn.close()


def update(uid, name):
    conn = myconn.connect(host='localhost', database='practice', user='root', password='PASSWORD')

    cursor = conn.cursor()

    try:
        cursor.execute("update emp set name='%s' where id=%d" % (name, uid))
        conn.commit()
        print("Employee data updated")
    except:
        conn.rollback()
        print("Error updating employee data")
    finally:
        cursor.close()
        conn.close()


choice = input("Enter y to delete a record and n to update a record:")
if choice == 'y':
    delete(int(input("Enter the id:")))
elif choice == 'n':
    update(int(input("Enter the id:")), input("Enter the name:"))
else:
    print("Incorrect choice")
