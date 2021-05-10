import os
import sqlite3
import time
from time import sleep
from datetime import datetime

filename = "/home/pi/fdr_data/fdr_"
# set the the log frequency here
# 5 = every 5 seconds
logperiod = 5
theline = ""

now = datetime.now()
filename += str(now)[:10]
filename += ".csv"

#get the database ready
memdb = sqlite3.connect('/memdb/memdb.db')
cursor = memdb.cursor()


file = open(filename, "a")

if os.stat(filename).st_size == 0:
	theline = "Time"
	cursor.execute("SELECT * FROM messages ORDER BY id")
	rows = cursor.fetchall()
	for row in rows:
		theline += "," + str(row[2])
	theline += "\n"
	file.write(theline)
	file.flush()
	file.close()
while True:
	file = open(filename, "a")
	now = datetime.now()
	theline = str(now)
	cursor.execute("SELECT * FROM messages ORDER BY id")
	rows = cursor.fetchall()
	for row in rows:
		theline += "," + str(row[3])
	theline += "\n"
#	print(theline)
	file.write(theline)
	file.flush()
	file.close()
	time.sleep(logperiod)
#file.close()
