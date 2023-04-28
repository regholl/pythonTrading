import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password'
)

cur = mydb.cursor()
cur.execute('USE stocks_database')