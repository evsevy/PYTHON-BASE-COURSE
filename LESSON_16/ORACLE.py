# importing module
import cx_Oracle

# Create a table in Oracle database
try:

	con = cx_Oracle.connect('tiger/scott@localhost:1521/xe')
	print(con.version)

	# Now execute the sqlquery
	cursor = con.cursor()

	# Creating a table employee
	cursor.execute(
		"create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")

	print("Table Created successfully")

except cx_Oracle.DatabaseError as e:
	print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()

#Просмотр набора результатов
#из запроса на выборку с помощью fetchall(), fetchmany(int), fetchone()		

import cx_Oracle

try:
	con = cx_Oracle.connect('tiger/scott@localhost:1521/xe')

except cx_Oracle.DatabaseError as er:
	print('There is an error in the Oracle database:', er)

else:
	try:
		cur = con.cursor()

		# fetchall() is used to fetch all records from result set
		cur.execute('select * from employee')
		rows = cur.fetchall()
		print(rows)

		# fetchmany(int) is used to fetch limited number of records from result set based on integer argument passed in it
		cur.execute('select * from employee')
		rows = cur.fetchmany(3)
		print(rows)

		# fetchone() is used fetch one record from top of the result set
		cur.execute('select * from employee')
		rows = cur.fetchone()
		print(rows)

	except cx_Oracle.DatabaseError as er:
		print('There is an error in the Oracle database:', er)

	except Exception as er:
		print('Error:'+str(er))

	finally:
		if cur:
			cur.close()

finally:
	if con:
		con.close()

# Вставка нескольких записей в таблицу с помощью метода executemany()

import cx_Oracle

# Load data from a csv file into Oracle table using executemany
try:
	con = cx_Oracle.connect('tiger/scott@localhost:1521/xe')

except cx_Oracle.DatabaseError as er:
	print('There is an error in Oracle database:', er)

else:
	try:
		cur = con.cursor()
		data = [[10007, 'Vikram', 48000.0], [10008, 'Sunil', 65000.1], [10009, 'Sameer', 75000.0]]

		cur = con.cursor()
		# Inserting multiple records into employee table
		# (:1,:2,:3) are place holders. They pick data from a list supplied as argument
		cur.executemany('insert into employee values(:1,:2,:3)', data)

	except cx_Oracle.DatabaseError as er:
		print('There is an error in Oracle database:', er)

	except Exception as er:
		print(er)

	else:
		# To commit the transaction manually
		con.commit()
		print('Multiple records are inserted successfully')

finally:
	if cur:
		cur.close()
	if con:
		con.close()

