import os
import sqlite3
import time
from time import sleep
from datetime import datetime

filename = "/home/pi/fdr_data/fdr_"
# set the the log frequency here
# 5 = every 5 seconds
logperiod = 2
theline = ""

now = datetime.now()
filename += str(now)[:19]
filename = filename.replace(" ","_")
filename = filename.replace(":","")
filename += ".csv"

#get the database ready
memdb = sqlite3.connect('/memdb/memdb.db')
cursor = memdb.cursor()

listOfTables = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'  AND name='messages'; """).fetchall()

while listOfTables == []:
	print('Table messages not found. Waiting for 3 seconds')
	time.sleep(3)
	listOfTables = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table'  AND name='messages'; """).fetchall()



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
