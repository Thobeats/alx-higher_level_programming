#!/usr/bin/python3
"""
Write a script that lists all cities
from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=argv[1],
        passwd=argv[2], db=argv[3],
        charset="utf8"
        )
    cur = conn.cursor()
    sql = """
            SELECT cities.id, states.name, cities.name
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """
    cur.execute(sql)
    cities = cur.fetchall()

    if cities is not None:
        for city in cities:
            print(city)

    cur.close()
    conn.close()
