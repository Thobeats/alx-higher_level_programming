#!/usr/bin/python3
"""
Write a script that takes in the name
of a state as an argument and lists
all cities of that state,
using the database hbtn_0e_4_usa
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
            SELECT cities.name
            FROM cities
            INNER JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    stateName = (argv[4],)
    cur.execute(sql, stateName)
    cities = cur.fetchall()

    if cities is not None:
        for i, city in enumerate(cities):
            if i < len(cities) - 1:
                print(city[0], end=", ")
            else:
                print(city[0])

    cur.close()
    conn.close()
