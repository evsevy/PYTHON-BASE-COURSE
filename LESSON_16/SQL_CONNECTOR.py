import pymssql 
import argparse
import sqlite3
import pandas as pd

conn = pymssql.connect(server='103.24.99.76', 
                        user='testUser', 
                        password='Abcd.1234', 
                        database='Portal_Data')

def get_sql():
    cursor = conn.cursor()
    cursor.execute("""SELECT *
                FROM sys.databases 
                WHERE name='Portal_Data' 
                """)                
    for row in cursor.fetchall(): 
        #print ('{}'.format(row[0]))
        print("%s\n" % str(row)) 
raww = get_sql()
conn.close()

#cursor = conn.cursor()
    #cursor.execute("""SELECT PARSE(name, database_id, create_date
                #FROM sys.databases) AS Result""")
    #cursor.execute("EXEC sp_databases")
    #cursor.execute("SELECT name FROM master.dbo.sysdatabases")
    #cursor.execute("""SELECT name, database_id, create_date
                #FROM sys.databases 
                #WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb') 
                #""")                
    #for row in cursor.fetchall(): 
        #print ('{}'.format(row[0]))
        #print("%s\n" % str(row))

import sqlite3
import csv
import os

def create_db_table():
    conn = sqlite3.connect('DATABASE.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Portal_Data 
             (Portal_Data)''')           
			
    conn.commit()
    conn.close()

def import_one_file_csv_to_sqlite():
    con = sqlite3.connect('DATABASE.db')
    cur = con.cursor()

    with open('C:\\Users\\AllOneNeon\\Python\\data.csv', 'r', encoding='utf-8') as open_csv:
        rows = csv.reader(open_csv, delimiter="|")
        
        for row in rows:
            cur.execute('INSERT INTO Portal_Data VALUES (?)', row)

    con.commit()
    con.close()  
                
if __name__ == '__main__':
    create_db_table()
    import_one_file_csv_to_sqlite()
