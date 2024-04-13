#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa 
"""

from sys import argv
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
cur = conn.cursor()

cur.execute("SELECT * FROM {}.states ORDER BY states.id ASC".format(argv[3]))
states = cur.fetchall()

for state in states:
    print(state)

cur.close()
conn.close()