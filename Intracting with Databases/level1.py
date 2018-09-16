import sqlite3
def create_table():
    conn=sqlite3.connect("praful.db") #connect to the database
    cur=conn.cursor() #create a cursor to access the database
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT , quantity INTEGER, price REAL)") #this will create a table in database if the table does not exist
    conn.commit()
    conn.close()
def insert(item,quantity,price):
    conn=sqlite3.connect("praful.db") #connect to the database
    cur=conn.cursor() #create a cursor to access the database
    cur.execute("INSERT INTO store values(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

create_table()
insert("coffe cup",10,5)

def view():
    conn=sqlite3.connect("praful.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows
print(view())
