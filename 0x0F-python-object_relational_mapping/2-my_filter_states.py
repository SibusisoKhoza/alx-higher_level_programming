#!/usr/bin/python3
"""
takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb


def print_n_state():
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name\
        LIKE binary %s", [format(argv[4])])
    for rows in cur.fetchall():
        print(rows)

    cur.close()
    db.close()


if __name__ == "__main__":
    print_n_state()
