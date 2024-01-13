#!/usr/bin/python3
"""
takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
Safe from sql injection
"""

import MySQLdb


def print_n_state():
    from sys import argv
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (argv[4],))
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    db.close()


if __name__ == "__main__":
    print_n_state()
