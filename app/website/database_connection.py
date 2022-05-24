#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="$salma2012",  # your password
                     db="logindata")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
cur.execute("SELECT * FROM logindata")

# print all the first cell of all the rows
#for i in cur.fetchall():
 #   print (i[0] , i[1] , i[2] )

db.close()