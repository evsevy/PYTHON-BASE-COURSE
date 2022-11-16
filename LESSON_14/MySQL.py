"""
import pymysql
 
con = pymysql.connect('localhost', 'user17', 
    's$cret', 'mydb')
 
with con:
    
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
 
    version = cur.fetchone()
    
    print("Database version: {}".format(version[0]))
    """
import pymysql
 
con = pymysql.connect('localhost', 'user17', 
    's$cret', 'testdb')
 
with con: 
 
    cur = con.cursor()
    cur.execute("SELECT * FROM cities")
 
    rows = cur.fetchall()
 
    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))
