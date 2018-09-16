import sqlite3

def connect(): #this will connect connect to the database
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("create table if not exists book(id INTEGER PRIMARY KEY,title\
    text,author text,year integer, isbn integer)") #create the table in the database if not exist
    conn.commit()
    conn.close()

def insert(title,author,year,isbn): 
	"""
	This Function Function accept title , author , year ,isbn as argument.
	And Add the row to the database
	"""
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("insert into book values(NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
	"""
	This function will return all the rows present in the database
	"""
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("select * from book")
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
	"""
	Accepts title , author , year ,isbn as arguments.
	
	This Function Will return the specifies  rows depending on the value of its arguments. 
	"""
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("select * from book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete(id):
	"""
	This Function will accept id as argument.
	
	Delete the row having id it accepts.
	"""
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("delete from book where id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
	"""
	This function accepts  title , author , year ,isbn as arguments.
	
	This will update the row having id it accepts.
	"""
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("update  book set title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect() #this call calls the connect function to get connected to the database
