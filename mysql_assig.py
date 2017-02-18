#!/usr/bin/env python

import sys
import MySQLdb
import datetime
import os
import csv
from datetime import timedelta
from tabulate import tabulate

##Check if MYSQL_USER/MYSQL_PASS are null
if os.environ["MYSQL_USER"] == " " or os.environ["MYSQL_PASS"] == " ":
  print "Please declare MYSQL_USER and MYSQL_PASS"
  quit()
else:
  print 'MYSQL_USER/MYSQL_PASS exists'


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
sql = "SELECT  EVENT_START_TIME,EVENT_END_TIME,EVENT_NAME FROM EVENTS \
       WHERE EVENT_START_TIME > '{}'".format(Current_week)

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   print "{:25} {:25} {:25}".format("START_DATE","END_DATE","EVENT_NAME")
   print  tabulate(results)
except:
   print "Error: unable to fecth data"

db.close()
