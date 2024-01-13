#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa
"""

import MySQLdb


def print_n_state():
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")
    for rows in cursor.fetchall():
        if rows[1][0] == 'N':
            print(rows)

    cursor.close()
    db.close()


if __name__ == "__main__":
    print_n_state()
    