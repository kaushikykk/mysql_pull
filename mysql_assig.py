#!/usr/bin/env python

import sys
import MySQLdb
import datetime
import os
import csv
from datetime import timedelta
from tabulate import tabulate

##Set user credentials as environment variables
MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASS = os.environ["MYSQL_PASS"]

#Creating a variable currentweek, which would be currentdate-7 days.
now = datetime.datetime.now()
Current_week = now - timedelta(days=7)
Current_week = Current_week.strftime("%Y-%m-%d %H:%M:%S")


# Database connection.
db = MySQLdb.connect("ultra01.clfb35oemeao.us-west-2.rds.amazonaws.com",MYSQL_USER,MYSQL_PASS,"Ultradb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# SQL query to fetch data
sql = "SELECT * FROM EVENTS \
       WHERE EVENT_START_TIME > '{}'".format(Current_week)

##Catch all the exceptions.
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print "{:25} {:20} {:25}".format("START_DATE","END_DATE","EVENT_NAME")
   for row in results:
     table =[[row[3]],[row[4]],[row[1]]]
      # Now print fetched result
     #table = ["{} {} {:25}".format(START_DATE,END_DATE,EVENT_NAME)]
    # table = [[row[3]], [row[4]], [row[1]]
     print tabulate(table)
except:
   print "Error: unable to fecth data"


# disconnect from server
db.close()
