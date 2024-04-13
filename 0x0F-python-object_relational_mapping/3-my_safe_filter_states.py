#!/usr/bin/python3
"""
write a script that takes in arguments
and displays all values in the states
table of hbtn_0e_0_usa where name matches
the argument. But this time,
write one that is safe from
MySQL injections!
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
            SELECT * FROM {}.states WHERE name LIKE BINARY
            %s ORDER BY states.id ASC
            """
    value = (argv[4],)
    cur.execute(sql.format(argv[3]), value)
    states = cur.fetchall()

    if states is not None:
        for state in states:
            print(state)

    cur.close()
    conn.close()
